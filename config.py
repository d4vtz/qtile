from libqtile.config import Match
from libqtile.layout.columns import Columns
from libqtile.layout.floating import Floating
from libqtile.layout.max import Max

from settings.groups import set_groups
from settings.hooks import autostart
from settings.keys import set_keys
from settings.screens import set_screens

autostart()

keys = set_keys()
groups = set_groups()
screens = set_screens()

layouts = [
    Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    Max(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()


dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = Floating(
    float_rules=[
        *Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"
