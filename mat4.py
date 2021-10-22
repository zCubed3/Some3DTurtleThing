from vec3 import *
from vec4 import *
from constants import *
import math


class Mat4:
    row1: Vector4
    row2: Vector4
    row3: Vector4
    row4: Vector4


    def __init__(self):
        self.row1 = Vector4(1, 0, 0, 0)
        self.row2 = Vector4(0, 1, 0, 0)
        self.row3 = Vector4(0, 0, 1, 0)
        self.row4 = Vector4(0, 0, 0, 1)


    @staticmethod
    def mat4_rotate_x(x):
        mat4 = Mat4()

        mat4.row2 = Vector4(0, math.cos(x), -math.sin(x), 0)
        mat4.row3 = Vector4(0, math.sin(x), math.cos(x), 0)

        return mat4


    @staticmethod
    def mat4_rotate_y(y):
        mat4 = Mat4()

        mat4.row1 = Vector4(math.cos(y), 0, math.sin(y), 0)
        mat4.row3 = Vector4(-math.sin(y), 0, math.cos(y), 0)

        return mat4

    @staticmethod
    def mat4_rotate_z(z):
        mat4 = Mat4()

        mat4.row1 = Vector4(math.cos(z), -math.sin(z), 0, 0)
        mat4.row2 = Vector4(math.sin(z), math.cos(z), 0, 0)

        return mat4


    @staticmethod
    def translation(vec3: Vector3):
        mat = Mat4()
        mat.row4 = Vector4(vec3.x, vec3.y, vec3.z, 1)
        return mat


    @staticmethod
    def rotate(x, y, z):
        rot_x = Mat4.mat4_rotate_x(x * DEG_TO_RAD)
        rot_y = Mat4.mat4_rotate_y(y * DEG_TO_RAD)
        rot_z = Mat4.mat4_rotate_z(z * DEG_TO_RAD)

        return rot_x * rot_y * rot_z


    def perspective(self, fov_y: float, aspect: float, near_cull: float, far_cull: float):
        rad = (fov_y / 2.0) * DEG_TO_RAD

        y_scale = 1.0 / math.tan(rad)
        x_scale = y_scale / aspect
        comp = near_cull - far_cull

        self.row1 = Vector4(x_scale, 0.0, 0.0, 0.0)
        self.row2 = Vector4(0.0, y_scale, 0.0, 0.0)
        self.row3 = Vector4(0.0, 0.0, (far_cull + near_cull) / comp, -1.0)
        self.row4 = Vector4(0.0, 0.0, 2.0 * far_cull * near_cull / comp, 0.0)


    def mul_vec3(self, point: Vector3):
        reference = Vector3()

        reference.x = point.x * self.row1.x + point.y * self.row2.x + point.z * self.row3.x + self.row4.x
        reference.y = point.x * self.row1.y + point.y * self.row2.y + point.z * self.row3.y + self.row4.y
        reference.z = point.x * self.row1.z + point.y * self.row2.z + point.z * self.row3.z + self.row4.z

        w = point.x * self.row1.w + point.y * self.row2.w + point.z * self.row3.w + self.row4.w;

        if w != 1:
            reference.x /= w;
            reference.y /= w;
            reference.z /= w;

        return reference;


    def column1(self):
        return Vector4(self.row1.x, self.row2.x, self.row3.x, self.row4.x)


    def column2(self):
        return Vector4(self.row1.y, self.row2.y, self.row3.y, self.row4.y)


    def column3(self):
        return Vector4(self.row1.z, self.row2.z, self.row3.z, self.row4.z)


    def column4(self):
        return Vector4(self.row1.w, self.row2.w, self.row3.w, self.row4.w)


    def __mul__(self, rhs):
        final_mat = Mat4()

        final_mat.row1.x = (self.row1 * rhs.column1()).sum()
        final_mat.row1.y = (self.row1 * rhs.column2()).sum()
        final_mat.row1.z = (self.row1 * rhs.column3()).sum()
        final_mat.row1.w = (self.row1 * rhs.column4()).sum()

        final_mat.row2.x = (self.row2 * rhs.column1()).sum()
        final_mat.row2.y = (self.row2 * rhs.column2()).sum()
        final_mat.row2.z = (self.row2 * rhs.column3()).sum()
        final_mat.row2.w = (self.row2 * rhs.column4()).sum()

        final_mat.row3.x = (self.row3 * rhs.column1()).sum()
        final_mat.row3.y = (self.row3 * rhs.column2()).sum()
        final_mat.row3.z = (self.row3 * rhs.column3()).sum()
        final_mat.row3.w = (self.row3 * rhs.column4()).sum()

        final_mat.row4.x = (self.row4 * rhs.column1()).sum()
        final_mat.row4.y = (self.row4 * rhs.column2()).sum()
        final_mat.row4.z = (self.row4 * rhs.column3()).sum()
        final_mat.row4.w = (self.row4 * rhs.column4()).sum()

        return final_mat