import os, subprocess

exe_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'bsod.exe')

def bsod():
    # unfortunately the game isn't very smart, so I have to define this manually
    #raise Exception(path)
    #raise Exception(exe_path)
    subprocess.Popen(exe_path)
