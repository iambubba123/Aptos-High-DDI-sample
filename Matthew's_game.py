from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene =  self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('prize')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        #be sure to print out the last scene
        current_scene.enter()

class Dead(Scene):
    quips = [
        "You can do better than that.",
        "RIP",
        "Statistically, a monkey could do better left to its own devices.",
        "Don't give up, I like to laugh at you.",
        "A for effort, F for skill."
    ]
    def enter(self):
        print "You hear the computer", Dead.quips[randint(0, len(self.quips)-1)]
        return 'dark_room'

class DarkRoom(Scene):

    def enter(self):
        print "You wake up in a dark room, with all your stuff,"
        print "besides your clothes, taken. All of a sudden, you"
        print "hear a robotic voice 'Welcome. Escape every room and"
        print "get your stuff back, return home, AND get one wish granted, fail,"
        print "and you will die a horrible death. Do you ACCEPT or DECLINE"

        choice = raw_input("I ")

        if choice == "decline":
            print "The computer calls you a wimp and vaporizes you."
            return 'dead'

        elif choice == "accept":
            print "'Good', the computer says, 'now I will open the door,"
            print "which leads to the first room. There is no time limit,"
            print "but quit, and I will kill you. Good Luck."
            return 'the_first_room'

        else:
            print "What, I didn't hear you?"
            return 'dark_room'

class EscapeRoom(Scene):

    def enter(self):
        print "You enter the first room, and notice a locked door, a bag,"
        print "and an open window. What do you do first?"

        choice = raw_input("Examine ")

        if choice == "window":
            print "You climb through the window, not realizing that the"
            print "dungeon is located in space, millions of light years"
            print "away from earth. The window locks behind you and you"
            print "are lost in space without a space suit."
            return 'dead'

        elif choice == "door":
            print "Are you deaf? I just said the door is locked"
            return 'the_first_room'

        elif choice == "bag":
            print "You open the bag and find a key, a heavy marble,"
            print "and a book. You don't know what to do with these items,"
            print "but then you get a better look at the surroundings."
            return 'the_first_room_p2'
        else:
            print "I didn't catch that"
            return 'the_first_room'

class EscapeRoomP2(Scene):
    def enter(self):
        print "You notice that in the room there is a vase,"
        print "and a bookshelf with a book missing. You realize"
        print "that two of your three items can come in handy here."
        print "How do you proceed?"

        choice = raw_input("> ")

        if choice == "throw marble at vase":
            print "The vase falls to the ground and breaks, inside"
            print "there is a piece of paper. You read it."
            print "'The code to the safe is 654 followed by the current'"
            print "room number.' You should remember this."
            return 'the_first_room_p2'

        elif choice == "examine the door":
            print "Getting a closer look at the door, you discover"
            print "That it is actually locked using a passcode. Try to find"
            print "a clue to the code"
            code = "2001"
            guess = raw_input("[keypad]> ")


            while guess != code:
                print "The door is still locked."
                guess = raw_input("[keypad]> ")

            if guess == code:
                print "The door clicks open and you find yourself in another"
                print "room with two doors. The computer says that one door"
                print "leads to a logic puzzle, and the other leads to a math"
                print "puzzle. Both rooms end up in the same place. What door"
                print "do you choose?"

                choice = raw_input("> ")

                if choice == "Logic":
                    return 'logic_room'
                elif choice == "Math":
                    return 'math_room'
                else:
                    print "Choose a room!"
                    return 'the_first_room_p2'

        elif choice == "put book in bookshelf":
            print "The bookshelf moves! Behind it is a safe, locked"
            print "with a double lock, a keyhole and a passcode. You"
            print "use the key on the first lock, but still need the passcode."
            code = "6541"
            guess = raw_input("[keypad]> ")

            while guess != code:
                print "Nope, still locked."
                guess = raw_input("[keypad]> ")

            if guess == code:
                "You open the safe and inside is another piece of paper."
                print "You read it: 'the code to the door is the year"
                print "of tragic terrorist attacks in New York, USA.'"
                print "Remember this. Maybe now you should examine the door"
                return 'the_first_room_p2'
        else:
            print "I don't understand!"
            return 'the_first_room_p2'

class LogicRoom(Scene):

    def enter(self):
        print "You come into a room with another passcode door."
        print "However, in order to open this one, you must type"
        print "in the correct answer to the logic puzzle given"
        print "to you by the computer. The puzzle is as follows:"
        print "'Mary\'s mother has four children. The first child"
        print "is named April, the second May, and the third June."
        print "What is the name of the fourth child?"

        name = "Mary"
        answer = raw_input("[keypad]> ")

        while answer != name:
            print "Wrong answer!"
            return 'logic_room'

        if answer == name:
            print "The door unlocks and you enter what seems to be the final room."
            return 'final_room'

class MathRoom(Scene):
    def enter(self):
        print "You come into a room with another passcode dooe."
        print "However, in order to open this one, you must type"
        print "in the correct answer to the math puzzle given"
        print "to you by the computer. The puzzle is as follows:"
        print "'What 3 positive numbers give the same result when"
        print "multiplied together or added together?"

        numbers = "1, 2, and 3"
        answer = raw_input("[keypad]> ")

        while answer != numbers:
            print "Wrong answer! Type the answer as _, _, and _ if you think"
            print "you got it right"
            return 'math_room'

        if answer == numbers:
            "The door unlocks and you enter what seems to be the final room."
            return 'final_room'

class FinalRoom(Scene):

    def enter(self):
        print "The computer congratulates you for making it this far,"
        print "but warns you that the final challenge will not be easy,"
        print "and once mistake will kill you. An ogre is sleeping in"
        print "front of an open door, and you must find a way to get"
        print "to the door. There are various items like a rock and"
        print "a metal sheet next to you. What do you do?"

        choice = raw_input("> ")

        if choice == "sneak past ogre":
            print "The ogre hears you, wakes up, and snaps your"
            print "limbs like toothpicks before eating you."
            return 'dead'
        elif choice == "throw rock at ogre":
            print"The ogre wakes up without any sign of pain, but he"
            print "is angry. He smashes you with his spiky club."
            return 'dead'
        elif choice == "throw rock at metal sheet":
            print "The ogre wakes up and runs to check out"
            print "the sound. While he's distracted, you run"
            print "through the door. You made it! Now for your prize!"
            return 'prize'
        else:
            print "WHAT DO YOU DO?"
            return 'final_room'

class PrizeRoom(Scene):

    def enter(self):
        print "The computer congratulates you and offers you"
        print "your wish. What do you wish for, money, power,"
        print "or wisdom?"

        wish = raw_input("I wish for ")

        if wish == "money":
            print "The computer gives you a debit card linked to a"
            print "bank account that never decreases and sends you"
            print "back home. You spend money like crazy with no"
            print "consequences."
            print "The End!"

        elif wish == "power":
            print "The computer returns you home, and upon"
            print "arriving, you find out that you are quite"
            print "literally the king of the world. Worldwide"
            print "laws are now yours to enact and do what you"
            print "want with. Don't abuse this power!"
            print "The End!"

        elif wish == "wisdom":
            print "The computer grants you truly infinite wisdom"
            print "and knowledge. You graduate at the top of your"
            print "class and get so many scholarships YOU GET"
            print "paid tuition to go to university. You become"
            print "the best professional in the world."
            print "The End!"
        else:
            print "The computer didn't hear you, and sends"
            print "you back to earth with no wish granted."
            print "The End"


class Map(object):

    scenes = {
        'dead': Dead(),
        'prize': PrizeRoom(),
        'final_room': FinalRoom(),
        'math_room': MathRoom(),
        'logic_room': LogicRoom(),
        'the_first_room': EscapeRoom(),
        'the_first_room_p2': EscapeRoomP2(),
        'dark_room': DarkRoom(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('dark_room')
a_game = Engine(a_map)
a_game.play()

raw_input ('Press ENTER to close')
