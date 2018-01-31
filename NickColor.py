import hexchat
import re
import random
import urllib2
import json
import sys
import os
import time
reload(sys);
sys.setdefaultencoding("utf8")

__module_name__ = 'NickColor'
__module_version__ = '1.0'
__module_author__ = "cbool222"
__module_description__ = 'Skrypt kolorujący nicki.'

hexchat.prnt('\002\00304Załadowano skrypt NickColor\002\003')


		
def colored(word, word_eol, userdata):
		if word[2] == "@":
			nick = "\002\00303" + word[0] + "\002\003"
			message = word[1]
			hexchat.emit_print("Channel Message", nick, message)
			return hexchat.EAT_ALL
		elif word[2] == "+":
			nick = "\002\00308" + word[0] + "\002\003"
			message = word[1]
			hexchat.emit_print("Channel Message", nick, message)
			return hexchat.EAT_ALL
		elif word[2] == "!":
			nick = "\002\00306" + word[0] + "\002\003"
			message = word[1]
			hexchat.emit_print("Channel Message", nick, message)
			return hexchat.EAT_ALL
		elif word[2] == "%":
			nick = "\002\00310" + word[0] + "\002\003"
			message = word[1]
			hexchat.emit_print("Channel Message", nick, message)
			return hexchat.EAT_ALL
		elif word[0] == "Wonziu":
			nick = "\002\00304" + word[0] + "\002\003"
			message = "\002\00304" + word[1] + "\002\003"
			hexchat.emit_print("Channel Message", nick, message)
			return hexchat.EAT_ALL	
		elif word[0] == "dzej":
			nick = "\002\00309" + word[0] + "\002\003"
			message = "\002\00309" + word[1] + "\002\003"
			hexchat.emit_print("Channel Message", nick, message)
			return hexchat.EAT_ALL				

hexchat.hook_print('Channel Message', colored)