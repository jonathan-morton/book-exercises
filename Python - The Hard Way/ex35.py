from sys import exit

def gold_room():
    print "This room is full of gold. How much do you take?"
    
    next = raw_input("> ")
    if int(next):
        how_much = int(next)
    else:
        dead("Man, learn to type a number")
    
    if how_much < 50:
        print "You're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print "There is a bear with a lot of honey here"
    print "How will you move the bear?"
    
    bear_moved = False
    
    while True:
        next = raw_input("> ")
        
        if next == "take honey":
            dead("The bear slaps your face off")
        elif next == "taunt bear" and not bear_moved:
            print "The bear moved"
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear came back and killed you")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I don't know what you mean"
            
def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"
    
    next = raw_input("> ")
    
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty")
    else:
        cthulhu_room()

def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    next = raw_input("> ")
    
    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You tripped and fell on a knife")

start()
            