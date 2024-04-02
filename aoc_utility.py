import os, sys

def getPathOfPythonFile():
    path_of_python_file = sys.argv[0]
    return path_of_python_file

def ingestTextFile(filename):
    with open(filename) as f:
        input = f.readlines()
    return input