#!/usr/bin/python

fd = open('/etc/passwd','r')
lista = fd.readlines()
dicc = {}

for linea in lista:
	lista2 = linea.split(':')
	
	#print "usuario:", lista2[0], "shell", lista2[len(lista2) -1]
	dicc[lista2[0]] = lista2[-1][:-1] # Para quitarme el \n 

print dicc["root"]
print len(dicc)

try:
	print dicc["imaginario"]
except KeyError:
	print "Usuario imaginario no existe"