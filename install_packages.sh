#!/bin/bash

# Función para instalar yay
install_yay() {
  if ! command -v yay &> /dev/null; then
    echo "yay no está instalado. Instalando yay..."
    sudo pacman -S --noconfirm base-devel git
    git clone https://aur.archlinux.org/yay.git
    cd yay
    makepkg -si --noconfirm
    cd ..
    rm -rf yay
  else
    echo "yay ya está instalado."
  fi
}

# Llamar a la función para instalar yay si es necesario
install_yay

# Instalación de paquetes desde los repositorios oficiales
sudo pacman -S \
  alacritty \
  alsa-utils \
  base \
  base-devel \
  bat \
  brightnessctl \
  calc \
  efibootmgr \
  firefox \
  gedit \
  git \
  gparted \
  gst-plugin-pipewire \
  htop \
  intel-media-driver \
  intel-ucode \
  iwd \
  lib32-libglvnd \
  libpulse \
  libreoffice-fresh \
  libva-intel-driver \
  lightdm \
  lightdm-gtk-greeter \
  linux \
  linux-firmware \
  nano \
  neofetch \
  neovim \
  networkmanager \
  nitrogen \
  pavucontrol \
  picom \
  pulseaudio \
  pulseaudio-alsa \
  qtile \
  ranger \
  reflector \
  rofi \
  scrot \
  smartmontools \
  thunar \
  tree \
  ueberzug \
  unrar \
  unzip \
  variety \
  vim \
  w3m \
  wget \
  wireless_tools \
  wireplumber \
  wpa_supplicant \
  xdg-utils \
  xorg-server \
  xorg-xinit \
  zsh \
  zsh-autosuggestions \
  zsh-syntax-highlighting
