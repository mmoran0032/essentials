# BASHRC for ARES2m (Linux Mint 17.1 64b)

function truncate {
  newPWD="${PWD/#$HOME/~}"
  maxlen=40
  maxshow=37
  if [ ${#newPWD} -gt $maxlen ]; then
    newPWD="...${newPWD: -$maxshow}"
  fi
}

PROMPT_COMMAND=truncate
export PS1="\[\033[1;30m\]\!(\#)\[\033[m\] \[\033[1;31m\]\${newPWD} >\[\033[m\] "
eval "$(dircolors ~/.colors-ls)"

export EDITOR=/usr/bin/vim
if [ -n "$DISPLAY" -a "$TERM" == "xterm" ]
then
  export TERM=xterm-256color
fi

# Adjusting bash_history to be more helpful
export HISTIGNORE="&:[ ]*:exit:hide"
export HISTTIMEFORMAT="%Y-%m-%d %H:%M: "
export HISTSIZE=5000


PATH=${PATH}:/home/mikemoran/bin
PATH=${PATH}:/usr/local/bin
PATH=${PATH}:/home/mikemoran/.local/bin
export PATH

. ~/.aliases

# Runs history saving script when in an interactive shell
# history file saved to ~/.python_history
# DOESN'T WORK - readline module not found for some reason...
#export PYTHONSTARTUP=/home/mikemoran/bin/python/PYSTART.py

####
# Saving these, but I am going to start from scratch to make sure I am not
# just being an idiot with these. Also, python will automatically look in
# ~/.local, so I shouldn't need to worry about it, but I also don't know
# what will happen with multiple versions. Honestly, I don't know about
# anything anymore in terms of installing this stuff
####

# Sets up path variables for use with ROOT and PyROOT
#ROOTSYS=/usr/local
#export LD_LIBRARY_PATH=/home/mikemoran/.local:${ROOTSYS}/lib/root:${LD_LIBRARY_PATH}
#export PYTHONPATH=/home/mikemoran/.local:${ROOTSYS}/lib/root:/usr/local/lib:/usr/lib
#export PYTHONPATH=${PYTHONPATH}:/opt/pandas-0.16.0:/usr/lib/python2.7/dist-packages
# for rpy2 -- remove if it doesn't work again...
#export PYTHONPATH=${PYTHONPATH}:/usr/local/lib/python2.7/dist-packages
