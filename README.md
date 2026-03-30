# Qtile Dotfiles: Minimal Arch Linux
A Qtile (X11)-based desktop environment optimized for efficiency and aesthetics. This setup uses a vibrant color palette of blue, yellow, and orange, with complete automation for fresh Arch Linux installations.

- [**Spanish Version**](./README.es.md)

![Desktop](./screenshots/desktop.png)
---
![Terminal](./screenshots/terminal.png)

## Installation Instructions
Designed for deployment on Arch Linux Minimal. The installation script manages dependencies, themes, icons, cursors, and system services.

- Setup Time: ~7 minutes
- Required Space in root (/): 10 GB (minimum) 25 GB (recommended)

```bash
git clone https://github.com/Nasadmi/dotfiles.git
cd dotfiles
chmod +x install.sh
./install.sh
```
----
## Keyboard Shortcuts
The ```mod``` key is configured as the Super key (Windows).

## Window and System Management
| Shortcut | Action |
|--------|--------|
```mod + Enter``` | Open terminal (Kitty) |
```mod + w``` | Close focused window |
```mod + f```|Toggle full screen |
```mod + t```|Toggle floating state |
```mod + Tab```|Toggle between layouts |
```mod + Control + r```|Restart Qtile|
```mod + Control + q```|Shutdown Qtile|
```mod + .``` / ```mod + ,```|Switch between monitors (Next/Previous)|
```mod + Space```|Change keyboard layout (es,us by default)|

### Navigation and Layout
**Based on Vim's style:**
- *h: left*
- *j: down*
- *k: up*
- *l: right*

| Shortcut | Action |
|--------|--------|
```mod + [h,j,k,l]``` | Move focus |
```mod + Shift + [h,j,k,l]``` | Move window in layout |
|```mod + Control + [h,j,k,l]```|Resize window (except in monadtall and monadwide)|
```mod + n```|Normalize window size|

## Applications and Utilities

| Shortcut | Action |
|--------|--------|
| ```mod + r``` | Launcher (Rofi Type-4) |
| ```mod + v``` | Clipboard history (Greenclip) |
```mod + Shift + v```|Clear clipboard|
```mod + b```|Open browser (Google Chrome)|
```mod + e```|File manager (Thunar)|
```mod + s```|Capture Screen (Flameshot)|

## Scratchpad (Pop-Up Menus)
| Shortcut | Action |
|--------|--------|
```mod + Shift + Enter``` | Quick Floating Terminal |
```mod + a``` | Volume Control (Pavucontrol) |
```mod + Shift + b```| Bluetooth Manager (Blueman) |
```mod + p```| Player (YouTube Music with Pear Desktop) |

## Bootloader
Any bootloader can be used, but the script is designed to configure Grub if it's installed, using the [Graphite GTK Theme GRUB](https://github.com/vinceliuice/Graphite-gtk-theme) theme.

## [Configuration](./SETTINGS.md)

## Components (Core)
- **WM**: Qtile (X11)
- **Terminal**: Kitty
- **Shell**: Fish Shell + Starship (Nerd-Font-Symbols preset)
- **Compositor**: Picom (Pijulius fork)
- **Clipboard**: Greenclip
- **Bar**: Custom Qtile Bar with dynamic network detection via network_finder.py.

- **Display Manager**: SDDM ([default SilentSDDM theme](https://github.com/uiriansan/SilentSDDM))

## Appearance
- **GTK Theme**: [Tokyonight](https://github.com/Fausto-Korpsvart/Tokyonight-GTK-Theme) (Dark, Moon, MacOS)
- **Icons**: [Papirus](https://github.com/PapirusDevelopmentTeam/papirus-icon-theme)
- **Cursor**: [Vimix White](https://github.com/vinceliuice/Vimix-cursors)
- **Font**: [FiraMono Nerd Font / Hack Nerd Font](https://www.nerdfonts.com/font-downloads)

## Additional Notes
1. **Root Shell**: To apply the Fish/Starship configuration to the root user, Run:
```bash
sudo ./setroot.sh
```
2. **SDDM**: The default session is configured for **Qtile (X11)**, preventing accidental login to unconfigured Wayland sessions (this doesn't work in Wayland).

3. **Icat**: To open images in Kitty, there's an alias configured in config.fish. Run ```kt``` to open images in Kitty.
```bash
# ~/.config/fish/config.fish
starship init fish | source
alias kt="kitten icat"
fastfetch --config os
```