#!/usr/bin/python3

#---------------------------------------
# Script de gerenciamento de usuários.
# Autor: Leonardo Migot.
# Data: Jun/2016
#
# Funções:
# 	Exibe usuários/grupos existentes.
# 	Lista usuários de cada grupo.
# 	Adiciona novos usuários/grupos.
# 	Remove usuários/grupos.
#	Altera propriedades de usuários/grupos.
# 	
# 	Deve ser executado como 'Root'.
#---------------------------------------

def ifRoot():

	if not os.getenv("USER") == 'root':
		print(u"Você não é o administrador!.")
		exit(1)

def getKey(item):

	return item[0]

################
### USUÁRIOS ###
################

def lsUser(address):

	idMin = int(sys.argv[1]) 
	idMax = int(sys.argv[2])

	file = open(address, "r")
	pair = []

	for string in file.readlines():

		temp = int(string.split(":")[2]), string.split(":")[3], string.split(":")[0]
		pair.append(temp)

	pair.sort(key=getKey)

	for i in pair:

		if i[0] >= idMin and i[0] <= idMax:
			print(i[0], "\t", i[1], "\t", i[2])

	file.close()

def adduser():

	name = input(u"Nome do usuário: ")
	uid = input(u"UID do usuário: ")
	group = input("Nome do grupo: ")

	home = "/home/" + name
	os.system("useradd -m -d " + home + " -s /bin/bash " + " -G " + group + " -u " + str(uid) + " " + name)

def removeuser():

	name = input(u"Nome do usuário: ")

	os.system("userdel " + name)

def edituser():

	nomeusr = input(u"Nome do usuário: ")
		
	print(	u"1 - Adicionar á algum grupo.\n"
		u"2 - Mudar nome.\n"
		u"3 - Bloquear senha.\n"
		u"4 - Desbloquear senha.\n"
		u"5 - Data de expiração.\n"
		u"6 - Alterar UID.\n" )

	op2 = int(input(">> "))

	if op2 == 1:

		parameter = input("Nome do grupo: ")
		os.system("usermod -G " + parameter + " " + nomeusr)

	elif op2 == 2:

		parameter = input("Novo nome (login): ")
		os.system("usermod -l " + parameter + " " + nomeusr)

	elif op2 == 3:

		os.system("usermod -L " + nomeusr)

	elif op2 == 4:

		os.system("usermod -U " + nomeusr)

	elif op2 == 5:

		ano = input(u"Ano de expiração: ")
		mes = input(u"Mês de expiração: ")
		dia = input(u"Dia de expiração: ")

		os.system("usermod -e " + ano + "-" + mes + "-" + dia + " " + nomeusr)

	elif op2 == 6:

		parameter = input("Novo UID: ")
		os.system("usermod -u " + parameter + " " + nomeusr)

##############
### GRUPOS ###
##############

def lsGroup(address):

	idMin = int(sys.argv[3]) 
	idMax = int(sys.argv[4])


	file = open(address, "r")
	pair = []

	for string in file.readlines():

		temp = int(string.split(":")[2]), string.split(":")[0]
		pair.append(temp)

	pair.sort(key=getKey)

	for i in pair:

		if i[0] >= idMin and i[0] <= idMax:
			print(i[0], "\t", i[1])

	file.close()

def groupUsers(address):

	name = input("Nome do grupo: ")

	file = open(address, "r")

	pair = []

	for string in file.readlines():

		temp = int(string.split(":")[2]), string.split(":")
		pair.append(temp)

	pair.sort(key=getKey)

	for i in pair:

		if i[1][0] == name:
			print(i[1][3])

	file.close()

def addgroup():

	name = input("Nome do grupo: ")
	gid = input("GID do grupo: ")

	os.system("groupadd -g " + str(gid) + " " + name)

def removegroup():

	name = input("Nome do grupo: ")

	os.system("groupdel "+ name)

def editgroup():

	name = input("Nome do grupo: ")
	new = input("Novo nome do grupo: ")
	gid = input("Novo GID do grupo: ")

	os.system("groupmod -g" + str(gid) + " -n " + new + " " + name)

##############
###  MAIN  ###
##############

import os
import sys

user_f = "/etc/passwd"
group_f = "/etc/group"

ifRoot()

while True:
	print( 	u"Escolha um opção:\n"

			#Usuários
			u"1 - Listar todos usuários.\n"
			u"2 - Adicionar um usuário.\n"
			u"3 - Remover um usuário.\n"
			u"4 - Editar usuário.\n"

			#Grupos
			u"5 - Listar todos grupos.\n"
			u"6 - Listar usuários por grupo.\n"
			u"7 - Adicionar um grupo.\n"
			u"8 - Remover um grupo.\n"
			u"9 - Editar um grupo (GID e nome).\n"
			u"0 - SAIR.\n" )

	opcao = int(input("> "))

	if opcao == 0:

		exit(0)

	elif opcao == 1:

		lsUser(user_f)

	elif opcao == 2:

		adduser()

	elif opcao == 3:

		removeuser()

	elif opcao == 4:

		edituser()

	elif opcao == 5:

		lsGroup(group_f)

	elif opcao == 6:

		groupUsers(group_f)

	elif opcao == 7:

		addgroup()

	elif opcao == 8:

		removegroup()

	elif opcao == 9:

		editgroup()

	pause = input("Tecle enter...")
	os.system("clear")

#############
###  FIM  ###
#############