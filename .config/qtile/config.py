import os
import subprocess
from collections.abc import Callable
import libqtile.resources
from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Output, Screen, DropDown, ScratchPad
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn("bash /home/nasadmi/.config/rofi/launchers/type-4/launcher.sh")),
    Key([mod], "v", lazy.spawn("bash /home/nasadmi/.config/rofi/launchers/type-1/launcher.sh")),
    Key([mod, "shift"], "v", 
        lazy.spawn("bash -c 'greenclip clear && pkill -RTMIN+1 greenclip && notify-send \"Clipboard cleared\"'"), 
        desc="Clear clipboard"
    ),
    Key([mod, "shift"], "Return", lazy.group['scratchpad'].dropdown_toggle('kitty')),
    Key([mod], "a", lazy.group['scratchpad'].dropdown_toggle('pavucontrol')),
    Key([mod, "shift"], "b", lazy.group['scratchpad'].dropdown_toggle('blueman-manager')),
    Key([mod], "b", lazy.spawn('google-chrome-stable')),
    Key([mod], "e", lazy.spawn('thunar')),
    Key([mod], 'period', lazy.next_screen(), desc='Next monitor'),
    Key([mod], 'comma', lazy.prev_screen(), desc='Previous monitor'),
    Key([mod], "s", lazy.spawn('flameshot gui')),
    Key([mod], "p", lazy.group['scratchpad'].dropdown_toggle('pear-desktop')),
    Key([mod], "Space", lazy.widget["keyboardlayout"].next_keyboard(), desc="Next keyboard layout"),
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


colors = {
    "bg": "#141414",
    "active": "#FF0055",
    "special": "#9E00FF",
    "fg": "#FFF",
    "blue": "#23BAD5",
    "yellow": "#ffff00",
    "orange": "#ff8700",
    "green": "#37BE69",
    "inactive": "#666",
}

group_names = ["1", "2", "3", "4", "5", "6"]
group_labels = ["", "", "", "", "", ""]

groups = []

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            label=group_labels[i],
        )
    )

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

groups.append(
    ScratchPad("scratchpad", [
        DropDown("kitty", "kitty", opacity=0.9, height=0.6, width=0.7, x=0.15, y=0.1),
        DropDown("pavucontrol", "pavucontrol", opacity=0.9, height=0.6, width=0.7, x=0.15, y=0.1),
        DropDown("blueman-manager", "blueman-manager", opacity=0.9, height=0.6, width=0.7, x=0.15, y=0.1),
        DropDown("pear-desktop", "pear-desktop", opacity=0.9, height=0.8, width=0.9, x=0.05, y=0.1)
    ]),
)

layouts = [
    layout.MonadTall(border_focus=colors['special'], border_normal=colors['inactive'], border_width=3, margin=3),
    layout.MonadWide(border_focus=colors['special'], border_normal=colors['inactive'], border_width=3, margin=3),
    layout.Bsp(border_focus=colors['special'], border_normal=colors['inactive'], border_width=3, margin=3),
    layout.Max(),
    # layout.Columns(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Matrix(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

def left_circle_icon():
    return widget.TextBox(
        text="\uE0B6",
        fontsize=38,
        foreground=colors['bg'],
        padding=-1
    )

def right_circle_icon():
    return widget.TextBox(
        text="\uE0B4",
        fontsize=38,
        foreground=colors['bg'],
        padding=0,
    )

def icon(bg=colors['bg'], fg=colors['fg'], txt='?', p=8):
    return widget.TextBox(
        text=txt,
        fontsize=16,
        background=bg,
        foreground=fg,
        padding=p
    )

def baseWidgets():
    return [
        left_circle_icon(),
        widget.GroupBox(
            background=colors['bg'],
            highlight_method='text',
            this_current_screen_border=colors['fg'],
            other_current_screen_border=colors['fg'],
            inactive=colors['inactive'],
            active=colors['special'],
            padding_x=5,                        
            fontsize=14,                               
            disable_drag=True,
            urgent_alert_method='text',
            urgent_text=colors['active'],
            use_mouse_wheel=False,
        ),
        right_circle_icon(),
        widget.Spacer(length=5),
        left_circle_icon(),
        icon(txt="", fg=colors['green']),
        widget.Mpris2(
            background=colors['bg'],
            foreground=colors['green'],
            font='Hack Nerd Font Mono Bold',
            no_metadata_text='',
            paused_text='{track}',
            display_metadata=['xesam:title', 'xesam:artist'],
            max_chars=30,
            mouse_callbacks={},
        ),
        right_circle_icon(),
        widget.Spacer(),
        left_circle_icon(),
        icon(txt="", fg=colors['active']),
        widget.CurrentLayout(
            background=colors['bg'],
            foreground=colors['active'],
            font="Hack Nerd Font Mono Bold",
            padding_x=-1,
        ),
        right_circle_icon(),
        widget.Spacer(length=5),
        left_circle_icon(),
        icon(txt="", fg=colors['special']),
        widget.Clock(
            format="%Y-%m-%d %I:%M:%S",
            foreground=colors['special'],
            background=colors['bg'],
            font="Hack Nerd Font Mono Bold",
            padding_x=1
        ),
        right_circle_icon(),
        widget.Spacer(length=5),
        left_circle_icon(),
        icon(txt='󰁹', fg=colors['yellow'], p=1),
        widget.Battery(
            update_interval=15,
            full_short_text='100%',
            format='{percent:2.0%}',
            foreground=colors['yellow'],
            background=colors['bg'],
            font='Hack Nerd Font Mono Bold'
        ),
        icon(txt='', fg=colors['blue'], p=9),
        widget.PulseVolume(
            background=colors['bg'],
            foreground=colors['blue'],
            emoji=False,
            font='Hack Nerd Font Mono Bold',
            fmt='{}',
            mouse_callbacks={},
            mute_format=''
        ),
        icon(txt='󰤨', fg=colors['orange'], p=9),
        widget.Net(
            interface='wlp0s20f3',
            format='{down:.0f}{down_suffix}  {up:.0f}{up_suffix}',
            font='Hack Nerd Font Mono Bold',
            background=colors['bg'],
            foreground=colors['orange'],
        ),
        icon(txt='󰌌', fg=colors["green"]),
        widget.KeyboardLayout(
            background=colors['bg'],
            configured_keyboards=['us', 'es'],
            font="Hack Nerd Font Mono Bold",
            foreground=colors['green']
        ),
        right_circle_icon()
    ]


logo = os.path.join(os.path.dirname(libqtile.resources.__file__), "logo.png")
screens = [
    Screen(
        top=bar.Bar(baseWidgets(), 38,
            font="Hack Nerd Font Mono",
            background="#00000000",
            margin = [10, 10, 10, 10],),
    ),
    Screen(
        top=bar.Bar(baseWidgets(), 38,
            font="Hack Nerd Font Mono",
            background="#00000000",
            margin = [10, 10, 10, 10],),
    ),
]

# Instead of screens, you can define a function here to specify which Screen
# should correspond to which Output.
fake_screens: list[Screen] | None = None

# Instead of screens or fake screens, you can define a function here that
# returns a list of Screen objects based on the list of Outputs; that way you
# can decide based on e.g. the number of screens, or which ports are plugged
# in exactly what do render in each bar for each screen.
generate_screens: Callable[[list[Output]], list[Screen]] | None = None

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    border_focus=colors['special'],
    border_normal=colors['inactive'],
    border_width=3,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class='google-chrome', title='Save File')
    ],
    default_float_size=(800, 600),
)

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

auto_fullscreen = True
focus_on_window_activation = "smart"
focus_previous_on_window_remove = False
reconfigure_screens = True
cursor_warp = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

idle_timers = []  # type: list
idle_inhibitors = []  # type: list

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
