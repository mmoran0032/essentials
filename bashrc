# BASHRC for ARES2m (Linux Mint 17.1 64b)

# Making the prompt and terminal better
function truncate {
  newPWD="${PWD/#$HOME/~}"
  maxlen=35
  maxshow=32
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

export PATH=${PATH}:/usr/local/bin:/home/mikemoran/.local/bin
# for Miniconda...
# export PATH=/home/mikemoran/,miniconda/bin:$PATH
# for Swift
export PATH=${PATH}:/opt/swift-2.2/usr/bin

# sourcing
. ~/.aliases
eval "$(dircolors ~/.colors-ls)"
. /opt/root/bin/thisroot.sh

### Added by the Heroku Toolbelt
export PATH="/usr/local/heroku/bin:$PATH"
