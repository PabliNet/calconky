from os import chmod, getegid as uid, remove
from os.path import exists, split
from shutil import copy

def esroot(uid=uid()):
	if uid == 0:
		return True
	else:
		return False

def install(command):
	if command[-3:] != '.py':
		copy (_cmd(command), rute)
	else:
		print ('No se puede instalar, porque no está compilado')
		exit(-1)
	
def delete(command):
	if exists(rute + _cmd(command)):
		remove (rute + _cmd(command))
	else:
		print ('El paquetete no está instalado manualmente')
		exit(-1)

def _ifexist(command):
	tupla = (rute + command, rute[:5] + rute[11:] + command)
	lista = [False, False]
	for i in range(len(tupla)):
		if exists(tupla[i]):
			lista[i] = True
	return lista

def opciones(command, system=False, escmd=True):
	command = _cmd(command)
	if escmd:
		cat = 'el comando'
	else:
		cat = 'la aplicación'
	if not (_ifexist(command)[0] or _ifexist(command)[1]) and not system:
		mostrar = f'\n -i, --install\t- para instalar {cat}\n'
	elif _ifexist(command)[0] and not system:
		mostrar = f'\n -r, --remove\t- para desinstalar {cat}\n'
	elif _ifexist(command)[1] and system:
		mostrar = f'Tiene que desinstalar {cat} desde su gestor de paquetes'
	if 'mostrar' in locals():
		print (mostrar)

def _cmd(param):
	if param[-3:] == '.py':
		param = param.replace('.py', '')
	return split(param)[1]

rute = '/usr/local/bin/'

if __name__ == '__main__':
	pass