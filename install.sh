#!/usr/bin/env bash

function download() {
  git clone https://github.com/sgpthomas/oh-my-zsh
  cp -r oh-my-zsh ~/.oh-my-zsh
}

function install() {
  ln zshrc ~/.zshrc  
  touch ~/.zshenv
  touch ~/.zshprojects
}

download
install
