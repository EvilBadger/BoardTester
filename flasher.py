#
#
#
#
#
import ConfigParser
from subprocess import call

def ReadConfig ( option ):
   # Returns config file as a dict
   ConfigFile = ConfigParser.ConfigParser()
   ConfigFile.read("flasher.cfg")
   return ConfigFile.get("Config" , option )

def InitGPIO ():
    # Set up all of the GPIO ports
	#
	#Define Pins
    errLED   = "pinname"
    passLED  = "pinname"
    pwrPIN   = "pinname"
    bootPIN  = "pinname"
    pwrPIN   = "pinname"
    flashTestBTN = "pinname"
    flashProdBTN = "pinname"
	
	#Setup ports and Inputs/Outputs etc...
    return

def Flash(file):
    cmd = "stm32flash -w " + file + " -v -g 0x0 -b 115200 " + ReadConfig("SerialDevice")
    print cmd
    if (call( cmd.split(), shell=False )):
        print "Flashed Successful\n"

Flash( ReadConfig("ProdHex"))
