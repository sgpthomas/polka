set expandtab
set tabstop=2
set softtabstop=2
set shiftwidth=2

call plug#begin('~/.local/share/nvim/plugged')

" dahlia vim highlighting
Plug '~/Cornell/research/dahlia/tools/vim'
Plug 'tpope/vim-surround'

" theme
Plug 'lifepillar/vim-solarized8'
Plug 'liuchengxu/space-vim-dark'

call plug#end()

" set theme to solarized
colorscheme space-vim-dark
set termguicolors
hi LineNr ctermbg=NONE guibg=NONE
hi Comment guifg=#5C6370 ctermfg=59
