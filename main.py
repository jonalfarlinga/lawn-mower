# imports os, shutils, sched, time
from shutil import move  # noqa:F401
from os import listdir, path  # noqa:F401

# load sweep paths
'assume that script runs from home'
sweeps = [
    path.join("C:\\Users", "Public", "Desktop"),
    path.join("C:\\Users", "denni", "OneDrive", "Desktop")
]

# load dustbin path
dustbin = path.join("C:\\Users", "Public", "Dustbin")

# load ignores
ignores = []

print(listdir(sweeps[0]))
# while true
#   for each path in sweeps
for dir_path in sweeps:
    #   list items in sweep
    contents = listdir(dir_path)
    #   for each item in list
    for item in contents:
        #   move item from sweep to dustbin
        if item not in ignores:
            move(
                path.join(dir_path, item),
                dustbin
            )
#   schedule delay(10min)
