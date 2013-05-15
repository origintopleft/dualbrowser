from distutils.core import setup
import py2exe, sys
from time import sleep

sys.argv.append("py2exe")

print "Welcome to the setup script. Please hold while we examine the projectInf file"

# Defaults for some options
name = "Some Project"
version = "Some Version"
srcdir = "src"
libfile = "library.zip"
includes = [] # Nothing
excludes = [] # Also nothing

# Start the dict for config
configDict = {}

# Other initializations
mainfile = ""
iconfile = ""

# Open the config file and start checking it
try:
	with open("projectInf") as configFile:
		for configLine in configFile:
			config = configLine.strip("\n").split("=")
			if config[0] == "srcdir":
				srcdir = config[1]
			elif config[0] == "name":
				name = config[1]
			elif config[0] == "version":
				version = config[1]
			elif config[0] == "mainfile":
				mainfile = config[1]
			elif config[0] == "iconfile":
				iconfile = config[1]
			elif config[0] == "libfile":
				libfile = config[1]
			elif config[0] == "includes":
				includes = config[1].split("|")
			elif config[0] == "excludes":
				excludes = config[1].split("|")
			elif config[0] == "ascii":
				if config[1] == "1":
					configDict["ascii"] = True
				else:
					configDict["ascii"] = False
			else:
				configDict[config[0]] = config[1]
# What if the file doesn't exist?
except IOError:
	print "ERROR: projectInf file does not exist!"
	sleep(5)
	sys.exit()

# What if I forgot to define a main file?
if mainfile == "":
	print "ERROR: Main file is not defined!"
	sleep(5)
	sys.exit()

# Echo off what the projectInf file says
print "Here is the project information I have gathered:"
print " ; The project name is", name
print " ; The base source directory is", srcdir
print " ; The main file name is", mainfile
if iconfile == "":
	print " ; You have not selected an icon file."
else:
	print " ; The icon file is", iconfile
print " ; You wish to include: ",
for item in includes:
	print item + " ",
print ""
print " ; You wish to exclude: ",
for item in excludes:
	print item + " ",
print ""
print " ; You wish to name the library file \"" + libfile + "\""

# Get a confirmation
confirmation = raw_input("Is this correct? [Y/N] ")
# If yes, or anything starting with Y, do nothing
if confirmation[0].lower() == "y":
	pass
# Otherwise, exit gracefully
else:
	print "Goodbye."
	sleep(5)
	sys.exit()

# If we're here, it's time to get to work

# First, we need to flick the optimization on.
configDict["optimize"] = 2

# Create the dictionary for the setup script
mainFileDict = {"script": srcdir + "\\" + mainfile}
if iconfile != "":
	mainFileDict["icon_resources"] = [(1,srcdir + "\\" + iconfile)]

# Finally, the preparations are complete. LET US BEGIN!
setup(
	name = name,
	#version = version, # TODO
	windows = [mainFileDict],
	zipfile = libfile,
	options = {"py2exe": configDict}
)

# Wrap up by saying g'bye to the user
print "You should check to see if py2exe screwed up."
print "Exiting in ten seconds."
sleep(10)
sys.exit()
