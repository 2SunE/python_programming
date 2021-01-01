from cs1robots import *

# 로봇이 있는 방
create_world()

# 처음 로봇이 가지고 있는 beepers 개수, 오른쪽을 보고 있는 hubo 생성
hubo = Robot(beepers= 1)

# 앞으로 한 칸씩 이동
hubo.move()
hubo.move()
hubo.move()
hubo.move()

# 왼쪽으로 방향 전환
hubo.turn_left()

# 위로 한 칸씩 이동
hubo.move()
hubo.move()
hubo.move()

# 오른쪽으로 방향 전환
def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

turn_right()

hubo.move()