# Importaciones
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Screen, Match
from libqtile.lazy import lazy
from libqtile import qtile
import subprocess

# Modo principal
mod = "mod4"
terminal = "alacritty"  # Cambia a tu terminal preferida

# Colores
colors = {
    "background": "#282c34",
    "foreground": "#abb2bf",
    "highlight": "#61afef",
    "urgent": "#e06c75",
}

# Atajos de teclado
keys = [
    # Cambiar entre ventanas
    Key([mod], "h", lazy.layout.left(), desc="Mover foco a la izquierda"),
    Key([mod], "l", lazy.layout.right(), desc="Mover foco a la derecha"),
    Key([mod], "j", lazy.layout.down(), desc="Mover foco hacia abajo"),
    Key([mod], "k", lazy.layout.up(), desc="Mover foco hacia arriba"),
    Key([mod], "space", lazy.layout.next(), desc="Mover foco a otra ventana"),

    # Mover ventanas entre columnas izquierda/derecha o arriba/abajo en la pila actual
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Mover ventana a la izquierda"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Mover ventana a la derecha"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Mover ventana hacia abajo"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Mover ventana hacia arriba"),

    # Agrandar ventanas
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Ampliar ventana a la izquierda"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Ampliar ventana a la derecha"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Ampliar ventana hacia abajo"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Ampliar ventana hacia arriba"),

    # Restablecer tamaños de ventana
    Key([mod], "n", lazy.layout.normalize(), desc="Restablecer todos los tamaños de ventana"),

    # Alternar entre vistas divididas y no divididas de la pila
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Alternar entre vistas divididas y no divididas de la pila"),

    # Lanzar terminal
    Key([mod], "Return", lazy.spawn(terminal), desc="Abrir terminal"),

    # Cambiar entre diseños
    Key([mod], "Tab", lazy.next_layout(), desc="Cambiar entre diseños"),

    # Cerrar ventana
    Key([mod], "q", lazy.window.kill(), desc="Cerrar ventana activa"),

    # Recargar configuración de Qtile
    Key([mod, "control"], "r", lazy.restart(), desc="Recargar configuración"),

    # Apagar Qtile
    Key([mod, "control"], "q", lazy.shutdown(), desc="Apagar Qtile"),

    # Lanzar programas comunes
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Lanzar Rofi"),
    Key([mod], "g", lazy.spawn("google-chrome-stable"), desc="Lanzar Google Chrome"),

    # Lanzar Rofi y actualizar Qtile
    Key([mod, "mod1"], "r", lazy.spawn("rofi -show drun"), desc="Lanzar Rofi"),

    # Control de brillo con brightnessctl
    Key([mod], "F5", lazy.spawn("brightnessctl set 5%-"), desc="Bajar el brillo"),
    Key([mod], "F6", lazy.spawn("brightnessctl set 5%+"), desc="Subir el brillo"),
    # Atajo para bajar el volumen (Mod + F7)
    Key([mod], "F11", lazy.spawn("pamixer --decrease 1"), desc="Bajar el volumen"),
    # Atajo para subir el volumen (Mod + F8)
    Key([mod], "F12", lazy.spawn("pamixer --increase 1"), desc="Subir el volumen"),
    Key([mod], "F1", lazy.spawn("playerctl play-pause"), desc="Pausar/Reanudar reproducción"),
    Key([mod], "F10", lazy.spawn("amixer -q set Master toggle"), desc="Silenciar/Desilenciar parlantes"),
    Key([mod], "p", lazy.spawn("screen")),
    Key([mod], "p", lazy.spawn("scrot /home/mkm/images_screanshots/"), desc="Screenshots"),
]

# Grupos de ventanas
groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(), desc=f"Cambiar a grupo {i.name}"),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True), desc=f"Mover ventana activa a grupo {i.name}"),
    ])

# Diseños de ventanas
layouts = [
    layout.MonadTall(
        border_focus=colors["highlight"],
        margin=8,
    ),
    layout.Max(),
    layout.MonadWide(
        border_focus=colors["highlight"],
        margin=8,
    ),
]

# Configuración de los widgets de la barra
widget_defaults = dict(
    font="JetBrains Mono",
    fontsize=14,
    padding=5,
    background=colors["background"],
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    fontsize=16,
                    margin_y=3,
                    margin_x=0,
                    padding_y=5,
                    padding_x=5,
                    borderwidth=1,
                    active=colors["highlight"],
                    inactive=colors["foreground"],
                    rounded=False,
                    highlight_color=colors["background"],
                    highlight_method="line",
                    this_current_screen_border=colors["highlight"],
                    this_screen_border=colors["background"],
                    other_current_screen_border=colors["foreground"],
                    other_screen_border=colors["background"],
                    foreground=colors["foreground"],
                ),
                widget.WindowName(
                    fontsize=16,
                    foreground=colors["foreground"],
                    padding=5,
                ),
                widget.Systray(
                    background=colors["background"],
                    padding=5,
                ),
                widget.Clock(
                    fontsize=14,
                    foreground=colors["foreground"],
                    format="%Y-%m-%d %H:%M",
                    padding=5,
                ),
            ],
            24,
            background=colors["background"],
        ),
    ),
]

# Configuración adicional
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []

follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
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

qtile.cmd_spawn("picom --config /home/mkm/.config/picom.conf")


wmname = "LG3D"
