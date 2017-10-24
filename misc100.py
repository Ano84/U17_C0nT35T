#!/usr/bin/python
import sys
class Unbuffered(object):
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)


sys.stdout = Unbuffered(sys.stdout)
sys.stderr = None
b = """

 #     #
 #  #  # ###### #       ####   ####  #    # ######
 #  #  # #      #      #    # #    # ##  ## #
 #  #  # #####  #      #      #    # # ## # #####
 #  #  # #      #      #      #    # #    # #
 #  #  # #      #      #    # #    # #    # #
  ## ##  ###### ######  ####   ####  #    # ######

"""

banner = '\tWelcome to UIT Hacking Contest 2017!\nGive me a string "s" that s[:10] == s.encode("base64")[:10]'
print b
print banner
s = raw_input(">>> s = ")
s = s.rstrip("\n")

if s == "":
    print "Hmmm... are you dumb?"
elif s[:10] == s.encode("base64")[:10]:
    print 'Good job! Take your flag:\n'
    print 'welcome_to_uit-hacking-contest!_just_a_warm_up_challenge\n'
    print 'Bye! Good luck!\n'
else:
    print 'Try again!\n'