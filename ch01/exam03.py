# 휴보의 신문배달
from cs1robots import *

"""
문제의 개요
- 계단을 4칸 올라가기 > climb_up_four_stairs()
- 신문을 놓기 > hubo.drop_beeper()
- 돌아서기(180도) > turn_around()
- 계단을 4칸 내려가기 > climb_down_four_stairs()
"""

create_world()
hubo = Robot(beepers= 1)

def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

def climb_up_one_stair():
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.move()

for i in range (4):
    climb_up_one_stair()

hubo.move()
hubo.drop_beeper()

hubo.turn_left()
hubo.turn_left()

def climb_down_one_stairs():
    hubo.move()
    hubo.move()
    hubo.turn_left()
    hubo.move()
    turn_right()

for i in range(4):
    climb_down_one_stairs()

hubo.move()