#!/usr/bin/env bash

function download() {
  rm -rf oh-my-zsh
  git clone https://github.com/sgpthomas/oh-my-zsh --recursive
  cp -r oh-my-zsh ~/.oh-my-zsh
}

function install() {
  ln zshrc ~/.zshrc  
  touch ~/.zshenv
  touch ~/.zshprojects
  touch ~/.zshalias
  touch ~/.zshlocal
}

download
install
source ~/.zshrc
