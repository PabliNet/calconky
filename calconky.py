#!/usr/bin/python3
from os import getenv
from sys import argv, exit, path
from datetime import date
from locale import LC_ALL, setlocale
from calendar import monthcalendar
from pyquete import delete, esroot, install, opciones

def error(opcion):
	l = (
		'Opción no válida',
		'Demasiados argumentos',
		'Se necesita ser superusuario o root'
	)
	if opcion == -1:
		opcion = len(l)
	print (f'ERROR: {l[opcion-1]}.')
	return opcion

def eshoy (dia, hoy=(date.today().strftime('%Y-%m-%d')).split('-')[2]):
	if dia == int(hoy):
		return '[', ']'
	else:
		return '\u0020', '\u0020'

def strDia (dia, hoy=date.today().strftime('%d')):
	if dia == 0:
		return '\u0020' + '\u00B7' * 2 + '\u0020'
	elif dia < 10:
		return eshoy(dia)[0] + '\u00B7' + str(dia) + eshoy(dia)[1]
	else:
		return eshoy(dia)[0] + str(dia) + eshoy(dia)[1]

if len(argv) == 1:
	argv.extend(['0', '1'])

if argv[1] in ('-i', '--install', '-r', '--remove'):
	if esroot() and len(argv) == 2:
		if argv[1] in ('-i', '--install'):
			install(argv[0])
		elif argv[1] in ('-r', '--remove'):
			delete(argv[0])
		exit()
	elif not esroot():
		exit(error(-1))

if len(argv) == 2 and not argv[1].isdigit():
	if argv[1] in ('-m', '-my', '-ym'):
		setlocale(LC_ALL, '')
		mes = date.today().strftime('%B %Y').capitalize()
		if argv[1] == '-ym':
			mes = mes.split(' ')
			mes.reverse()
			mes = ' '.join(mes)
		elif argv[1] == '-m':
			mes = mes.split(' ')[0]
		print (mes)
	elif argv[1] in ('-h', '--help'):
		print ('Modo de empleo:', f'{argv[0]} [SANGRÍA] 0', f'{argv[0]} [SANGRÍA] 1', f'{argv[0]} [OPCIÓN]', '\n   0: nombre de los días\n   1: las semanas', sep='\n ')
		print ('\nVisualiza con calendario para Conky\n')
		print (f'Opciones:', '-m\t\t- mes', '-my\t\t- mes año', '-ym\t\t- año mes\n', '-h, --help\t- muestra esta ayuda y finaliza', '-v, --version\t- informa de la versión y finaliza\n', sep='\n ')
		opciones(argv[0])
		opciones(argv[0], True)
		print('\nSugerencia:', '    Si desea sin sangría, teclee:', f'\t{argv[0]} 0', f'\t{argv[0]}', sep='\n')
	elif argv[1] in ('-v', '--version'):
		print (f'{argv[0]} 1.0.2','Copyright © 2021\n', 'Desarrollado por Pablo Alejandro Carravetti', sep='\n')
	else:
		exit(error(1))
	exit()
elif len(argv) == 2 and argv[1].isdigit() and argv[1] == '0':
	argv.append('0')
elif len(argv) == 2 and argv[1].isdigit() and argv[1] != '0':
	argv.append('1')
elif len(argv) == 3 and not (argv[1].isdigit() and argv[2] in ('0', '1')):
	exit(error(1))
elif len(argv) > 3:
	exit(error(2))

argv[2] = bool(int(argv[2]))

dato = tuple((date.today().strftime('%Y-%m')).split('-'))

strMes = [['\u0020Lu\u0020', '\u0020Ma\u0020', '\u0020Mi\u0020', '\u0020Ju\u0020', '\u0020Vi\u0020', '\u0020Sa\u0020', '\u0020Do\u0020']]
for semana in monthcalendar(int(dato[0]), int(dato[1])):
	strSemana = []
	for nDia in semana:
		strSemana.append(strDia(nDia))
	strMes.append(strSemana)
del (nDia, strSemana)

if not argv[2]:
	a, b = 0, 1
else:
	a, b = 1, len(strMes)

for semana in strMes[a:b]:
	print (int(argv[1]) * ' ' + ''.join(semana))