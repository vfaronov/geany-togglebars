Geany Toggle Bars plugin
========================

This is a plugin for `Geany`__
to show and hide the menu and status bars with a keystroke.

__ http://geany.org/

Most of the time, when using Geany,
I don't need the menu and status bars; they are just noise.
But occasionally I want to check the status bar
(e.g. for the line/column number)
or browse the menu.
So I want to toggle their visibility with a keystroke.
This plugin does that.

Because it's so useful to see the progress bar during a build,
the status bar will be automatically shown whenever the progress bar is shown
(and hidden afterwards).


Installation
------------

**Caution.** When enabled, this plugin removes your Geany menu bar,
which might confuse you and prevent you from disabling it.
If you're lost, start Geany with the ``--no-plugins`` option,
or simply uninstall the plugin code.

#. Install Geany 1.27.
   The plugin relies on undocumented internals
   and may not work with newer versions.

#. Make sure that "Show status bar"
   (Geany preferences → Interface → Miscellaneous)
   is **enabled**.

#. Install `GeanyPy`__.
   On Debian/Ubuntu, install ``geany-plugin-py``
   `as well as`__ ``python-gtk2``.

#. Put ``togglebars.py`` on your `Geany plugin path`__,
   e.g. in ``~/.config/geany/plugins/``.

#. Open Geany's plugin manager (Tools → Plugin Manager)
   and enable GeanyPy and Toggle Bars.

#. Select Toggle Bars, click Keybindings,
   and set your preferred key for "Toggle menu and status bars".

__ http://plugins.geany.org/geanypy.html
__ https://bugs.launchpad.net/ubuntu/+source/geany-plugins/+bug/1592928
__ http://www.geany.org/manual/current/index.html#plugins
