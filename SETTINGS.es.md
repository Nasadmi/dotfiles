# Configuración y Rutas de Archivo

Este documento detalla la ubicación exacta de los archivos de configuración de cada software incluido en estos dotfiles. **Nota:** Todas las rutas son relativas al directorio ```$HOME```. Se recomienda el uso de ```code``` para editar estos archivos.

|Software|Ruta de configuración|Descripción|
|--------|---------------------|-----------|
|**Qtile**|```~/.config/qtile/config.py```|Configuración principal del gestor de ventanas.|
|**Kitty**|```~/.config/kitty/kitty.conf```|Ajustes de la terminal, fuentes y colores.|
|**Fish**|```~/.config/fish/config.fish```|Alias, funciones y configuración interactiva del shell.|
|**Picom**|```~/.config/picom/picom.conf```|Ajustes del compositor (opacidad, sombras, animaciones).|
|**Rofi**|```~/.config/rofi```|Directorio principal de lanzadores y menús de apagado.|
|**Dunst**|```~/.config/dunst/dunstrc```|Estilo y comportamiento de las notificaciones.|
|**Starship**|```~/.config/starship.toml```|Personalización del prompt para el shell.|
|**Greenclip**|```~/.config/greenclip.toml```|Ajustes del historial del portapapeles.|
|**GTK 3.0/4.0**|```~/.config/gtk-x.0/settings.ini```|Consistencia de temas, iconos y fuentes para apps GTK.|
|**GTK 2.0**|```~/.gtkrc-2.0```|Consistencia de temas, iconos y fuentes para apps que usen GTK 2.0.|

# Recuperación de Qtile (Backup)

Este archivo es una versión verificada y funcional de Qtile. Si tu config.py principal falla, sigue estos pasos para restaurar el sistema:

1. Crea un backup de tu configuración actual (dañada):

```bash
mv ~/.config/qtile/config.py ~/.config/qtile/config.py.bak
```

2. Sustitúyela por la versión por defecto:
```bash
cp ~/.config/qtile/default_config.py ~/.config/qtile/config.py
```

3. Reinicia Qtile: Presiona ```mod + Control + r``` (si la sesión sigue activa) o reinicia el gestor de sesiones (SDDM).

# Aplicaciones de arranque
## Systemd
- **bluetoothctl**: gestión de dispositivos bluetooth *(system-wide)*
- **sddm**: gestor de pantallas *(system-wide)*
- **greenclip**: historial de porpapeles *(a nivel de usuario)*
## Autostart
Qtile tiene un script ```autostart.sh``` que arranca elementos de la interfaz:
```bash
# ~/.config/qtile/autostart.sh
udiskie -t &
dunst &
picom --config $HOME/.config/picom/picom.conf &
feh --bg-scale $HOME/wallpapers/default.png &
```
- **Udiskie**: gestión de dispositivos de almacenamiento externo
- **Dunst**: sistema de notificaciones
- **Picom**: compositor
- **Feh**: gestor de fondos de pantalla

# Temas de Aplicaciones GTK
Se recomienda el uso de ```lxappearance``` para modificar **GTK-3.0**.
- Haga una copia para GTK-4.0
```bash
cp ~/.config/gtk-3.0/settings.ini ~/.config/gtk-4.0/settings.ini
```
- Para GTK-2.0 utilicé los mismos nombres, pero adaptándolo a la sintaxis (ejemplo):
```ini
; ~/.config/gtk-3.0/settings.ini
[Settings]
gtk-theme-name=Tokyonight-BL-MB-Dark-Dark-Moon
```
```bash
# ~/.gtkrc-2.0
gtk-theme-name="Tokyonight-BL-MB-Dark-Dark-Moon"
```
Para descargar e instalar nuevos temas (a nivel de usuario):
- Temas: copiar el tema dentro de ```~/.local/share/themes```
```bash
cp ~/Downloads/[Tema] ~/.local/share/themes
```
- Iconos:
    - Apartado de iconos de ```lxappearance```
    - Copiarlo a ```~/.local/share/icons```
- Cursores
    - Apartado de cursores de ```lxappearance```
    - Copiarlo a ```~/.local/share/icons```
- Fuentes locales
    - Copiarlo en ```~/.local/share/fonts```

Se recomienda el uso de la página [Pling](https://www.pling.com/browse?cat=148&ord=latest) para buscar temas, iconos y cursores.