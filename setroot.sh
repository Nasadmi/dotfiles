#!/bin/bash

# Verificar si es root
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root (use sudo ./setroot.sh)"
  exit 1
fi

# Detectar el usuario real que lanzó el script
REAL_USER=${SUDO_USER:-$USER}
REAL_HOME=$(getent passwd "$REAL_USER" | cut -d: -f6)

echo "Configuring root shell to match $REAL_USER..."

# Crear carpeta .config para root si no existe
mkdir -p /root/.config

# Enlaces simbólicos usando rutas absolutas
ln -sf "$REAL_HOME/.config/starship.toml" /root/.config/starship.toml
ln -sf "$REAL_HOME/.config/fish" /root/.config/

# Cambiar el shell de root
chsh -s /usr/bin/fish root

echo "Root shell is now Fish and shares your config."