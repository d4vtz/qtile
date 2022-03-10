from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from .functions import (focus_next_group, focus_previous_group, resize_down,
                        resize_left, resize_right, resize_up)
from .groups import set_groups


class Directions:
    def __init__(self, vim_mode=False):
        if vim_mode:
            self.left = "h"
            self.down = "j"
            self.up = "k"
            self.right = "l"
        else:
            self.left = "Left"
            self.down = "Down"
            self.up = "Up"
            self.right = "Right"


class Modifiers:
    mod = "mod4"
    alt = "mod1"
    ctrl = "control"
    shift = "shift"

    super = [mod]
    control = [ctrl]
    super_shift = [mod, shift]
    super_ctrl = [mod, ctrl]
    super_alt = [mod, alt]


def set_keys():
    keys = []
    directions = Directions(vim_mode=False)
    alt_directions = Directions(vim_mode=True)
    modifiers = Modifiers()

    # Recargar y Salir de Qtile
    keys.extend(
        [
            Key(
                modifiers.super_shift,
                "r",
                lazy.restart(),
                desc="Reiniciar Qtile",
            ),
            Key(
                modifiers.super_ctrl,
                "q",
                lazy.shutdown(),
                desc="Salir de Qtile",
            ),
        ]
    )

    # Cambiar el tamaño de las ventanas
    keys.extend(
        [
            Key(
                modifiers.super,
                alt_directions.left,
                resize_left,
                desc="Cambiar el tamaño de las ventanas hacia la izquierda",
            ),
            Key(
                modifiers.super,
                alt_directions.down,
                resize_down,
                desc="Cambiar el tamaño de las ventanas hacia abajo",
            ),
            Key(
                modifiers.super,
                alt_directions.up,
                resize_up,
                desc="Cambiar el tamaño de las ventanas hacia arriba",
            ),
            Key(
                modifiers.super,
                alt_directions.right,
                resize_right,
                desc="Cambiar el tamaño de las ventanas hacia la derecha",
            ),
            Key(
                modifiers.super,
                directions.left,
                lazy.layout.left(),
                desc="Mover foco a la izquierda",
            ),
            Key(
                modifiers.super,
                directions.right,
                lazy.layout.right(),
                desc="Mover foco a la derecha",
            ),
            Key(
                modifiers.super,
                directions.down,
                lazy.layout.down(),
                desc="Mover foco hacia abajo",
            ),
            Key(
                modifiers.super,
                directions.up,
                lazy.layout.up(),
                desc="Mover foco hacia arriba",
            ),
        ]
    )

    # Cambiar posición de la ventana enfocada.
    keys.extend(
        [
            Key(
                modifiers.super_shift,
                directions.left,
                lazy.layout.shuffle_left(),
                desc="Mover ventana hacia la izquierda",
            ),
            Key(
                modifiers.super_shift,
                directions.right,
                lazy.layout.shuffle_right(),
                desc="Mover ventana hacia la derecha",
            ),
            Key(
                modifiers.super_shift,
                directions.down,
                lazy.layout.shuffle_down(),
                desc="Mover ventana hacia abajo",
            ),
            Key(
                modifiers.super_shift,
                directions.up,
                lazy.layout.shuffle_up(),
                desc="Mover ventana hacia arriba",
            ),
            Key(
                modifiers.super,
                "Tab",
                lazy.next_layout(),
                desc="Cambiar entre diferentes layouts",
            ),
            Key(
                modifiers.super,
                "q",
                lazy.window.kill(),
                desc="Cerrar ventana enfocada",
            ),
            Key(
                modifiers.super,
                "space",
                lazy.spawncmd(),
                desc="Ejecutar un comando usando el widget de prompt",
            ),
            Key(
                modifiers.super_ctrl,
                "Return",
                lazy.layout.toggle_split(),
                desc="Rotar ventanas",
            ),
        ]
    )

    for index, group in enumerate(set_groups(), start=1):
        keys.append(
            Key(
                modifiers.super,
                str(index),
                lazy.group[group.name].toscreen(),
            )
        ),
        keys.append(
            Key(
                modifiers.super_shift,
                str(index),
                lazy.window.togroup(group.name),
            )
        )
    keys.extend(
        [
            Key(
                modifiers.control,
                directions.left,
                lazy.function(focus_previous_group),
            ),
            Key(
                modifiers.control,
                directions.right,
                lazy.function(focus_next_group),
            ),
        ]
    )

    # Accesos a aplicaciones
    keys.extend(
        [
            Key(
                modifiers.super,
                "Return",
                lazy.spawn(guess_terminal()),
                desc="Lanzar terminal",
            ),
            Key(
                modifiers.super_shift,
                "Return",
                lazy.spawn("rofi -show drun -theme ~/.config/rofi/nord.rasi"),
                desc="Lanzar rofi",
            ),
            Key(
                modifiers.super,
                "w",
                lazy.spawn("google-chrome-stable"),
                desc="Lanzar el navegador.",
            ),
            Key(
                modifiers.super,
                "f",
                lazy.spawn("thunar"),
                desc="Lanzar el administrador de archivos.",
            ),
        ]
    )

    return keys
