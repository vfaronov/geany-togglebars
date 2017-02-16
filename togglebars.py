import os

import geany
import gtk


class ToggleBars(geany.Plugin):

    __plugin_name__ = 'Toggle Bars'
    __plugin_version__ = '0.4.0'
    __plugin_description__ = \
        'Show/hide the Geany menu and status bars with a keystroke'
    __plugin_author__ = 'Vasiliy Faronov <vfaronov@gmail.com>'

    def __init__(self):
        super(ToggleBars, self).__init__()
        self.confirmed = self.confirm()

        # The plugin API does not expose the menu and status bars directly.
        # To avoid relying on a particular layout of the main window
        # (which may change in future Geany releases), we recursively walk
        # the main window's children to find the right kind of widget.
        # See also http://lists.geany.org/pipermail/devel/2016-July/010038.html
        self.menubar = find_widget(geany.main_widgets.window, is_main_menubar)
        self.statusbar = find_widget(geany.main_widgets.window,
                                     is_main_statusbar)

        self.currently_visible = None
        self.toggle(False)       # Hide initially

        self.progressbar = geany.main_widgets.progressbar
        self.handler1 = self.progressbar.connect('show', self.on_progress_show)
        self.handler2 = self.progressbar.connect('hide', self.on_progress_hide)

        self.key_group = self.set_key_group('togglebars', 1)
        self.key_group.add_key_item('toggle', 'Toggle menu and status bars',
                                    self.on_keybinding)

    def confirm(self):
        # http://lists.geany.org/pipermail/devel/2016-July/010044.html
        path = os.path.join(geany.app.configdir, 'plugins', 'togglebars.on')
        text = ('The Toggle Bars plugin is about to hide your Geany menu bar. '
                'You need to set a keybinding to toggle it.\n\n'
                'If you get stuck, you can bring the menu bar back '
                'by removing this file and restarting Geany:\n\n'
                '%s\n\nEnable the Toggle Bars plugin now?' % path)
        if not os.path.exists(path):
            if geany.dialogs.show_question(text):
                create_empty_file(path)
        return os.path.exists(path)

    def on_keybinding(self, *_args):
        self.toggle()

    def toggle(self, show=None):
        if not self.confirmed:
            return
        if show is None:
            show = not self.currently_visible
        for widget in [self.menubar, self.statusbar]:
            if widget is not None:
                if show:
                    widget.show()
                else:
                    widget.hide()
        self.currently_visible = show

    def on_progress_show(self, *_args):
        if self.confirmed:
            if not self.currently_visible and self.statusbar is not None:
                self.statusbar.show()

    def on_progress_hide(self, *_args):
        if self.confirmed:
            if not self.currently_visible and self.statusbar is not None:
                self.statusbar.hide()

    def cleanup(self):
        self.toggle(True)       # Show everything
        self.progressbar.disconnect(self.handler1)
        self.progressbar.disconnect(self.handler2)


def create_empty_file(path):
    dir_path = os.path.dirname(path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    with open(path, 'w'):
        pass


def find_widget(origin, predicate):
    if predicate(origin):
        return origin
    elif isinstance(origin, gtk.Container):
        for child in origin.get_children():
            r = find_widget(child, predicate)
            if r is not None:
                return r
    return None


def is_main_menubar(widget):
    return (isinstance(widget, gtk.MenuBar) and
            any(menu_item.get_submenu() is geany.main_widgets.tools_menu
                for menu_item in widget.get_children()))


def is_main_statusbar(widget):
    return (isinstance(widget, gtk.Statusbar) and
            find_widget(widget, lambda w: w is geany.main_widgets.progressbar))
