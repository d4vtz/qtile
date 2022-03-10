from libqtile import bar
from libqtile.config import Screen

from .widgets import set_widgets


def set_screens():

    return [
        Screen(
            top=bar.Bar(
                widgets=set_widgets(),
                size=22,
                margin=[6, 6, 6, 6],  # [N. E. S, W]
                opacity=0.8,
            ),
            wallpaper="~/.config/qtile/archlinux.png",
            wallpaper_mode="fill",
        )
    ]
