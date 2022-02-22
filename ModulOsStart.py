import os

Path = "/home/cq/ModulOsExercise"
print(Path)
Subfolder = ["Subfolder1", "Subfolder2", "Subfolder3", "Subfolder4", "Subfolder5"]
print(Subfolder[2])
for i in range(5):
    os.makedirs(os.path.join(Path, Subfolder[i]), exist_ok=True)
    # print(os.path.join(Path, Subfolder[i]))
