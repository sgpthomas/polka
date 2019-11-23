# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH="/home/samthomas/.oh-my-zsh"

# theme name
ZSH_THEME="sammythomas"

# plugins
plugins=(
  git-prompt-custom
  colored-man-pages
  better-vim
  up-dir
  zsh-syntax-highlighting
)

# oh my zsh stuff
source $ZSH/oh-my-zsh.sh

# User configuration
####### Alias #######
source ~/.zshalias
####### Alias #######

highlight () {
  grep -E "$1|$"
}

loop() {
  while [ 1 = 1 ]; do
    echo "--------------"
    "$@"
  done
}

function remake() {
  rm -f $1
  make $1
}

# clear screen thing
clear-screen() { echoti clear; zle redisplay; }
zle -N clear-screen

###### custom project commands setup ######
source ~/.zshprojects
function mkproj() {
  if [ ! -z $1 ]; then
    echo "hash -d $1=$PWD" >> ~/.zshprojects
    source ~/.zshprojects
  else;
    echo "Need name!"
  fi
}

### local zsh stuff
source ~/.zshlocal
