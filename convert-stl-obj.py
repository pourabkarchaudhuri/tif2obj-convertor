import trimesh
import os

# Set Filepath
FILE_NAME = "testing_groundtruth.stl"
macro_name = FILE_NAME.split('.')
EXPORT_FILENAME = macro_name[0] + ".obj"
INPUT_PATH = os.path.join(os.getcwd(), "output", "stl", FILE_NAME)
EXPORT_PATH = os.path.join(os.getcwd(), "output", "obj", EXPORT_FILENAME)

print("Converting to .obj")
mesh1 = trimesh.load(INPUT_PATH)
mesh2 = mesh1.copy()
mesh2.apply_scale(1.1)
mesh2.export(EXPORT_PATH)
print("Converstion completed from .stl to .obj")
print("File saved at {}".format(EXPORT_PATH))