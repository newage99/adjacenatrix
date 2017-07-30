#! /usr/bin/python3
from PIL import Image

def main():

    ok = False

    if len(sys.argv) > 2:

        n = int(sys.argv[1])
        g = int(sys.argv[2])

        if n%(g+1) == 0:
            print("OK!")
        
    if ok:

        
        

    img = Image.new('1', (100,100))
