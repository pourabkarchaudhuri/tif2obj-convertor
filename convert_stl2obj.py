import trimesh
import os
import time
start_time = time.time()

def convert(filename):
    # Set Filepath

    EXPORT_PATH = os.path.join(os.getcwd(), "output", "obj")

    if not os.path.exists(EXPORT_PATH):
            os.makedirs(EXPORT_PATH)

    INPUT_PATH = os.path.join(os.getcwd(), "output", "stl")
    start_time = time.time()
    

    MESH_PATH = os.path.join(INPUT_PATH, filename)

    print("Converting to .obj")

    mesh1 = trimesh.load(MESH_PATH)
    mesh2 = mesh1.copy()
    mesh2.apply_scale(0.4)

    macro_name = filename.split('.')
    output_name = macro_name[0] + ".obj"

    SAVE_PATH = os.path.join(EXPORT_PATH, output_name)

    mesh2.export(SAVE_PATH)

    print("File saved at {}".format(SAVE_PATH))
    execution_time = (time.time() - start_time)
    print("Export to .OBJ completed")
    print("OBJ Generation Execution time : {0:.2f}s".format(round(execution_time,2)))

    return output_name