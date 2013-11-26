class Error:
    def cannotOpenError(self):
        return "You can't open that!"
    def alreadyOpenError(self):
        return "It's already open!"
    def lockedNeedKeyError(self):
        return "You'll need a key to open that."
    def objectOutOfScopeError(self):
        return "You can't see that."
    def alreadyCarryingObjectError(self):
        return "You're already carrying that!"
    def uncarryableObjectError(self):
        return "You can't pick that up!"
    def openBeforeLookingInError(self):
        return "You'll have to open it first."

class Character:
    def __init__(self, name, description, inventory):
        self.name = name
        self.description = description
        self.inventory = inventory

class Player(Character):
    def __init__(self, name, description, inventory):
        self.name = "player"
        super().__init__

#def move(self, location):


class Object:
    def __init__(self, name, initDesc, description, carryable):
        self.name = name
        self.initDesc = initDesc
        self.description = description
        self.carryable = carryable

    def describe(self):
        print(self.description)

class Container(Object):
    def __init__(self, name, initDesc, description, openDesc, state="closed", openable=True, key=None, carryable=True):
        super().__init__
        self.openDesc = openDesc
        self.state = state
        self.openable = openable
        self.key = key

    def open(self):
        if self.state == 'open':
            print(Error().alreadyOpenError())
        elif self.state == 'locked':
            print(Error().lockedNeedKeyError())
        else:
            self.state = 'open'
            print("You open the {}.".format(self.name))

    def get(self):
        if self.carryable == True:
            if self in PLAYER.inventory:
                print(Error().alreadyCarryingObjectError())
            else:
                PLAYER.inventory.append(self)
                print("You pick up the {}.".format(self.name))
        else:
            print(Error().uncarryableObjectError())

    def describeInner(self):
        if self.state == 'open':
            print(self.openDesc)
        else:
            print(Error().openBeforeLookingInError())

class Clothing(Object):
    def __init__(self, name, initDesc, description, wornDesc, carryable=True, wearable=True, state="unworn"):
        self.name = name
        self.initDesc = initDesc
        self.description = description
        self.wornDesc = wornDesc
        self.carryable = carryable
        self.wearable = wearable
        self.state = state

class Scenery(Object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Scene:
    def enter(self):
        print("")
        print("This is the list objects function. It hasn't yet")
        print("been implemented.")

    def get(self, obj):
        if (type(obj) == Container and
            obj in self.objects and
            obj.carryable == True):
                obj.get()

    def describe(self, obj):
        if obj in self.objects:
            obj.describe()
        else:
            print(Error().objectOutOfScopeError())

PLAYER = Player('player','pretty nondescript',[])

class Bedroom(Scene):
    objects = {
                'snuffbox':Container("snuffbox","there is a fine wooden snuff box on the old oak table.","the snuff box is made of mahogany, with a tortoise shell inlay.\nit looks expensive.","the inside of the box is just as opulent as the outside; it's lined with a layer of mother of pearl that shimmers in the light.")
              }
    characters = {
                   'player':PLAYER
                 }

    def enter(self):
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


class Actions:
    def open(self,obj):
        if type(obj) == Container:
            if obj.state == 'open':
                print("It's already open!")
            elif obj.state == 'locked':
                # call to helpers.checkItemInInv
                # if obj.key in inventory, open. else, error.
                print("You can't open that without a key.")
            else:
                obj.state = 'open'
                print("You open the {}.".format(obj.name))
        else:
            print("That item is not openable.")

    def look(self, obj):
        if type(obj) == Container:
            if obj.state == 'open':
                print(obj.description)
                print("The {} is open.".format(obj.name))
            else:
                print(obj.closedDesc)
        elif type(obj) == Scenery:
            print(obj.description)

    def lookin(self, obj):
        if type(obj) != Container:
            print("You can't look inside of that!")
        elif type(obj) == Container and obj.openable == True:             
            if obj.state == 'open':
                print(obj.openDesc)
            else:
                obj.state = 'open'
                print("First opening the {}:".format(obj.name))
                print(obj.openDesc)
        else:
            print("You can't look inside of that!")

