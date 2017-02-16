import geany
import gtk


def resolve_widget(top, indices, expected_cls):
    node = top
    indices = list(indices)
    while indices and isinstance(node, gtk.Container):
        try:
            node = node.get_children()[indices.pop(0)]
        except IndexError:
            return None
    return node if isinstance(node, expected_cls) else None


class ToggleBars(geany.Plugin):

    __plugin_name__ = 'Toggle Bars'
    __plugin_version__ = '0.4.0.dev1'
    __plugin_description__ = \
        'Show/hide the Geany menu and status bars with a keystroke'
    __plugin_author__ = 'Vasiliy Faronov <vfaronov@gmail.com>'

    def __init__(self):
        super(ToggleBars, self).__init__()
        self.menubar = resolve_widget(geany.main_widgets.window,
                                      (0, 0, 0), gtk.MenuBar)
        self.statusbar = resolve_widget(geany.main_widgets.window,
                                        (0, -1, 0), gtk.Statusbar)
        self.currently_visible = None
        self.toggle(False)       # Hide initially

        self.progressbar = geany.main_widgets.progressbar
        self.handler1 = self.progressbar.connect('show', self.on_progress_show)
        self.handler2 = self.progressbar.connect('hide', self.on_progress_hide)

        self.key_group = self.set_key_group('togglebars', 1)
        self.key_group.add_key_item('toggle', 'Toggle menu and status bars',
                                    self.on_keybinding)

    def on_keybinding(self, *_args):
        self.toggle()

    def toggle(self, show=None):
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
        if not self.currently_visible and self.statusbar is not None:
            self.statusbar.show()

    def on_progress_hide(self, *_args):
        if not self.currently_visible and self.statusbar is not None:
            self.statusbar.hide()

    def cleanup(self):
        self.toggle(True)       # Show everything
        self.progressbar.disconnect(self.handler1)
        self.progressbar.disconnect(self.handler2)
