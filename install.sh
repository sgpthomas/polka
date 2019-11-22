#!/usr/bin/zsh

function download() {
  rm -rf oh-my-zsh
  git clone https://github.com/sgpthomas/oh-my-zsh --recursive
  git clone https://github.com/zsh-users/zsh-syntax-highlighting.git oh-mh-zsh/plugins
  cp -r oh-my-zsh ~/.oh-my-zsh
}

function install() {
  ln -s zshrc ~/.zshrc  
  touch ~/.zshenv
  touch ~/.zshprojects
  touch ~/.zshalias
  touch ~/.zshlocal
}

download
install
source ~/.zshrc
