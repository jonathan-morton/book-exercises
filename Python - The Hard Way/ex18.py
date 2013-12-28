#This is a convoluted way to make a function
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#Normal way
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    
def print_one(arg1):
    print "arg1: %r" % arg1

def print_none():
    print "I got nothing"

print_two("Jonathan", "Morton")
print_two_again("Jonathan", "Morton")
print_one("First")
print_none()
