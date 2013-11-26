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
    def notCarryingObjectError(self):
        return "You're not carrying that!"
    def uncarryableObjectError(self):
        return "You can't pick that up!"
    def openBeforeLookingInError(self):
        return "You'll have to open it first."
        
class ItemManager:
    items = {}
    # snuffbox:{
    #    ownedBy:BedRoom }

    def sceneInit(self, objList, owner):
        for obj in objList:
           self.items[obj.name] = {'self':obj,'ownedBy':owner}

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

class Character:
    def __init__(self, name, description, inventory, location):
        self.name = name
        self.description = description
        self.inventory = inventory
        self.location = location

class Player(Character):
    def __init__(self, name, description, inventory, location):
        super().__init__(name, description, inventory, location)

#def move(self, location):


class Item:
    def __init__(self, name, initDesc, description, carryable):
        self.name = name
        self.initDesc = initDesc
        self.description = description
        self.carryable = carryable

    def describe(self):
        print(self.description)

class Container(Item):
    def __init__(self, name, initDesc, description, openDesc, state="closed", openable=True, key=None, carryable=True):
        self.openDesc = openDesc
        self.state = state
        self.openable = openable
        self.key = key
        super().__init__(name, initDesc, description, carryable)

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
                PLAYER.location.objects.remove(self)
                print("You pick up the {}.".format(self.name))
        else:
            print(Error().uncarryableObjectError())

    def drop(self):
        if self in PLAYER.inventory:
            PLAYER.inventory.remove(self)
            PLAYER.location.objects.append(self)
            print("You drop the {}.".format(self.name))
        else:
            print(Error().notCarryingObjectError())

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

class Scene:
    def enter(self):
        print("")
        print("This is the list objects function. It hasn't yet")
        print("been implemented.")
        ItemManager().sceneInit(self.objects, self)

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

PLAYER = Player('player','pretty nondescript',[],"")

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


# itemManager keeps track of item ownership
# when a scene is initialized, it passes its list of
# contents to ItemManager, who stores it in its dict

# class ItemManager
#    def addItem(self, obj, owner):
#        
#    def queryOwner(obj)
#        return obj.owner
#    def changeLocation(obj,objNewLocation)
#         obj.location = obj.NewLocation
