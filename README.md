## Calendario para Conky

### ¿Qué es Calendario para Conky?
Es un script para visualizar un calendario en Conky.

### ¿Cómo se instala?
Hay dos maneras de instalarlo, global y localmente.

#### Instalación global
Descargamos desde los repositorio _git_:   
`$ git clone https://github.com/PabliNet/calconky`

Para realizar la instalación global se necesita compilarlo, pero previamente instalamos el paquete de compilación _pyinstaller_:   
`$ pip3 install pyinstaller`

Compilamos:   
`$ pyinstaller -F calconky`

Nos posicionamos en el nuevo directorio _dist_:   
`$ cd dist`

Ejecutamos como _root_ o con privilegios de superusuario (anteponiemdo _sudo_):   
`# ./calconky -i`   
También se puede usar _--install_.

#### Instalación local
Para la instalación local hay que darle permisos de ejecución:   
`$ chmod +x shpkg`

Y lo ejecutamos:   
`$ ./shpkg -i`

### Modo de uso:
Si lo instalaste en modo local, en vez de escribir `${exec calconky}`, necesitarás escribir:   
`${exec python cal.py}`

Para visualizar los nombres de los día (Lu, Ma, Mi, Ju, Vi, Sa Do), tecleamos:   
`${exec calconky 0}`

Si queremos una sangría de 5 espacios:   
`${exec calconky 5 0}`   
`${exec calconky 5 1}`

También se puede agregar el nombre del mes y el año:   
`$alignc${exec calconky -my}`   
`${exec calconky 5 0}`   
`${exec calconky 5 1}`

Para más información:   
`$ calconky -h`
