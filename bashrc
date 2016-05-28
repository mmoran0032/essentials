# BASHRC for ARES2m (Linux Mint 17.3 64b)

# Making the prompt and terminal better
function truncate {
  newPWD="${PWD/#$HOME/~}"
  maxlen=30
  maxshow=27
  if [ ${#newPWD} -gt $maxlen ]; then
    newPWD="...${newPWD: -$maxshow}"
  fi
}

PROMPT_COMMAND=truncate
export PS1="\[\033[1;32m\][\[\033[1;30m\]\u@\h\[\033[m\] \[\033[1;31m\]\${newPWD}\[\033[1;32m\]]\[\033[m\] "

# making sure vim works well
export EDITOR=/usr/bin/vim
if [ -n "$DISPLAY" -a "$TERM" == "xterm" ]; then
  export TERM=xterm-256color
fi

# Adjusting bash_history to be more helpful
export HISTIGNORE="&:[ ]*:exit:hide"
export HISTTIMEFORMAT="%Y-%m-%d %H:%M: "
export HISTSIZE=2500

export PATH=/opt/miniconda3/bin:${PATH}:/home/mikemoran/.local/bin

# sourcing
. ~/.aliases
eval "$(dircolors ~/.colors-ls)"
#. /opt/root6/bin/thisroot.sh
#export PYTHONPATH=${PYTHONPATH}:${ROOTSYS}/bindings/pyroot/

