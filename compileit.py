#!/usr/bin/env python

import os, sys

try: 
    os.makedirs("build")
except FileExistsError as e:
    pass

os.chdir("build")

detect_os = sys.platform;
if detect_os == "linux":
    if len(sys.argv) == 1:
        pass  # TODO no args --> compile everything
    else:
        for arg in sys.argv[1:]:
            if os.path.isfile("../" + arg):
                # create object files for argument source files
                os.system("g++ -c -std=c++17 -g -O3 -Wall ../" + arg);
            else:
                print("File " + arg + " does not exist.")

        obj_files = [f for f in os.listdir() if os.path.isfile(f)]
        compile_cmd = "g++ -std=c++17 -g -O3 -Wall -o ../exe "
        for o in obj_files:
            compile_cmd += o + " "
        os.system(compile_cmd);
else:
    print("Unsupported OS.")

os.chdir("..")