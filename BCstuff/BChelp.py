import hexchat
import random

__module_name__ = "BleepingVomputer helping tool"
__module_version__ = "1.6"
__module_description__ = "Helps with questions."
__modeule_git__ = "https://github.com/EnyMan/Python/tree/master/BCstuff"
 
def Links(word, words_eol, userdata):

	#print word, " ", words_eol, " ", userdata

	if word[1] == "-h":
		hexchat.command("say Posible links: recuva, mbam, speccy, jrt, adw, ccleaner, speedfan, hidden, restorepoint, intel, infection[forum], malware[guide], mini, usb")

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

	elif word[1] == "malware":
		hexchat.command("say Preparation guide for malware removal CLICK -> http://www.bleepingcomputer.com/forums/t/34773/preparation-guide-for-use-before-using-malware-removal-tools-and-requesting-help/")		

	elif word[1] == "infection":
		hexchat.command("say For infection removal CLICK -> http://www.bleepingcomputer.com/forums/f/103/am-i-infected-what-do-i-do/")

	elif word[1] == "mini":
		hexchat.command("say To get MiniToolBox CLICK -> http://www.bleepingcomputer.com/download/minitoolbox/")

	elif word[1] == "usb":
		hexchat.command("say To get Windows USB Tool CLICK -> http://www.microsoftstore.com/store/msusa/html/pbPage.Help_Win7_usbdvd_dwnTool")
			
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
		hexchat.command("say Your data is completely lost and can't be recovered.")

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
	user = word[0][3:]

	if  word[1][0:1] != "!":
		return hexchat.EAT_PLUGIN

	#to kill bnc
	if hexchat.get_info("nick") == "Mous|BNC":
		return hexchat.EAT_PLUGIN

	for i in array:
		#exceptions
		if user[0:8] == "JayTee84":
			break

		if i.nick == user:
			print "prefix test", i.nick, i.prefix
			if i.prefix == "+" or i.prefix == "@" or i.prefix == "&" or i.prefix == "%" or i.prefix == "~":
				break
			else:
				return hexchat.EAT_PLUGIN
		else:
			pass

	#if hexchat.get_info("away") == None:
	#	return hexchat.EAT_PLUGIN
	
	#print word[1]
	
	lenght = len(word[1])
	#print "lenght ", lenght
	
	#loader = word[1][0:6].lower()
	#print "loader " + loader
	#0123456789
	#!mbam mous

	if word[1][0:5] == "!spin":
		HelpWheel(['spin'], ['spin'], None)

	elif word[1][0:6].lower() == "!mhelp":
		msg = "Help msg for Mous commands, usage text in [] is the actual link, for instance [mbam] would be uses as \"!mbam\"."
		msg += " Posible links are [recuva], [mbam], [speccy], [jrt] junkware removal tool, [adw] AdwCleaner, [ccleaner], [speedfan], [mini] minitoolbox, [usb] windows 7 install usb,"
		msg += " [hidden] show hidden files in windows, [restorepoint] how to use restorepoints in windows, [intel] intel online driver checker, [infection] am i infected what do i do, [malware] preparation guide, [internet] the truth about internet."
		msg += " [google] usage: \"!google keyword\" would create search link for keyword, keyword is optional."
		hexchat.command("msg " + user + " " + msg)
	elif word[1][0:7] == "!google":
		if lenght > 7:
			hexchat.command("say Here is the mighty link -> https://www.google.com/#q=" + word[1][8:].replace(' ', '+'))
		else:
			hexchat.command("say The all mighty google is here -> https://www.google.com/")
	elif word[1][0:7] == "!recuva":
		if lenght > 7:
			hexchat.command("say "+ word[1][8:] +"you can get Recuva by clicking on this link -> http://www.bleepingcomputer.com/download/recuva/")
		else:
			hexchat.command("say To get Recuva CLICK -> http://www.bleepingcomputer.com/download/recuva/")

	elif word[1][0:5] == "!mbam":
		if lenght > 5:
			hexchat.command("say "+ word[1][6:] +" you can get Malwarebytes Anti-Malware by clicking on this link -> http://www.bleepingcomputer.com/download/malwarebytes-anti-malware/")
		else:
			hexchat.command("say To get Malwarebytes Anti-Malware CLICK -> http://www.bleepingcomputer.com/download/malwarebytes-anti-malware/")

	elif word[1][0:7] == "!speccy":
		if lenght > 7:
			hexchat.command("say "+ word[1][8:] +" you can get Speccy by clicking on this link -> http://www.bleepingcomputer.com/download/speccy/")
		else:
			hexchat.command("say To get Speccy CLICK -> http://www.bleepingcomputer.com/download/speccy/")

	elif word[1][0:4] == "!jrt":
		if lenght > 4:
			hexchat.command("say "+ word[1][5:] +" you can get Junkware Removal Tool by clicking on this link -> http://www.bleepingcomputer.com/download/junkware-removal-tool/")
		else:
			hexchat.command("say To get Junkware Removal Tool CLICK -> http://www.bleepingcomputer.com/download/junkware-removal-tool/")

	elif word[1][0:4] == "!adw":
		if lenght > 4:
			hexchat.command("say "+ word[1][5:] +" you can get AdwCleaner by clicking on this link -> http://www.bleepingcomputer.com/download/adwcleaner/")
		else:
			hexchat.command("say To get AdwCleaner CLICK -> http://www.bleepingcomputer.com/download/adwcleaner/")

	elif word[1][0:9] == "!ccleaner":
		if lenght > 9:
			hexchat.command("say "+ word[1][10:] +" you can get CCleaner by clicking on this link -> http://www.bleepingcomputer.com/download/ccleaner/")
		else:
			hexchat.command("say To get CCleaner CLICK -> http://www.bleepingcomputer.com/download/ccleaner/")

	elif word[1][0:9] == "!speedfan":
		if lenght > 9:
			hexchat.command("say "+ word[1][10:] +" you can get SpeedFan by clicking on this link -> http://www.bleepingcomputer.com/download/speedfan/")
		else:
			hexchat.command("say To get SpeedFan CLICK -> http://www.bleepingcomputer.com/download/speedfan/")

	elif word[1][0:7] == "!hidden":
		if lenght > 7:
			hexchat.command("say "+ word[1][8:] +" tutorial on how to see hidden files/folders is here -> http://www.bleepingcomputer.com/tutorials/how-to-see-hidden-files-in-windows/")
		else:
			hexchat.command("say How to see hidden files/folders on windows CLICK -> http://www.bleepingcomputer.com/tutorials/how-to-see-hidden-files-in-windows/")

	elif word[1][0:14] == "!restorepoint":
		hexchat.command("say System restore point CLICK -> http://windows.microsoft.com/cs-cz/windows-vista/turn-back-time-on-your-pc-undo-system-changes-with-system-restore")

	elif word[1][0:6] == "!intel":
		hexchat.command("say Intel Update Utility CLICK -> http://www.intel.com/p/en_US/support/detect?iid=dc_iduu")

	elif word[1][0:8] == "!malware":
		hexchat.command("say Preparation guide for malware removal CLICK -> http://www.bleepingcomputer.com/forums/t/34773/preparation-guide-for-use-before-using-malware-removal-tools-and-requesting-help/")		

	elif word[1][0:10] == "!infection":
		hexchat.command("say For infection removal CLICK -> http://www.bleepingcomputer.com/forums/f/103/am-i-infected-what-do-i-do/")

	elif word[1][0:5] == "!mini":
		if lenght > 5:
			hexchat.command("say "+ word[1][6:] +" you can get MiniToolBox by clicking on this link ->http://www.bleepingcomputer.com/download/minitoolbox/")
		else:
			hexchat.command("say To get MiniToolBox CLICK -> http://www.bleepingcomputer.com/download/minitoolbox/")

	elif word[1][0:4] == "!usb":
		hexchat.command("say To get Windows USB Tool CLICK -> http://www.microsoftstore.com/store/msusa/html/pbPage.Help_Win7_usbdvd_dwnTool")

	elif word[1][0:9] == "!internet":
		hexchat.command("say dont trust everything thats writen on the Internet")
	else:
		return hexchat.EAT_PLUGIN

	return hexchat.EAT_PLUGIN

hexchat.hook_print("Channel Message", AutoLinks)
hexchat.hook_command("spin", HelpWheel)
hexchat.hook_command("bc", Links)
print "Loaded spin.py /spin to spin the wheel \n/bc [program] to show download link, use -h for help."