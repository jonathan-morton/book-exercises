from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)
indata = open(from_file).read()
open(to_file, 'w').write(indata)
print "Done"