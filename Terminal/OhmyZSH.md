sudo apt update && sudo apt dist-upgrade -y
sudo apt install zsh
zsh --version
sudo chsh -s $(which zsh)
zsh
instalar las letras
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
vim ~/.zshrc
ZSH_THEME="powerlevel10k/powerlevel10k"
