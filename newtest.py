class Container:
    def __init__(self, name, description, contents):
        self.name = name
        self.description = description
        self.contents = contents

class Item:
    def __init__(self, 
                 name, 
                 description, 
                 modules=None, 
                 trigger=None, 
                 carryable=True):

        self.name = name
        self.description = description
        self.modules = modules
        self.trigger = trigger
        self.carryable = carryable

class Part(Item):
    super().__init__
    self.carryable = False

bicycle = Item('bicycle',
               'wheels, frame, handlebars: all beautiful.',
               [
drafthole = Item('drafthole','the drafthole is clear and free of detritus.',None,None)
bit = Item('bit','smooth and lustrous, the attention to detail to even the least significant parts makes this pipe impressive',[drafthole],None,False)
cornkernel = Item('kernel of corn','a small kernel of corn, blackened with soot and tar.')
pipebowl = Container("pipe bowl","the pipe bowl is charred with use.",cornkernel)
pipe = Item('ornate pipe','this pipe is hand-carved from the ivory of an african elephant. the smooth bit is made of some kind of dark wood.',[pipebowl,bit])
dresser = Item('Louis XIV dresser','this dresser hails from the french renaissance. it is carved from one piece of mahogany and is extremely heavy.',None,None,"That's far too heavy to pick up.")

