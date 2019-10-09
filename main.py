#!/usr/bin/python3
# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*- 

# Written by Cristian Bottazzi
# 07/10/2019
# Description: A little sysadmin database tool to work with PostgreSQL
#

import os.path
import configparser
from func import checkSettingsFile

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


print (color.BOLD + color.YELLOW)
print("  ===========================================")
print("  |                                         |")
print("  |    SysAx => AXIA SysAdmin ToolKit       |")
print("  |   PostgreSQL Database Administration    |")
print("  |                                         |")
print("  ===========================================")
print(color.END)
print()

config = configparser.ConfigParser()
if checkSettingsFile():
	config.read('settings.dat')
else:
	print(color.RED + "Settings file not configured. Rename it to settings.dat" + color.END)
	quit()

def backupDatabase():
	print(color.CYAN)
	print("Avaiable configs:")
	print(config.sections())
	print(color.END)
	selection = input('Database selected: ')
	if selection in config.sections():
		print(color.GREEN + "executing...")
		cmd = 'pg_dump --dbname=postgresql://'+ config[selection]['username'] +':'+ config[selection]['password'] +'@'+ config[selection]['host'] +':'+config[selection]['port']+'/'+ config[selection]['database'] +' -F t > '+selection+'.tar'
		os.system(cmd)
		print("end.\n" + color.END)
	else:
		print(color.RED + "The database configuration doesn't exist on settings file\n\n" + color.END)

def exportTable():
	print(color.CYAN)
	print("Avaiable configs:")
	print(config.sections())
	source = input('SOURCE: ')
	if source not in config.sections():
		print(color.RED + "The database configuration doesn't exist on settings file\n\n" + color.END)
		return
	destination = input('DESTINATION: ')
	if destination not in config.sections():
		print(color.RED + "The database configuration doesn't exist on settings file\n\n" + color.END)
		return
	table = input('TABLE: ')
	print(color.GREEN + "executing...")
	cmd = 'pg_dump --dbname=postgresql://'+ config[source]['username'] +':'+ config[source]['password'] +'@'+ config[source]['host'] +':'+config[source]['port']+'/'+ config[source]['database'] + " -t " + table +' > '+table+'.sql'
	os.system(cmd)
	cmd = 'psql --dbname=postgresql://'+ config[destination]['username'] +':'+ config[destination]['password'] +'@'+ config[destination]['host'] +':'+config[destination]['port']+'/'+ config[destination]['database'] +' < '+table+'.sql'
	os.system(cmd)
	print(color.END)

def dumpAllDatabases():
	print(color.CYAN)
	print("Avaiable configs:")
	print(config.sections())
	source = input('DATABASE TO BACKUP: ')
	if source not in config.sections():
		print(color.RED + "The database configuration doesn't exist on settings file\n\n" + color.END)
		return
	destination = input('Save as: ')
	if not source:
		print(color.RED + "You have not provided a file name. Save as "+ source +"_DUMP.tar\n\n" + color.END)
		destination = source + "_DUMP"
		return

	print(color.GREEN + "executing...")
	cmd = "pg_dumpall --dbname=postgresql://"+ config[source]['username'] +':'+ config[source]['password'] +'@'+ config[source]['host'] +':'+config[source]['port'] + " > " + destination + ".sql"
	os.system(cmd)
	print("end." + color.END)

def restoreDatabase():
	print(color.CYAN)
	source = input('SOURCE FILE PATH: ')
	if not os.path.isfile(source):
		print(color.RED + "The backup file doesn't exist on the provided path\n\n" + color.END)
		return
	print("Avaiable configs:")
	print(config.sections())
	destination = input('RESTORE ON THE DATABASE: ')
	if destination not in config.sections():
		print(color.RED + "The database configuration doesn't exist on settings file\n\n" + color.END)
		return
	print(color.BOLD + color.RED + "ARE YOU REALLY SURE? THE DESTINATION DATABASE ("+ color.GREEN + destination + color.RED +") WILL BE ERASED" + color.END)
	print("If you're sure, type: " + color.YELLOW + color.BOLD + "yes, sure" + color.END)
	confirm = input('Are you sure?: ')
	if confirm != "yes, sure":
		return
	print(color.GREEN + "executing...")
	cmd = "pg_restore --dbname=postgresql://"+ config[destination]['username'] +':'+ config[destination]['password'] +'@'+ config[destination]['host'] +':'+config[destination]['port']+'/'+ config[destination]['database'] + " -c -1 < " + source
	os.system(cmd)
	print("end." + color.END)

menu = {}
menu['1']= color.GREEN + "Copy table" + color.END + " from " + color.RED + "prod" + color.END + " database to " + color.BLUE + "develop" + color.END + " database" 
menu['2']= color.GREEN + "Backup" + color.END + " database (to TAR file)"
menu['3']= color.GREEN + "Restore " + color.END + "database from backup (from TAR file)"
menu['4']= color.GREEN + "Backup ALL " + color.END + "databases from server"
menu['q']= color.YELLOW + "Exit" + color.END

while True:
	options=menu.keys()
	options = sorted(options)
	print(color.BOLD + "-------------------  MENU  ------------------------" + color.END)
	for entry in options:
		print(entry, menu[entry])
	print("-------------------  END  -------------------------")

	selection = input("Please Select: ")
	if selection =='1':
		exportTable()
	elif selection == '2':
		backupDatabase()
	elif selection == '3':
		restoreDatabase()
	elif selection == '4':
		dumpAllDatabases()
	elif selection == 'q':
		break
	else: 
		print("Unknown Option Selected!")