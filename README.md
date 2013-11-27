# Adventure!
I decided I wanted to learn Python again, but this time, rather than follow
some dusty old tome desperate to teach me how best to perform mathematical
calculations, I decided I'd do it my own way, at my own pace -- and make it 
fun. 

So here we are. Adventure! A text adventure.

## What's the story?
I don't know yet. I'm writing the engine first; given that this is really
a coding exercise, I'm not terribly bothered about crafting a unique and
ingenious story. That said, I *am* writing something on the side in Inform
to show off the engine -- and provide an experience that isn't *completely*
terrible.

## TODO:
* Attach move function to Character class.
* Make a map class; instantiate Scenes from in there, like so:

<<<<<<< HEAD
       4--3
          |
    0--1--2--5

    class Map:
        layout = [
                  {'east':1}, # 0 // bedroom
                  {'east':2}, # 1 // landing
                  {'east':5,'north':3}, # 2 // hallway
                  {'south':2,'west':4}, # 3 // kitchen
                  {'east':3} // #4 lounge
                  {'west':2} // #5 front garden
                 ]
=======
           4--3
              |
        0--1--2--5

        class Map:
            layout = [
                       {'east':1}, # 0 // bedroom
                       {'east':2}, # 1 // landing
                       {'east':5,'north':3}, # 2 // hallway
                       {'south':2,'west':4}, # 3 // kitchen
                       {'east':3} // #4 lounge
                       {'west':2} // #5 front garden
                     ]
>>>>>>> master

        rooms = [Bedroom(Scene),Landing(Scene),Hallway(Scene),Kitchen(Scene),Lounge(Scene),FrontGarden(Scene)]
        
        def east(self, fromLocation=PLAYER.location)
            location = rooms.index(fromLocation)
            try:
                PLAYER.move(layout[location]['east'])
            except:
                print(Error().cantGoThatWayError())
    
* Write main loop.
* Split project into files.
* Read gameobject class definitions from json.

## What's next?
<<<<<<< HEAD
I don't know. A roguelike, maybe, or perhaps something more functional.
=======
I don't know. A roguelike, maybe, or perhaps something more functional. I'm considering looking at forking/threading.
>>>>>>> master
