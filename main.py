import numerics
import turtle
from datetime import datetime
import math
import obj
import time

perspective = numerics.Mat4()

perspective.perspective(45.0, 1.0, 0.001, 100.0)

model_matrix = numerics.Mat4()
last_time = time.perf_counter()

total_time = 0
time_scale = 1

test_model = obj.ObjModel("models/test.obj")

MATRIX_MODE = 1

if MATRIX_MODE:
    turtle.bgcolor(0, 0, 0)
    turtle.color("#00FF00")

turtle.hideturtle()
turtle.speed(0)
turtle.tracer(0, 0)
turtle.delay(0)

turtle.pensize(1)

while True:
    turtle.update()
    turtle.clear()

    cur_time = time.perf_counter()
    delta_time = cur_time - last_time

    trans = numerics.Mat4.translation(numerics.Vector3(0, 0, 5))
    #trans = numerics.Mat4.translation(numerics.Vector3(math.sin(total_time), math.cos(total_time), 5))
    rot = numerics.Mat4.rotate(math.cos(total_time) * 20, 180, math.sin(total_time) * 20)

    model_matrix = rot * trans

    last_time = cur_time
    total_time += delta_time * time_scale

    amount = 0
    for t in test_model.triangles:
        #if amount % 100 == 0:
        #    turtle.update()

        turtle.penup()
        #amount += 1

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