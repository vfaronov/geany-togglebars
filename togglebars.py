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
    __plugin_version__ = '0.2.1'
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

    def cleanup(self):
        self.toggle(True)       # Show everything
