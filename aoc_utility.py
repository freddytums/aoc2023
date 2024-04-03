import os, sys, csv

def getPathOfPythonFile():
    path_of_python_file = sys.argv[0]
    return path_of_python_file

def ingestTextFile(filename):
    with open(filename) as f:
        input = f.readlines()
    return input

def outputTextFile(filename, output):
    with open(filename, 'w') as f:
        write = csv.writer(f, delimiter = '\n')
        write.writerow(output)
        f.close()