import numerics
import turtle
from datetime import datetime
import math
import obj

perspective = numerics.Mat4()

perspective.perspective(45.0, 1.0, 0.001, 100.0)

points = [
    numerics.Vector3(0, 0, 1),  # 0
    numerics.Vector3(-1, 0, 1), # 1
    numerics.Vector3(-1, 1, 1), # 2
    numerics.Vector3(0, 1, 1),  # 3
    numerics.Vector3(0, 0, 2),  # 4
    numerics.Vector3(-1, 0, 2), # 5
    numerics.Vector3(-1, 1, 2), # 6
    numerics.Vector3(0, 1, 2)   # 7
]

indices = [
    0, 2, 1,
    0, 3, 2,

    3, 5, 6,
    3,
]

model_matrix = numerics.Mat4()
last_time = datetime.now()

total_time = 0
time_scale = 1

test_model = obj.ObjModel("models/test.obj")

turtle.speed(100)
turtle.tracer(0, 0)
while True:
    turtle.update()

    turtle.clear()
    cur_time = datetime.now()

    diff_time = (last_time - cur_time).microseconds
    delta_time = diff_time / 1000000.0

    trans = numerics.Mat4.translation(numerics.Vector3(math.sin(total_time), math.cos(total_time), 5))
    rot = numerics.Mat4.rotate(total_time, total_time, total_time)

    model_matrix = rot * trans

    last_time = cur_time
    total_time += delta_time * time_scale

    for t in test_model.triangles:
        turtle.penup()

        #if amount % 100 == 0:
        #    turtle.update()

        for i in t:
            try:
                reference = model_matrix.mul_vec3(test_model.points[i])

                final = perspective.mul_vec3(reference)
                final.scale(300)

                turtle.goto((final.x, final.y))
                turtle.pendown()

            except Exception as E:
                print(E)


turtle.done()