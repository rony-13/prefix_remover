import os

unwanted_portion = "y2mate.com - "

for filename in os.listdir("."):
    if filename.startswith(unwanted_portion):
        os.rename(filename, filename[len(unwanted_portion):])
