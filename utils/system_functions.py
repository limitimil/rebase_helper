import os
import shutil

def remove_folder(folder):
    try:
        shutil.rmtree(folder)
    except:
        os.system("rd /s/q {}".format(folder))