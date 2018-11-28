"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Lara Peters.
"""
########################################################################
# Done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window =rg.TurtleWindow()
sally = rg.SimpleTurtle('turtle')
sally.pen = rg.Pen('green', 2)
sally.speed = 11
size = 134
for k in range (13):
    sally.draw_circle(size)
    sally.right(90)
    sally.forward(13)
    sally.left(90)


roger=rg.SimpleTurtle('turtle')
roger.pen = rg.Pen('blue',10)
roger.speed = 10
size = 180
for k in range (20):
    roger.draw_square(size)
    roger.right(90)
    roger.forward(10)
    roger.left(90)
    roger.pen_up()
    size = size-20
    roger.pen_down()


