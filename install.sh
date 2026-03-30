#!/bin/bash

# --- 1. Verificaciones Base ---
if pacman -Qg base-devel > /dev/null 2>&1; then
    echo -e "\e[32m[OK]\e[0m base-devel already exists."
else
    echo -e "\e[33m[!]\e[0m Installing base-devel..."
    sudo pacman -S --noconfirm base-devel
fi

if command -v git > /dev/null 2>&1; then
    echo -e "\e[32m[OK]\e[0m git is already installed."
else
    echo -e "\e[33m[!]\e[0m Installing git..."
    sudo pacman -S --noconfirm git
fi

# --- 2. Grub Theming ---
if [ -d "/boot/grub" ]; then
    echo -e "\e[32m[OK]\e[0m GRUB Detected. Installing theme..."
    git clone https://github.com/vinceliuice/Graphite-gtk-theme
    cd Graphite-gtk-theme/other/grub2/ && sudo ./install.sh
    cd ../../../
    rm -rf Graphite-gtk-theme
else
    echo -e "\e[31m[!]\e[0m Skipping GRUB bootloader settings"
fi

# --- 3. Yay Installation ---
if ! command -v yay > /dev/null 2>&1; then
    echo -e "\033[0;33mInstalling yay...\033[0m"
    git clone https://aur.archlinux.org/yay.git
    cd yay && makepkg -si --noconfirm && cd ..
    rm -rf yay
fi

# --- 4. Package Installation ---
echo -e "\033[1;33mInstalling packages...\033[0m"
sudo pacman -S --noconfirm qtile kitty python-pip rofi stow sddm dunst starship \
    ttf-hack-nerd otf-firamono-nerd fish pulseaudio pulseaudio-alsa \
    pulseaudio-bluetooth pulseaudio-jack alsa-utils pavucontrol xclip \
    xorg-xinit vlc gvfs ntfs-3g udiskie thunar flameshot bluez bluez-utils \
    blueman fastfetch btop ranger unzip qt6-base qt6-svg lxappearance feh

yay -S --noconfirm picom-pijulius-next-git google-chrome pear-desktop rofi-greenclip

# Python libraries for Qtile
pip install --break-system-packages psutil dbus-fast pulsectl_asyncio

# --- 5. SDDM Theme ---
git clone -b main --depth=1 https://github.com/uiriansan/SilentSDDM
cd SilentSDDM && sudo ./install.sh && cd ..
rm -rf SilentSDDM
sudo mkdir -p /etc/sddm.conf.d
echo -e "[Autologin]\nSession=qtile.desktop\nUser=$USER\n\n[General]\nDisplayServer=x11" | sudo tee /etc/sddm.conf.d/10-session.conf

sudo systemctl enable sddm.service
sudo systemctl enable bluetooth.service

# --- 6. Local Assets (Icons, Themes, Cursors) ---
mkdir -p ~/.local/share/icons ~/.local/share/themes

# Papirus Icons
git clone https://github.com/PapirusDevelopmentTeam/papirus-icon-theme
cd papirus-icon-theme
cp -r Papirus-Dark Papirus-Light Papirus ~/.local/share/icons/
cd .. && rm -rf papirus-icon-theme

# Vimix Cursors
git clone https://github.com/vinceliuice/Vimix-cursors
cd Vimix-cursors
./install.sh # El instalador oficial es mejor que copiar a mano
cd .. && rm -rf Vimix-cursors

# Tokyonight GTK Theme
if git clone https://github.com/Fausto-Korpsvart/Tokyonight-GTK-Theme; then
    cd Tokyonight-GTK-Theme
    chmod +x ./themes/install.sh
    ./themes/install.sh -d ~/.local/share/themes -n Tokyonight-BL-MB-Dark -c dark --tweaks moon macos
    cd ..
    rm -rf Tokyonight-GTK-Theme
fi

# Fastfetch presets
cd ~/.local/share
git clone https://github.com/LierB/fastfetch

# --- 7. Final Configuration & Stow ---
echo -e "\033[0;36mAplying settings from dotfiles...\033[0m"

# Asegurar que estamos en el directorio correcto de dotfiles
cd ~/dotfiles

# Permisos de ejecución
chmod +x .config/rofi/launchers/type-4/launcher.sh
chmod +x .config/rofi/launchers/type-1/launcher.sh
chmod +x .config/qtile/autostart.sh

# Cambiar shell
if [ "$SHELL" != "/usr/bin/fish" ]; then
    echo -e "Change default shell..."
    sudo chsh -s /usr/bin/fish $USER
fi

# Stow (el punto indica el directorio actual)
stow .

# Greenclip User Service
systemctl --user enable --now greenclip.service

echo -e "\033[0;32m\033[0m"

echo -e "To change the root shell execute ./setroot.sh with root priviliges"
echo -e "\033[0;32mDONE! Reboot system\033[0m"