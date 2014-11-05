# Exercise 43: Basic Object Oriented Analysis & Design

# 1. Write/draw about the problem. 
# 2. Extract key concepts
# 3. Create a class hierarchy and object map for the concepts. (Nouns for classes, verbs for functions)
# 4. Skeleton code and test
# 5. Repeat

# *Map 
#  - next_scene
#  - opening_scene
# *Engine
#  -play
# *Scene 
#  - enter
#  * Death
#  * Central Corridor
#  * Laser Weapon Armory
#  * The Bridge
#  * Escape Pod

from sys import exit
from random import randint

class Scene(object):

	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()"
		exit(1)

class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()

		while True:
			print "\n---------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)


class Death(Scene):

	quips = [
		"You died. You kinda suck at this.",
		"Your mom would be proud... if she were smarter",
		"Such a luser.",
		"I have a small puppy thats better at this"
	]

	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)



class CentralCorridor(Scene):

	def enter(self):
		print """
		The Gothons of Planet Percal #25 have invaded your ship and destroyed
		your entire crew. You are the last surviving member and your last
		mission is to get the neutron destruct bomb from the Weapons Armory,
		put it in the bridge, and blow up the ship after getting into an escape pod
		"""
		print "\n"
		print """
		You're running down the central corridor to the Weapons Armory when
		a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume
		flowing around his hate filled body. Hes blocking the door to the Armory
		and about to pull a weapon to blast you. 
		"""

		action = raw_input("> ")

		if action == "shoot!":
			print " Blah blah blah happens"
			print "you are dead."
			return 'death'

		elif action == "dodge!":
			print "You try to dodge"
			print " you're dead"
			return 'death'

		elif action == "tell a joke!":
			print "You try to dodge"
			print " you're dead"
			return 'laser_weapon_armory'

		else:	
			print "DOES NOT COMPUTE"
			return 'central_corridor'	

class LaserWeaponArmory(Scene):

	def enter(self):
		pass

class TheBridge(Scene):

	def enter(self):
		pass		

class EscapePod(Scene):

	def enter(self):
		pass


class Map(object):

	def __init__(self, start_scene):
		pass

	def next_scene(self, scene_name):
		pass

	def opening_scene(self):
		pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()