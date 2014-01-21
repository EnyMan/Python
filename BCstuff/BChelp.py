import hexchat
import random

__module_name__ = "BleepingVomputer helping tool"
__module_version__ = "1.2"
__module_description__ = "Helps with questions."
__modeule_git__ = "https://github.com/EnyMan/Python/tree/master/BCstuff"
 
def Links(word, words_eol, userdata):

	if word[1] == "-h":
		hexchat.command("say Posible links: recuva, mbam, speccy, jrt, adw, ccleaner, speedfan, hidden, restorepoint, intel, infection")

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
		hexchat.command("say For infection removal CLICK -> http://www.bleepingcomputer.com/forums/f/22/virus-trojan-spyware-and-malware-removal-logs/")		

	else:
		hexchat.command("say To get more help CLICK -> http://www.bleepingcomputer.com/")

	return hexchat.EAT_ALL
 

def HelpWheelrand(word, words_eol, userdata):

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

	return hexchat.EAT_ALL
 

def AutoLinks(word, words_eol, userdata):

	if hexchat.get_info("away") == None:
		return hexchat.EAT_PLUGIN

	lenght = len(word[1])
	#print "lenght ", lenght
	
	loader = word[1][0:9]
	#print "loader " + loader

	message = word[1][10:lenght]
	#print "message " + message

	if loader == "mous: /bc":
		print "found command"
	else:
		#print "no '/bc' insted '" + loader + "' found"
		return hexchat.EAT_PLUGIN

	if message == "-h":
		hexchat.command("say Posible links: recuva, mbam, speccy, jrt, adw, ccleaner, speedfan, hidden, restorepoint, intel, infection")

	elif message == "recuva":
		hexchat.command("say To get Recuva CLICK -> http://www.bleepingcomputer.com/download/recuva/")

	elif message == "mbam":
		hexchat.command("say To get Malwarebytes Anti-Malware CLICK -> http://www.bleepingcomputer.com/download/malwarebytes-anti-malware/")

	elif message == "speccy":
		hexchat.command("say To get Speccy CLICK -> http://www.bleepingcomputer.com/download/speccy/")

	elif message == "jrt":
		hexchat.command("say To get Junkware Removal Tool CLICK -> http://www.bleepingcomputer.com/download/junkware-removal-tool/")

	elif message == "adw":
		hexchat.command("say To get AdwCleaner CLICK -> http://www.bleepingcomputer.com/download/adwcleaner/")

	elif message == "ccleaner":
		hexchat.command("say To get CCleaner CLICK -> http://www.bleepingcomputer.com/download/ccleaner/")

	elif message == "speedfan":
		hexchat.command("say To get SpeedFan CLICK -> http://www.bleepingcomputer.com/download/speedfan/")

	elif message == "hidden":
		hexchat.command("say How to see hidden files/folders on windows CLICK -> http://www.bleepingcomputer.com/tutorials/how-to-see-hidden-files-in-windows/")

	elif message == "restorepoint":
		hexchat.command("say System restore point CLICK -> http://windows.microsoft.com/cs-cz/windows-vista/turn-back-time-on-your-pc-undo-system-changes-with-system-restore")

	elif message == "intel":
		hexchat.command("say Intel Update Utility CLICK -> http://www.intel.com/p/en_US/support/detect?iid=dc_iduu")

	elif message == "infection":
		hexchat.command("say For infection removal CLICK -> http://www.bleepingcomputer.com/forums/f/22/virus-trojan-spyware-and-malware-removal-logs/")		

	else:
		hexchat.command("say To get more help CLICK -> http://www.bleepingcomputer.com/")

	return hexchat.EAT_PLUGIN


hexchat.hook_print("Channel Msg Hilight", AutoLinks)
hexchat.hook_command("spin", HelpWheelrand)
hexchat.hook_command("bc", Links)
print "Loaded spin.py /spin to spin the wheel \n/bc [program] to show download link, use -h for help."