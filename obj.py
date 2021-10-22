import vec3

class ObjModel:
    points = []
    triangles = []


    def __init__(self, file_path):
        file = open(file_path)

        while True:
            line = file.readline()

            if not line:
                break

            if line.startswith("v "):
                numbers_only = line.replace("v ", "")
                numbers_only = numbers_only.replace("\n", "")

                numbers = numbers_only.split(" ")

                self.points.append(vec3.Vector3(float(numbers[0]), -float(numbers[1]), float(numbers[2])))

            if line.startswith("f "):
                numbers_only = line.replace("f ", "")
                numbers_only = numbers_only.replace("\n", "")

                faces = numbers_only.split(" ")

                triangle = []
                for face in faces:
                    indices = face.split("/")
                    triangle.append(int(indices[0]) - 1)

                self.triangles.append(triangle)