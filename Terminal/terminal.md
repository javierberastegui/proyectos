#  Comandos interasantes terminal linux

------------

Vamos a crear una serie de alias que bajo mi punto de vista son necesarios para mi día a día, recuerda cambiar las rutas debido a que normalmente no compartiremos las mismas. 

------------

La edición del documento se realizará directamente desde el archivo vim .zshrc ejecutando el comando: 

> vim ~/.zshrc  

Una vez dentro nos irémos a la ultima linea y comentaremos algo como: 

> Alias linux

En la siguiente linea comenzaremos con las creación de los alias

------------

alias venv="source venv/bin/activate"
alias push="git push origin main"
alias pull="git pull origin main"
alias add="git add ."