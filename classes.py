import sys
from pyparsing import *

# ===============================================================

class Error:
    def cannotOpenError(self):
        return "You can't open that!"
    def alreadyOpenError(self):
        return "It's already open!"
    def alreadyClosedError(self):
        return "It's already closed!"
    def lockedNeedKeyError(self):
        return "You'll need a key to open that."
    def objectOutOfScopeError(self):
        return "You can't see that."
    def alreadyCarryingObjectError(self):
        return "You're already carrying that!"
    def notCarryingObjectError(self):
        return "You're not carrying that!"
    def uncarryableObjectError(self):
        return "You can't pick that up!"
    def openBeforeLookingInError(self):
        return "You'll have to open it first."
    def unknownActionError(self):
        return "I don't know how to do that."
    def mustProvideObjectError(self):
        return "You must provide an object."

# ===============================================================
        
class ItemManager:
    items = {}

    def sceneInit(self, objList, owner):
        for obj in objList:
           self.items[obj.name] = {'self':obj,'ownedBy':owner}

    def fetchItem(self, name, directObject=True):
        try: 
            if directObject == True:
                return self.items[name]['self']
            else:
                return self.items[name]
        except:
            return False

    def tryAction(self, item, action):
        try:
            getattr(item,action)()
        except:
            raise Exception
            
    def changeOwner(self, obj, newOwner):
        if obj.name in self.items:
            self.items[obj.name]['ownedBy'] = newOwner
            return True
        else:
            return False

    def determineOwner(self, obj):
        if obj.name in self.items:
            return self.items[obj.name]['ownedBy']
        else:
            return False

    def determineScope(self, obj):
        if obj.name in self.items:
            if (self.determineOwner(obj) == PLAYER.location or
                self.determineOwner(obj) == PLAYER):
                return True
            else:
                return False

# ===============================================================

class Character:
    def __init__(self, name, description, inventory, location):
        self.name = name
        self.description = description
        self.inventory = inventory
        self.location = location

class Player(Character):
    def __init__(self, name, description, inventory, location):
        super().__init__(name, description, inventory, location)

# ===============================================================

PLAYER = Player('player','pretty nondescript',[],"")

# ===============================================================

class Item:
    def __init__(self, name, initDesc, description, carryable):
        self.name = name
        self.initDesc = initDesc
        self.description = description
        self.carryable = carryable

    def check(func):
        def decorated(*args, **kwargs):
            if ItemManager().determineScope(*args) == True:
                return func(*args, **kwargs)
            else:
                print(Error().objectOutOfScopeError())
        return decorated

    @check
    def describe(self):
        print(self.description)

    @check
    def get(self):
        if self.carryable == True:
            if ItemManager().determineOwner(self) == PLAYER:
                print(Error().alreadyCarryingObjectError())
            else:
                ItemManager().changeOwner(self,PLAYER)
                print("You pick up the {}.".format(self.name))
        else:
            print(Error().uncarryableObjectError())

    def drop(self):
        if ItemManager().determineOwner(self) == PLAYER:
            ItemManager().changeOwner(self, PLAYER.location)
            print("You drop the {}.".format(self.name))
        else:
            print(Error().notCarryingObjectError())

class Container(Item):
    def __init__(self, name, initDesc, description, openDesc, state="closed", openable=True, key=None, carryable=True):
        self.openDesc = openDesc
        self.state = state
        self.openable = openable
        self.key = key
        super().__init__(name, initDesc, description, carryable)

    @Item.check
    def open(self):
        if self.state == 'open':
            print(Error().alreadyOpenError())
        elif self.state == 'locked':
            print(Error().lockedNeedKeyError())
        else:
            self.state = 'open'
            print("You open the {}.".format(self.name))

    @Item.check
    def close(self):
        if self.state == 'open':
            self.state = 'closed'
            print("You close the {}.".format(self.name))
        else:
            print(Error().alreadyClosedError())

    @Item.check
    def describeInner(self):
        if self.state == 'open':
            print(self.openDesc)
        else:
            print(Error().openBeforeLookingInError())

class Clothing(Item):
    def __init__(self, name, initDesc, description, wornDesc, carryable=True, wearable=True, state="unworn"):
        self.name = name
        self.initDesc = initDesc
        self.description = description
        self.wornDesc = wornDesc
        self.carryable = carryable
        self.wearable = wearable
        self.state = state

class Scenery(Item):
    def __init__(self, name, description):
        self.name = name
        self.description = description

# ===============================================================

class Scene:
    def enter(self):
        print("")
        print("This is the list objects function. It hasn't yet")
        print("been implemented.")
        ItemManager().sceneInit(self.objects, self)

    def describe(self):
        print("There will be a description implemented in this class soon, as well as a printedName.")


class Bedroom(Scene):
    objects = [
                Container("snuffbox","there is a fine wooden snuff box on the old oak table.","the snuff box is made of mahogany, with a tortoise shell inlay.\nit looks expensive.","the inside of the box is just as opulent as the outside; it's lined with a layer of mother of pearl that shimmers in the light.")
              ]

    def enter(self):
        PLAYER.location = self
        print("Shit. Saigon.")
        print("You try to shake the cobwebs from your fuzzy mind,")
        print("realizing too late that your head is pounding.")
        print("The overhead fan is way too fucking loud, and")
        print("through the jagged pane of your broken window,")
        print("the sounds of a busy city invade.")
        print("")
        print("You take a slug from the bottle of whiskey on your")
        print("nightstand and sit up, scanning the room.")

        super().enter()

# ===============================================================

class Commands:
    def help(self):
        print("----")
        print("Interact with the parser using the following commands:")
        print("look: Use with an object to describe it; use on its own to describe your surrounds.")
        print("search <object>: Look inside an object.")
        print("go <direction>: Move the player in a specific direction.")
        print("get <object>: Pick up an object.")
        print("drop <object>: Drop an object you're carrying.")
        print("open <object>: Open an object.")
        print("close <object>: Close an object.")
        print("----")
    def quit(self):
        sys.exit()

class Parser:
    actions = ['look','search','go','get','drop','open','close']
    directions = ['north','east','south','west']
    commands = ['help','quit']
    objects = []

    def parse(self, sentence):
        parseTemplate = Optional(oneOf("describe search get").setResultsName("verb")) + Optional(oneOf("north east south west").setResultsName("direction")) + Optional(oneOf("at in").setResultsName("preposition")) + Optional(Word(alphas).setResultsName("object"))

        parsedString = parseTemplate.parseString(sentence)

        if not 'verb' in parsedString:
            print(Error().unknownActionError())
            return

        if (not 'object' in parsedString and
            parsedString['verb'] != 'describe'):
            print(Error().mustProvideObjectError())
            return

        if len(list(parsedString)) == 1:
            if parsedString['verb'] == "describe":
                PLAYER.location.describe()
        else:
            try:
                ItemManager().tryAction(ItemManager().fetchItem(parsedString['object']),
                                        parsedString['verb'])
            except:
                print(Error().objectOutOfScopeError())

