import hexchat
import random

__module_name__ = "BleepingVomputer helping tool"
__module_version__ = "1.5"
__module_description__ = "Helps with questions."
__modeule_git__ = "https://github.com/EnyMan/Python/tree/master/BCstuff"
 
def Links(word, words_eol, userdata):

	#print word, " ", words_eol, " ", userdata

	if word[1] == "-h":
		hexchat.command("say Posible links: recuva, mbam, speccy, jrt, adw, ccleaner, speedfan, hidden, restorepoint, intel, infection, malware")

	elif word[1] == "recuva":
		hexchat.command("say To get Recuva CLICK -> http://www.bleepingcomputer.com/download/recuva/")

	elif word[1] == "mbam":
		hexchat.command("say To get Malwarebytes Anti-Malware CLICK -> http://www.bleepingcomputer.com/download/malwarebytes-anti-malware/")

	elif word[1] == "speccy":
		hexchat.command("say To get Speccy CLICK -> http://www.bleepingcomputer.com/download/speccy/")

	elif word[1] == "jrt":
		hexchat.command("say To get Junkware Removal Tool CLICK -> http://www.bleepingcomputer.com/download/junkware-removal-tool/")

	elif word[1] == "adw":
		hexchat.command("say To get AdwCleaner CLICK -> http://www.bleepingcomputer.com/download/adwcleaner/")

	elif word[1] == "ccleaner":
		hexchat.command("say To get CCleaner CLICK -> http://www.bleepingcomputer.com/download/ccleaner/")

	elif word[1] == "speedfan":
		hexchat.command("say To get SpeedFan CLICK -> http://www.bleepingcomputer.com/download/speedfan/")

	elif word[1] == "hidden":
		hexchat.command("say How to see hidden files/folders on windows CLICK -> http://www.bleepingcomputer.com/tutorials/how-to-see-hidden-files-in-windows/")

	elif word[1] == "restorepoint":
		hexchat.command("say System restore point CLICK -> http://windows.microsoft.com/cs-cz/windows-vista/turn-back-time-on-your-pc-undo-system-changes-with-system-restore")

	elif word[1] == "intel":
		hexchat.command("say Intel Update Utility CLICK -> http://www.intel.com/p/en_US/support/detect?iid=dc_iduu")

	elif word[1] == "infection":
		hexchat.command("say For infection removal CLICK -> http://www.bleepingcomputer.com/forums/t/34773/preparation-guide-for-use-before-using-malware-removal-tools-and-requesting-help/")		

	elif word[1] == "malware":
		hexchat.command("say For infection removal CLICK -> http://www.bleepingcomputer.com/forums/f/103/am-i-infected-what-do-i-do/")	
	
	else:
		hexchat.command("say To get more help CLICK -> http://www.bleepingcomputer.com/")

	return hexchat.EAT_ALL
 

def HelpWheel(word, words_eol, userdata):

	#print word, " ", words_eol, " ", userdata


	val2 = random.randint(1,10)

	if val2 == 1:
		hexchat.command("say For malware removal we suggest using our forum or talking to someone from MRT program.")

	elif val2 == 2:
		hexchat.command("say Yes, click OK")

	elif val2 == 3:
		hexchat.command("say Your data are completly lost and can't be recovered.")

	elif val2 == 4:
		hexchat.command("say OK, let me google that for you.")

	elif val2 == 5:
		hexchat.command("say Have you tried turning it off and on again? aka reboot?")

	elif val2 == 6:
		hexchat.command("say Are all wires connected correctly? Double check them please.")

	elif val2 == 7:
		hexchat.command("say Well that is a problem isn't it?")

	elif val2 == 8:
		hexchat.command("say NO!")

	elif val2 == 9:
		hexchat.command("say Make sure your keyboard is plugged in correctly.")

	else:
		hexchat.command("say Yes, click OK.")

	return hexchat.EAT_PLUGIN
 

def AutoLinks(word, words_eol, userdata):

	array = hexchat.get_list("users")
	user = word[0]

	for i in array:
		if i.nick == user:
			if i.prefix == "+" or i.prefix == "@" or i.prefix == "&" or i.prefix == "%":
				break
			else:
				print "bad prefix ", i.prefix
				return hexchat.EAT_PLUGIN
		else:
			pass

	if hexchat.get_info("away") == None:
		return hexchat.EAT_PLUGIN
	
	#print word[1]
	
	lenght = len(word[1])
	#print "lenght ", lenght
	
	loader = word[1][0:6].lower()
	#print "loader " + loader
	
	command = word[1][6:9]
	
	if command == "/bc":
		#print "found /bc"
		message = word[1][10:lenght]
		Links(['bc', message], [word[1][7:lenght], message], None)
	else:
		#print "found something else"
		command = word[1][6:11]
		if command == "/spin":
			#print "found /spin"
			HelpWheel(['spin'], ['spin'], None)
		else:
			#print "exiting"
			return hexchat.EAT_PLUGIN

	return hexchat.EAT_PLUGIN

hexchat.hook_print("Channel Msg Hilight", AutoLinks)
hexchat.hook_command("spin", HelpWheel)
hexchat.hook_command("bc", Links)
print "Loaded spin.py /spin to spin the wheel \n/bc [program] to show download link, use -h for help."