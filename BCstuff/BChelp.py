import hexchat
import random

__module_name__ = "BleepingVomputer helping tool"
__module_version__ = "1.2"
__module_description__ = "Helps with questions."
__modeule_git__ = "https://github.com/EnyMan/Python/tree/master/BCstuff"
 
def DownloadLinks(word, words_eol, userdata):

	if word[1] == "recuva":
		hexchat.command("say To get Recuva click -> http://www.bleepingcomputer.com/download/recuva/")

	elif word[1] == "mbam":
		hexchat.command("say To get Recuva Malwarebytes Anti-Malware click -> http://www.bleepingcomputer.com/download/malwarebytes-anti-malware/")

	elif word[1] == "speccy":
		hexchat.command("say To get Speccy click -> http://www.bleepingcomputer.com/download/speccy/")

	elif word[1] == "jrt":
		hexchat.command("say To get Junkware Removal Tool click -> http://www.bleepingcomputer.com/download/junkware-removal-tool/")

	elif word[1] == "adw":
		hexchat.command("say To get AdwCleaner click -> http://www.bleepingcomputer.com/download/adwcleaner/")

	elif word[1] == "ccleaner":
		hexchat.command("say To get CCleaner click -> http://www.bleepingcomputer.com/download/ccleaner/")

	elif word[1] == "speedfan":
		hexchat.command("say To get SpeedFan click -> http://www.bleepingcomputer.com/download/speedfan/")

	elif word[1] == "hidden":
		hexchat.command("say How to see hidden files/folders on windows click -> http://www.bleepingcomputer.com/tutorials/how-to-see-hidden-files-in-windows/")

	else:
		hexchat.command("say To get more help click -> http://www.bleepingcomputer.com/")

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
 

hexchat.hook_command("spin", HelpWheelrand)
hexchat.hook_command("bc", DownloadLinks)
print "Loaded spin.py /spin to spin the wheel \n/bc [program] to show download link."
