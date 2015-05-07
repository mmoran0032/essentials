execute pathogen#infect()

set nocompatible
set number
set cursorline
set mouse=a

set syntax=on
filetype on

"Removes trailing whitespace from entire file
command Rtw %s/\s\+$//e

set ignorecase smartcase
set hlsearch

"For Python specifically
set tabstop=2
set shiftwidth=2
"Folding, with za
set foldmethod=indent
set foldlevel=99

au BufRead,BufNewFile *.md set filetype=markdown

set expandtab
autocmd FileType make setlocal noexpandtab
set backup
set backupdir=~/.vim/backup/
set directory=~/.vim/backup/

set background=dark
colorscheme distinguished
set laststatus=2
set noshowmode

" Settings for airline
let g:bufferline_echo=0
let g:airline_powerline_fonts=1
set ttimeoutlen=50
autocmd VimEnter *
\ let &statusline='%{bufferline#refresh_status()}' . bufferline#get_status_string()

let g:airline_powerline_fonts=0
let g:airline_theme='powerlineish'
"let g:airline#extensions#tabline#enabled=1
let g:airline_left_sep=''
let g:airline_right_sep=''

