#! /usr/bin/python3
import sys, math
from PIL import Image

def main():

    ok = False

    if len(sys.argv) > 1:

        n = int(sys.argv[1])
        g = int(sys.argv[2])

        if n%(g+1) != 0:
            print("It's not going to be optimal.")

        x = (n/(g+1))*((g*(g+1))/2)
        
        ok = True
        
    if ok:

        cell_width = 15
        line_width = 2
        number_of_matrices_per_row = 4
        px = (((n*cell_width)+line_width)*number_of_matrices_per_row)-line_width

        img = Image.new('RGB', (px,px))
        pix = img.load()

        #HACEMOS LAS LINEAS QUE SEPARAN LAS MATRICES
        pos = cell_width * n

        for i in range(0,number_of_matrices_per_row-1):

            for j in range(0,line_width):
                
                for t in range(0,px):

                    pix[pos+j,t] = (255,255,255)
                    pix[t,pos+j] = (255,255,255)

            pos += (cell_width*n) + line_width

        #HACEMOS LAS CASILLAS BLANCAS DE FONDO
        pos_x = cell_width
        pos_y = 0

        for i in range(0,number_of_matrices_per_row):

            for j in range(0,number_of_matrices_per_row):

                offset = 1

                for t in range(0,n-1):

                    for x in range(offset*cell_width,n*cell_width):

                        for y in range(0,cell_width):

                            pix[(i*((cell_width*n)+line_width))+x,(j*((cell_width*n)+line_width))+((t*cell_width)+y)] = (255,255,255)

                    offset += 1
                

        img.save("matrices.png")
        img.show()

        

        

        


if __name__ == "__main__":
    main()
