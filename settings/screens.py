from libqtile import bar, widget
from libqtile.config import Screen


def set_screens():
    widgets = [
        widget.CurrentLayout(),
        widget.GroupBox(),
        widget.Prompt(),
        widget.WindowName(),
        widget.Chord(
            chords_colors={
                "launch": ("#ff0000", "#ffffff"),
            },
            name_transform=lambda name: name.upper(),
        ),
        widget.TextBox("default config", name="default"),
        widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
        widget.Systray(),
        widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
        widget.QuickExit(),
    ]

    return [
        Screen(
            top=bar.Bar(
                widgets=widgets,
                size=22,
                margin=[6, 6, 6, 6],  # [N. E. S, W]
                opacity=0.8,
            ),
            wallpaper="~/.config/qtile/archlinux.png",
            wallpaper_mode="fill",
        )
    ]
