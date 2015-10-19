#!/usr/bin/python
#-*-coding: UTF-8-*-

'''
 CUPP - Common User Passwords Profiler
 
 Adaptation by No Web at Home

 nowebathome AT gmail DOT com
 http://www.cybrary.it/members/nowebathome
 http://creator.wonderhowto.com/nowebathome/
 
 CUPP author:

 Muris Kurgas aka j0rgan
 j0rgan [at] remote-exploit [dot] org
 http://www.remote-exploit.org
 http://www.azuzi.me

 LICENSE

 This program is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation; either version 3 of the License, or
 any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program; if not, write to the Free Software
 Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

 See 'docs/LICENSE' for more information.
'''

import sys
import os
import ConfigParser

# FUNCTIONS

# My functions

# Returns true if the string only contains 8 numbers.
def is_date(string):
	if string[2:4]>"12" or string[2:4]=="00":
		return False
	l=list(string)
	x=0
	if l[2:4]>"12" or l[2:4]=="00":
		return False
	if len(string) != 0 and len(string) != 8:
		return False;
	while x < len(l):
		if l[x] not in '0123456789':
			return False
		x+=1
	return True

		
# Returns true if the list only contains items with 8 numbers.
def are_dates(l):
	x=0
	while x < len(l):
		print l[x]
		if is_date(l[x]) != True:
				return False
		x+=1
	return True
	
# Returns the date with the month as text
def text_month(date):
	x=int(date[2:4])
	months=['January', 'February', 'March', 'April', 'May', 'June',
	'July', 'August', 'September', 'October', 'November', 'December']
	return date[0:2]+months[x-1]+date[4:]
	
# Returns the word with uppercase first letter
def up(word):
	return word.title()

# Returns the list with each word with uppercase first letter
def up_list(l):
	x=[]
	for i in l:
		x.append(i.title())
	return x

# Returns the word reversed
def reverse(word):
	return word[::-1]

# Returns the list with each item reversed 	
def reverse_list(l):
	x=[]
	for i in l:
		x.append(reverse(i))
	return x

# Author functions

# concatenating
def concats(seq, start, stop):
	for mystr in seq:
		for num in xrange(start, stop):
			yield mystr + str(num)


# sorting and combinating
def komb(seq, start):
	for mystr in seq:
		for mystr1 in start:
			yield mystr + mystr1


# CONFIGURATION FILE

# Reading the configuration file

config = ConfigParser.ConfigParser()
config.read('cupp.cfg')

years = config.get('years', 'years').split(',')
chars = config.get('specialchars', 'chars').split(',')

numfrom = config.getint('nums','from')
numto = config.getint('nums','to')

wcfrom = config.getint('nums','wcfrom')
wcto = config.getint('nums','wcto')

# Leet mode configurations

a = config.get('leet','a')
i = config.get('leet','i')
e = config.get('leet','e')
t = config.get('leet','t')
o = config.get('leet','o')
s = config.get('leet','s')
g = config.get('leet','g')
z = config.get('leet','z')


# ARGUMENTS

if len(sys.argv) < 2 or sys.argv[1] == '-h' or sys.argv[1]== '--help':
	print "Usage: python cupp.py <options>"
	print "[ Options ]\n"
	print "-h, --help:	Help"
	print "	Under construction."
	print "	Glogal configuration file is cupp.cfg\n"	

	print "-i:	Interactive mode for dictionary building\n"

	print "-v, --version: Print the version of the program\n"
	exit()

elif sys.argv[1] == '-v' or sys.argv[1]=='--version':
	print ''' CUPP - Common User Passwords Profiler.
 
 Adaptation for study purposes by No Web at Home.

 Version 0.1

 September 2015

 nowebathome AT gmail DOT com
 http://www.cybrary.it/members/nowebathome
 http://creator.wonderhowto.com/nowebathome/
 
 Join me at project "elpscrk.py"'''
	exit()

elif sys.argv[1] == '-i':
	print "\r\n[+] Insert information about your target. "
	print "[+] If you don't know the answer, just press enter to skip.\r\n"

# INPUT

# Colecting informations
name = raw_input("[*] First name: ").lower()
while len(name) == 0 or name == " " or name == "  " or name == "   ":
	print "[-] A man needs a name! "
	name = raw_input("[*] First name: ").lower()
name = str(name)

surname = raw_input("[*] Surname: ").lower()

nick = raw_input("[*] Nickname: ").lower()

birthdate = (raw_input("[*] Birthdate (DDMMYYYY): "))
while len(birthdate) != 0 and len(birthdate) !=8or is_date(birthdate)!=True: 
	print "[-] Insert a valid format!"
	birthdate = raw_input("[*] Birthdate (DDMMYYYY): ")
birthdate = str(birthdate)

partner_name= raw_input("[*] Partner's name: ").lower()

partner_nick= raw_input("[*] Partner's nickname: ").lower()

partner_birthdate = raw_input("[*] Partner's birthdate (DDMMYYYY): ")
while is_date(partner_birthdate)!=True:
	print "[-] Insert a valid format!"
	partner_birthdate = raw_input("[*] Partner's birthdate (DDMMYYYY): ")
partner_birthdate = str(partner_birthdate)

extras = raw_input("[*] Important persons: ").replace(" ","")
extras = extras.lower()
extras = extras.split(',')

extras_nick = raw_input("[*] Nickname of them: ").replace(" ","")
extras_nick = extras_nick.lower()
extras_nick = extras_nick.split(',')

extras_birthdate = raw_input("[*] Important dates (DDMMYYYY): ").replace(" ","")
extras_birthdate = extras_birthdate.split(',')
while are_dates(extras_birthdate)!= True:
	print "[-] Insert a valid format for each date!"
	extras_birthdate = raw_input("[*] Important dates (DDMMYYYY): ").replace(" ","")
	extras_birthdate = extras_birthdate.split(',')

pet = raw_input("[*] Pet's name: ").lower()

answer = raw_input("[?] Add any keyword about the target? Y/N: ").lower()
if answer == "y":
	key_words = raw_input("[*] Insert the key words: ").replace(" ","")
	key_words = key_words.split(",")

spec_chars=[]
answer = raw_input("[?] Add special chars at the end of words? Y/N: ").lower()
if answer == "y":
	for i in chars:
		spec_chars.append(i)
		for j in chars:
			spec_chars.append(i+j)
			for k in chars:
				spec_chars.append(i+j+k)

random_num = raw_input("[?] Add random numbers at the end of words? Y/N ").lower()
leet_mode = raw_input("[?] Activate leet mode? (i.e. leet = 1337) Y/N:").lower()

print "\n[+] Creating dictionary..."

# String manipulation

# Birthdates

# Target's 
birthdate_yy = birthdate[-2:]
birthdate_yyyy = birthdate[-4:]
birthdate_dd = birthdate[:2]
birthdate_mm = birthdate[2:4]
birthdate_ddmm = birthdate[:4]
birthdate_text=text_month(birthdate)

# Partner's 
partner_birthdate_yy = partner_birthdate[-2:]
partner_birthdate_yyyy = partner_birthdate[-4:]
partner_birthdate_dd = partner_birthdate[:2]
partner_birthdate_mm = partner_birthdate[2:4]
partner_birthdate_ddmm = partner_birthdate[:4]
partner_birthdate_text=text_month(partner_birthdate)

# Mixed
birthdate_comb1 = birthdate_dd + partner_birthdate_dd
birthdate_comb2 = partner_birthdate_dd + birthdate_dd
birthdate_comb3 = birthdate_dd + partner_birthdate_mm
birthdate_comb3 = partner_birthdate_dd + birthdate_mm
birthdate_comb4 = birthdate_dd + partner_birthdate_text[2:-4]
birthdate_comb5 = partner_birthdate_dd + birthdate_text[2:-4]

# Upper case first letter
name_up = up(name)
surname_up = up(name)
nick_up = up(nick)
partner_name_up = up(partner_name)
partner_nick_up = up(partner_nick)
pet_up = up(pet)
extras_up = up_list(extras)


#I didn't get the point of this
'''
up_words = []
for i in words:
	up_words.append(up(i))
word = words+up_words
'''

# Names modification
name_reverse = reverse(name)
name_reverse_up = up(name_reverse)
nick_reverse = reverse(nick)
nick_reverse_up = up(nick_reverse)
partner_name_reverse = reverse(partner_name)
partner_name_reverse_up = up(partner_name_reverse)
partner_nick_reverse = reverse(partner_nick)
parter_nick_reverse_up = up(partner_nick_reverse)
extras_reverse = reverse_list(extras)
extras_reverse_up = up_list(extras_reverse)

# To guess Tiago's password
# double_nick = nick+reverse_nick
# double_nick_dot = nick+'.'+reverse_nick

reverse = [name_reverse, name_reverse_up, nick_reverse, nick_reverse_up, partner_name_reverse,
partner_name_reverse_up] + extras
rev_n = [name_reverse, name_reverse_up, nick_reverse, nick_reverse_up]
rev_w = [partner_name_reverse, partner_name_reverse_up]
rev_k = extras_reverse+extras_reverse_up

''' Need to check if the lists are coming as strings to prevent sum them instead of concatenating'''
# Let's do some serious work! This will be a mess of code, but... who cares? :) 

# Birthdays combinations

#Target's
bds = []
for i in birthdates:
	bds.append(i)
	for j in birthdates:
		if birthdates.index(i) != birthdates.index(j):
			bds.append(i+j)
			for k in birthdates:
				if birthdates.index(i) != birthdates.index(j) and birthdates.index(j) != birthdates.index(k) and birthdates.index(i) != birthdates.index(k):
					bds.append(i+j+k)

# Partner's
partner_birthdates = [partner_birthdate_yy, partner_birthdate_yyyy, partner_birthdate_dd, partner_birthdate_mm]
pbds = []
for i in partner_birthdates:
	pbds.append(i)
	for j in partner_birthdates:
		if partner_birthdates(i) != partner_birthdates.index(j):
			pbds.append(i+j)
			for k in partner_birthdates:
				if partner_birthdates.index(i) != partner_birthdates(j) and partner_birthdates.index(j) != partner_birthdates(k) and partner_birthdates.index(i) != partner_birthdates.index(k):
					pbds.append(i+j+k)


'''
# Important persons' --- I take a list here so I'check that later

kbds = [kidb_yy, kidb_yyy, kidb_yyyy, kidb_xd, kidb_xm, kidb_dd, kidb_mm]

kbdss = []

for kbds1 in kbds:
	kbdss.append(kbds1)
	for kbds2 in kbds:
		if kbds.index(kbds1) != kbds.index(kbds2):
			kbdss.append(kbds1+kbds2)
			for kbds3 in kbds:
				if kbds.index(kbds1) != kbds.index(kbds2) and kbds.index(kbds2) != kbds.index(kbds3) and kbds.index(kbds1) != kbds.index(kbds3):
					kbdss.append(kbds1+kbds2+kbds3)
'''


# string combinations....

kombinaac = [pet, pet_up]

kombina = [name, surname, nick, name_up, surname, surname_up]

kombinaw = [partner_name, partner_name_up, surname, surname_up]


[name, surname, nick, nameup, surnameup, nickup]


kombinaa = []
for kombina1 in kombina:
	kombinaa.append(kombina1)
	for kombina2 in kombina:
		if kombina.index(kombina1) != kombina.index(kombina2) and kombina.index(kombina1.title()) != kombina.index(kombina2.title()):
			kombinaa.append(kombina1+kombina2)

kombinaaw = []
for kombina1 in kombinaw:
	kombinaaw.append(kombina1)
	for kombina2 in kombinaw:
		if kombinaw.index(kombina1) != kombinaw.index(kombina2) and kombinaw.index(kombina1.title()) != kombinaw.index(kombina2.title()):
			kombinaaw.append(kombina1+kombina2)

kombinaak = []
for kombina1 in kombinak:
	kombinaak.append(kombina1)
	for kombina2 in kombinak:
		if kombinak.index(kombina1) != kombinak.index(kombina2) and kombinak.index(kombina1.title()) != kombinak.index(kombina2.title()):
			kombinaak.append(kombina1+kombina2)



komb1 = list(komb(kombinaa, bdss))
komb2 = list(komb(kombinaaw, wbdss))
komb3 = list(komb(kombinaak, kbdss))
komb4 = list(komb(kombinaa, years))
komb5 = list(komb(kombinaac, years))
komb6 = list(komb(kombinaaw, years))
komb7 = list(komb(kombinaak, years))
komb8 = list(komb(word, bdss))
komb9 = list(komb(word, wbdss))
komb10 = list(komb(word, kbdss))
komb11 = list(komb(word, years))
komb12 = ['']
komb13 = ['']
komb14 = ['']
komb15 = ['']
komb16 = ['']
komb21 = ['']

if random_num == "y":
	komb12 = list(concats(word, numfrom, numto))
	komb13 = list(concats(kombinaa, numfrom, numto))
	komb14 = list(concats(kombinaac, numfrom, numto))
	komb15 = list(concats(kombinaaw, numfrom, numto))
	komb16 = list(concats(kombinaak, numfrom, numto))
	komb21 = list(concats(reverse, numfrom, numto))
komb17 = list(komb(reverse, years))
komb18 = list(komb(rev_w, wbdss))
komb19 = list(komb(rev_k, kbdss))
komb20 = list(komb(rev_n, bdss))
komb001 = ['']
komb002 = ['']
komb003 = ['']
komb004 = ['']
komb005 = ['']
komb006 = ['']
if spechars1 == "y":
	komb001 = list(komb(kombinaa, spechars))
	komb002 = list(komb(kombinaac, spechars))
	komb003 = list(komb(kombinaaw , spechars))
	komb004 = list(komb(kombinaak , spechars))
	komb005 = list(komb(word, spechars))
	komb006 = list(komb(reverse, spechars))

print "[+] Sorting list and removing duplicates..."

komb_unique1 = dict.fromkeys(komb1).keys()
komb_unique2 = dict.fromkeys(komb2).keys()
komb_unique3 = dict.fromkeys(komb3).keys()
komb_unique4 = dict.fromkeys(komb4).keys()
komb_unique5 = dict.fromkeys(komb5).keys()
komb_unique6 = dict.fromkeys(komb6).keys()
komb_unique7 = dict.fromkeys(komb7).keys()
komb_unique8 = dict.fromkeys(komb8).keys()
komb_unique9 = dict.fromkeys(komb9).keys()
komb_unique10 = dict.fromkeys(komb10).keys()
komb_unique11 = dict.fromkeys(komb11).keys()
komb_unique12 = dict.fromkeys(komb12).keys()
komb_unique13 = dict.fromkeys(komb13).keys()
komb_unique14 = dict.fromkeys(komb14).keys()
komb_unique15 = dict.fromkeys(komb15).keys()
komb_unique16 = dict.fromkeys(komb16).keys()
komb_unique17 = dict.fromkeys(komb17).keys()
komb_unique18 = dict.fromkeys(komb18).keys()
komb_unique19 = dict.fromkeys(komb19).keys()
komb_unique20 = dict.fromkeys(komb20).keys()
komb_unique21 = dict.fromkeys(komb21).keys()
komb_unique01 = dict.fromkeys(kombinaa).keys()
komb_unique02 = dict.fromkeys(kombinaac).keys()
komb_unique03 = dict.fromkeys(kombinaaw).keys()
komb_unique04 = dict.fromkeys(kombinaak).keys()
komb_unique05 = dict.fromkeys(word).keys()
komb_unique07 = dict.fromkeys(komb001).keys()
komb_unique08 = dict.fromkeys(komb002).keys()
komb_unique09 = dict.fromkeys(komb003).keys()
komb_unique010 = dict.fromkeys(komb004).keys()
komb_unique011 = dict.fromkeys(komb005).keys()
komb_unique012 = dict.fromkeys(komb006).keys()

uniqlist = bdss+wbdss+kbdss+reverse+komb_unique01+komb_unique02+komb_unique03+komb_unique04+komb_unique05+komb_unique1+komb_unique2+komb_unique3+komb_unique4+komb_unique5+komb_unique6+komb_unique7+komb_unique8+komb_unique9+komb_unique10+komb_unique11+komb_unique12+komb_unique13+komb_unique14+komb_unique15+komb_unique16+komb_unique17+komb_unique18+komb_unique19+komb_unique20+komb_unique21+komb_unique07+komb_unique08+komb_unique09+komb_unique010+komb_unique011+komb_unique012

unique_lista = dict.fromkeys(uniqlist).keys()
unique_leet = []

# If you add more letters here you'll have to add more at the configutation file

if modo_leet == "y":
	for x in unique_lista:
		x = x.replace('a',a)
		x = x.replace('i',i)
		x = x.replace('e',e)
		x = x.replace('t',t)
		x = x.replace('o',o)
		x = x.replace('s',s)
		x = x.replace('g',g)
		x = x.replace('z',z)
		unique_leet.append(x)

unique_list = unique_lista + unique_leet

unique_list_finished = []
for x in unique_list:
	if len(x) > wcfrom and len(x) < wcto:
		unique_list_finished.append(x)

unique_list_finished.sort()

file_name=raw_input("\r\n[*] Type the name of output file: ")
f = open ( file_name+'.txt', 'w' )
f.write (os.linesep.join(unique_list_finished))
f = open ( name+'.txt', 'r' )
lines = 0
for line in f:
	lines += 1
f.close()

print "[+] Saving dictionary as \033[1;31m"+file_name+".txt\033[1;m, counting \033[1;31m"+str(lines)+"\033[1;m words."
exit()
