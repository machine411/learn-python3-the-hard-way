from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

class Engine(object):

    def __init__(self,scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            if current_scene != None:
                next_scene_name = current_scene.enter()
                current_scene = self.scene_map.next_scene(next_scene_name)
            else:
                break
        #current_scene.enter()

class Death(Scene):
    quips = [
        "You died. You kinda suck at this.",
        "Your Mom would be proud...if she were smarter.", "Such a luser.",
        "I have a small puppy that's better at this.", "You're worse than your Dad's jokes."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
              The Gothons of Planet Percal #25 have invaded your ship and
              destroyed your entire crew. You are the last surviving
              member and your last mission is to get the neutron destruct
              bomb from the Weapons Armory, put it in the bridge, and
              blow the ship up after getting into an escape pod.

              You're running down the central corridor to the Weapons
              Armory when a Gothon jumps out, red scaly skin, dark grimy
             teeth, and evil clown costume flowing around his hate
             filled body. He's blocking the door to the Armory and
             about to pull a weapon to blast you.
              """))
        action = input("> ")
        if action == "shoot!":
            print(dedent("""
                  Quick on the draw you yank out your blaster and fire
                  it at the Gothon. His clown costume is flowing and
                  moving around his body, which throws off your aim.
                  Your laser hits his costume but misses him entirely.
                  This completely ruins his brand new costume his mother
                  balabala
                  """))
            return 'death'

        elif action == "dodge!":
             print(dedent("""
                   Like a world class boxer you dodge, weave, slip and
                   slide right as the Gothon's blaster cranks a laser
                   past your head. In the middle of your artful dodge
                   your foot slips and you bang your head on the metal
                   wall and pass out. You wake up shortly after only to
                   die as the Gothon stomps on your head and eats you
                   """))
             return 'death'
        elif action == "tell a joke":
             print(dedent("""
                 Lucky for you they made you learn Gothon insults in
                 the academy. You tell the one Gothon joke you know:
                 Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr,
                 fur fvgf nebhaq gur ubhfr. The Gothon stops, tries
                 not to laugh, then busts out laughing and can't move.                 While he's laughing you run up and shoot him square in                      the head putting him down, then jump through the
                 Weapon Armory door.
                 """))
             return 'leaser_weapon_armory'
        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'
class LaserWeappnArmory(Scene):

    def enter(self):
        print(dedent("""
        You do a dive roll into the Weapon Armory, crouch and scan
        the room for more Gothons that might be hiding. It's dead
        quiet, too quiet. You stand up and run to the far side of
        the room and find the neutron bomb in its container.
         There's a keypad lock on the box and you need the code to
         get the bomb out. If you get the code wrong 10 times then
         the lock closes forever and you can't get the bomb. The
         code is 3 digits.
        """))

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0
        while guess != code and guesses < 10:
            print("BZZZZEDDD!")
            guesses +=1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
            the container clicks open and the steal
            gas out.
            you can to the TheBridge
            right spot.
            """))
            return 'the_bridge'
        else:
            print(dedent("""
                the lock buzzes one last
                sickening
                togther.
                gothons blow up
                """))
            return 'death'

class TheBridge(Scene):

    def enter(self):
        print(dedent("""
              You burst onto the bridge
              under your arm and
              take control
              clown costume than the last.
              weapons out yet.
              arm and don't want to set it off.
                """))

        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
                in a panic you throws
                and make a leap for the doors
                gothon shoots you right in the back
                you die you see another
                disarm the bomb.
                blow up when it goes off.
            """))
            return 'death'

        elif action =="slowly place the bomb":
            print(dedent("""
                You point your blaster at
                the gothons put their hands
                you inch backward to the door,
                carefully place the bomb on the floor,
                blaster at it.
                punch the close button and blast
                gothons can't get out.
                you run to the escape pod
            """))
            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE!")
            return "the_bridge"

class EscapePod(Scene):

    def enter(self):
        print(dedent("""
            You rush through the ship
            the escape pod before the whole ship
            like hardly any gothons are on the ship
            clear of interference. you get to the
            escape pods, and now need to pick one # TODO:
            them could be damaged but you don't have
            There's 5 pods,which one do you take?
            """))

        good_pod = randint(1,5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent("""
                You jump into pod {guess} and hit the
                The pod escape out into the void
                implodes as the hull ruptures,
                jam jelly.
            """))
            return 'death'
        else:
            print(dedent("""
            You jump into pod {guess} and hit the ej
            The pod easily slides out into space
            planet below. As it flies to the
            back and see your ship implode
            bright star, taking out the gothon ship
            time, you won!
            """))
            return 'finished'
class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        return 'finished'



class Map(object):

    scenes = {
        'central_corridor':CentralCorridor(),
        'leaser_weapon_armory':LaserWeappnArmory(),
        'the_brideg':TheBridge(),
        'escape_pod':EscapePod(),
        'death':Death(),
        'finished':Finished(),
    }
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
