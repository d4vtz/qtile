from libqtile import widget


def set_widgets():
    return [
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
