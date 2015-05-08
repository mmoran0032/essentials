# BASHRC for ARES2m (Linux Mint 17.1 64b)

# Making the prompt and terminal better
function truncate {
  newPWD="${PWD/#$HOME/~}"
  maxlen=40
  maxshow=37
  if [ ${#newPWD} -gt $maxlen ]; then
    newPWD="...${newPWD: -$maxshow}"
  fi
}

PROMPT_COMMAND=truncate
export PS1="\[\033[1;32m\][\[\033[1;30m\]\u@\h\[\033[m\] \[\033[1;31m\]\${newPWD}\[\033[1;32m\]]\[\033[m\] "
eval "$(dircolors ~/.colors-ls)"

# making sure vim works well
export EDITOR=/usr/bin/vim
if [ -n "$DISPLAY" -a "$TERM" == "xterm" ]; then
  export TERM=xterm-256color
fi

# Adjusting bash_history to be more helpful
export HISTIGNORE="&:[ ]*:exit:hide"
export HISTTIMEFORMAT="%Y-%m-%d %H:%M: "
export HISTSIZE=5000

export PATH=${PATH}:/usr/local/bin:/home/mikemoran/.local/bin

. ~/.aliases
