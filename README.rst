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


Installation
------------

#. Install Geany 1.27.
   The plugin relies on undocumented internals
   and may not work with newer versions.

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
