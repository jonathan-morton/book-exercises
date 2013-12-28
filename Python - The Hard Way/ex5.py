name = 'Jonathan Morton'
age = 24 #True
height = 74
weight = 170
eyes = 'brown'
teeth = 'white'
hair = 'black'

print "Let's talk about %r" % name
print "He's %r inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually thats not too too too heavy"
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#This line is hard to get right
print "If I add %d, %d, and %d I get %d" % (
	age, height, weight, age + height + weight)