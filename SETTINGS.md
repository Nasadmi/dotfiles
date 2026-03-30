# Configuration and File Paths

This document details the exact location of the configuration files for each software included in these dotfiles. **Note:** All paths are relative to the ```$HOME``` directory.

|Software|Configuration Path|Description|
|--------|---------------------|-----------|
**Qtile**|```~/.config/qtile/config.py```|Main window manager configuration.|
**Kitty**|```~/.config/kitty/kitty.conf```|Terminal settings, fonts, and colors.|
**Fish**|```~/.config/fish/config.fish```|Aliases, functions, and interactive shell configuration.|
**Picom**|```~/.config/picom/picom.conf```|Composer settings (opacity, shadows, animations).|
|**Rofi**|```~/.config/rofi```|Main directory for launchers and shutdown menus.|
**Dunst**|```~/.config/dunst/dunstrc```|Notification style and behavior.|
**Starship**|```~/.config/starship.toml```|Customization of the shell prompt.|
**Greenclip**|```~/.config/greenclip.toml```|Clipboard history settings.|
**GTK 3.0/4.0**|```~/.config/gtk-x.0/settings.ini```|Consistency of themes, icons, and fonts for GTK apps.|
|**GTK 2.0**|```~/.gtkrc-2.0```|Consistency of themes, icons, and fonts for apps using GTK 2.0.|

# Qtile Recovery (Backup)

This file is a verified and working version of Qtile. If your main config.py file fails, follow these steps to restore the system:

1. Create a backup of your current (corrupted) configuration:

```bash
mv ~/.config/qtile/config.py ~/.config/qtile/config.py.bak
```

2. Replace it with the default version:
```bash
cp ~/.config/qtile/default_config.py ~/.config/qtile/config.py
```

3. Restart Qtile: Press ```mod + Control + r``` (if the session is still active) or restart the session manager (SDDM).

# Startup Applications
## Systemd
- **bluetoothctl**: Bluetooth device management (system-wide)
- **sddm**: Display manager (system-wide)
- **greenclip**: Clipboard history (user-level)
## Autostart
Qtile has an `autostart.sh` script that starts interface elements:
```bash
# ~/.config/qtile/autostart.sh
udiskie -t &
dunst &
picom --config $HOME/.config/picom/picom.conf &
feh --bg-scale $HOME/wallpapers/default.png &
```
- **Udiskie**: External storage device management
- **Dunst**: Notification system
- **Picom**: Composer
- **Feh**: Wallpaper manager

# GTK Application Themes
```lxappearance``` is recommended To modify GTK-3.0:

- Make a copy for GTK-4.0:
```bash
`cp ~/.config/gtk-3.0/settings.ini ~/.config/gtk-4.0/settings.ini`
```
- For GTK-2.0, I used the same names, but adapted them to the syntax (example):
```ini
; ~/.config/gtk-3.0/settings.ini
[Settings]
gtk-theme-name=Tokyonight-BL-MB-Dark-Dark-Moon
```
```bash
# ~/.gtkrc-2.0
gtk-theme-name="Tokyonight-BL-MB-Dark-Dark-Moon"
```
To download and install new themes (at the user level):
- Themes: Copy the theme into ```~/.local/share/themes```
```bash
cp ~/Downloads/[Theme] ~/.local/share/themes
```
- Icons:
    - Icons section of ```lxappearance```
    - Copy it to ```~/.local/share/icons```
- Cursors:
    - Cursors section of ```lxappearance```
    - Copy it to ```~/.local/share/icons```
- Local Fonts
    - Copy it to ```~/.local/share/fonts```

It is recommended to use the [Pling](https://www.pling.com/browse?cat=148&ord=latest) website to find themes, icons, and cursors.