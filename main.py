#! /usr/bin/python3
import sys, math
from PIL import Image

image_offset = 1
n = 0
g = 0

def create_image(info):

    global image_offset
    global n
    global g

    cell_width = 15
    line_width = 2
    number_of_matrices_per_row = int(math.sqrt(len(info)))
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

    #LLENAMOS LAS MATRICES CON LOS RECUADROS ROJOS

    for i in range(0,number_of_matrices_per_row):

        for j in range(0,number_of_matrices_per_row):

            init_pos = 1
            start_x = (j*((cell_width*n)+line_width))+1
            start_y = (i*((cell_width*n)+line_width))+1
            c = 0

            for y in range(0,n-1):

                for x in range(init_pos,n):

                    for xx in range(start_x,start_x+(cell_width-2)):

                        for yy in range(start_y,start_y+(cell_width-2)):

                            if(info[(i*number_of_matrices_per_row)+j][c] == 1):
                                pix[(x*cell_width)+xx,(y*cell_width)+yy] = (255,0,0)

                    c += 1
                            

                init_pos += 1

            

    img.save("matrices_"+str(image_offset)+".png")
    img.show()
    image_offset += 1

def main():

    ok = False
    global n
    global g

    if len(sys.argv) > 1:

        n = int(sys.argv[1])
        g = int(sys.argv[2])

        if n%(g+1) != 0:
            print("It's not going to be optimal.")

        x = (n/(g+1))*((g*(g+1))/2)
        
        ok = True
        
    if ok:

        

        create_image([[0,1,1,1,0,0,1,0,1,0,0,0,0,1,1,1,0,0,1,0,1,0,0,0,0,1,1,1,0,0,1,0,1,0,0,0,1,1,1,0,0,1,0,1,0],[0,1,1,1,0,0,1,0,1,0,0,0,0,1,1,1,0,0,1,0,1,0,0,0,0,1,1,1,0,0,1,0,1,0,0,0,1,1,1,0,0,1,0,1,0],[0,1,1,1,0,0,1,0,1,0,0,0,0,1,1,1,0,0,1,0,1,0,0,0,0,1,1,1,0,0,1,0,1,0,0,0,1,1,1,0,0,1,0,1,0],[0,1,1,1,0,0,1,0,1,0,0,0,0,1,1,1,0,0,1,0,1,0,0,0,0,1,1,1,0,0,1,0,1,0,0,0,1,1,1,0,0,1,0,1,0]])


if __name__ == "__main__":
    main()
