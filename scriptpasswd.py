#!/usr/bin/python

fd = open('/etc/passwd','r')
lista = fd.readlines()

for linea in lista:
	lista2 = linea.split(':')
	print "usuario:", lista2[0], "shell", lista2[len(lista2) -1]