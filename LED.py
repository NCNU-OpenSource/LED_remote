import time

from PIL import Image
from PIL import ImageDraw

from Adafruit_LED_Backpack import Matrix8x8
import sys

# Create display instance on default I2C address (0x70) and bus number.
display = Matrix8x8.Matrix8x8()

# Alternatively, create a display with a specific I2C address and/or bus.
# display = Matrix8x8.Matrix8x8(address=0x74, busnum=1)

# Initialize the display. Must be called once before using the display.
display.begin()
# Set the alpha dictionary
# Run through each pixel individually and turn it on.
U=["11111100",
   "11111110",
   "00000011",
   "00000011",
   "00000011",
   "00000011",
   "11111110",
   "11111100"]
V=["11111000",
   "11111100",
   "00000110",
   "00000011",
   "00000011",
   "00000110",
   "11111100",
   "11111000"]
W=["11111111",
   "11111110",
   "00000100",
   "00011000",
   "00011000",
   "00000100",
   "11111110",
   "11111111"]
X=["10000001",
   "11000011",
   "11100111",
   "00111100",
   "00111100",
   "11100111",
   "11000011",
   "10000001"]
T=["11000000",
   "11000000",
   "11000000",
   "11111111",
   "11111111",
   "11000000",
   "11000000",
   "11000000"]
A=["00011111",
   "00111111",
   "01101100",
   "11001100",
   "11001100",
   "01101100",
   "00111111",
   "00011111"]
B=["11111111",
   "11111111",
   "10011001",
   "10011001",
   "10011001",
   "10011001",
   "01100110",
   "01100110"]
C=["00111100",
   "01111110",
   "10000001",
   "10000001",
   "10000001",
   "11000011",
   "01100110",
   "00100100"]
D=["11111111",
   "11111111",
   "11000011",
   "11000011",
   "11000011",
   "11000011",
   "01111110",
   "00111100"]
E=["11111111",
   "11111111",
   "10011001",
   "10011001",
   "10011001",
   "10011001",
   "10011001",
   "10011001"]
F=["11111111",
   "11111111",
   "11001100",
   "11001100",
   "11001100",
   "11001100",
   "11001100",
   "11001100"]
G=["00111100",
   "01111110",
   "11000011",
   "10000001",
   "10000001",
   "11001011",
   "01101110",
   "00101100"]
H=["11111111",
   "11111111",
   "00011000",
   "00011000",
   "00011000",
   "00011000",
   "11111111",
   "11111111"]
I=["00000000",
   "00000000",
   "11000011",
   "11111111",
   "11111111",
   "11000011",
   "00000000",
   "00000000"]
J=["00000000",
   "00000010",
   "11000011",
   "11000001",
   "11111111",
   "11111110",
   "11000000",
   "00000000"]
K=["11111111",
   "11111111",
   "00011000",
   "00011000",
   "00111100",
   "01100110",
   "11000011",
   "10000001"]
L=["10000011",
   "11111111",
   "11111111",
   "10000011",
   "00000011",
   "00000011",
   "00000011",
   "00000011"]

Y = ["10000000"
    ,"11000000"
    ,"11100001"
    ,"00011111"
    ,"00011111"
    ,"11100001"
    ,"11000000"
    ,"10000000"]
Z = ["11000011"
    ,"11000111"
    ,"11001111"
    ,"11001011"
    ,"10011011"
    ,"10110011"
    ,"11110011"
    ,"11000011"]
S = ["01100010"
    ,"10010001"
    ,"10010001"
    ,"10010001"
    ,"10001001"
    ,"10001001"
    ,"10001001"
    ,"01000110"]
R = ["11111111"
    ,"11111111"
    ,"11001000"
    ,"11001000"
    ,"11001100"
    ,"11011110"
    ,"01111011"
    ,"00110001"]
Q = ["00111100"
    ,"01111110"
    ,"11000011"
    ,"11000011"
    ,"11001011"
    ,"11000111"
    ,"01111110"
    ,"00111101"]
P = ["11111111"
    ,"11111111"
    ,"11001100"
    ,"11001100"
    ,"11001100"
    ,"11001100"
    ,"01111000"
    ,"00110000"]
O = ["00111100"
    ,"01111110"
    ,"11000011"
    ,"11000011"
    ,"11000011"
    ,"11000011"
    ,"01111110"
    ,"00111100"]
N = ["11111111"
    ,"11111111"
    ,"01100000"
    ,"00110000"
    ,"00011000"
    ,"00001100"
    ,"11111111"
    ,"11111111"]
M = ["11111111"
    ,"01111111"
    ,"00100000"
    ,"00011000"
    ,"00011000"
    ,"00100000"
    ,"01111111"
    ,"11111111"]
dot1=["00000000",
      "00000000",
      "00000000",
      "00001101",
      "00001110",
      "00000000",
      "00000000",
      "00000000"]
dot2=["00000000",
      "00000000",
      "00000000",
      "00000110",
      "00000110",
      "00000000",
      "00000000",
      "00000000"]
space=["00000000",
       "00000000",
       "00000000",
       "00000000",
       "00000000",
       "00000000",
       "00000000",
       "00000000"]

def show_alpha(element):
    if element == ' ':
        display.set_pixel(x, y,int(space[x][y]))
    if element == ',':
        display.set_pixel(x, y,int(dot1[x][y]))
    if element == '.':
        display.set_pixel(x, y,int(dot2[x][y]))
    if element == 'A':
        display.set_pixel(x, y,int(A[x][y]))
    if element == 'B':
        display.set_pixel(x, y,int(B[x][y]))
    if element == 'C':
        display.set_pixel(x, y,int(C[x][y]))
    if element == 'D':
        display.set_pixel(x, y,int(D[x][y]))
    if element == 'E':
        display.set_pixel(x, y,int(E[x][y]))
    if element == 'F':
        display.set_pixel(x, y,int(F[x][y]))
    if element == 'G':
        display.set_pixel(x, y,int(G[x][y]))
    if element == 'H':
        display.set_pixel(x, y,int(H[x][y]))
    if element == 'I':
        display.set_pixel(x, y,int(I[x][y]))
    if element == 'J':
        display.set_pixel(x, y,int(J[x][y]))
    if element == 'K':
        display.set_pixel(x, y,int(K[x][y]))
    if element == 'L':
        display.set_pixel(x, y,int(L[x][y]))
    if element == 'M':
        display.set_pixel(x, y,int(M[x][y]))
    if element == 'N':
        display.set_pixel(x, y,int(N[x][y]))
    if element == 'O':
        display.set_pixel(x, y,int(O[x][y]))
    if element == 'P':
        display.set_pixel(x, y,int(P[x][y]))
    if element == 'Q':
        display.set_pixel(x, y,int(Q[x][y]))
    if element == 'R':
        display.set_pixel(x, y,int(R[x][y]))
    if element == 'S':
        display.set_pixel(x, y,int(S[x][y]))
    if element == 'T':
        display.set_pixel(x, y,int(T[x][y]))
    if element == 'U':
        display.set_pixel(x, y,int(U[x][y]))
    if element == 'V':
        display.set_pixel(x, y,int(V[x][y]))
    if element == 'W':
        display.set_pixel(x, y,int(W[x][y]))
    if element == 'X':
        display.set_pixel(x, y,int(X[x][y]))
    if element == 'Y':
        display.set_pixel(x, y,int(Y[x][y]))
    if element == 'Z':
        display.set_pixel(x, y,int(Z[x][y]))
while True :
    if int(sys.argv[2])==1:
        for element in sys.argv[1].upper():
            display.clear()
            for x in range(8):
                for y in range(8):
                    show_alpha(element)
            display.write_display()
            time.sleep(0.9)
    elif int(sys.argv[2])==2:
        for element in sys.argv[1].upper():
            display.clear()
            for x in range(8):
                for y in range(8):
                    show_alpha(element)
                time.sleep(0.3)
                display.write_display()
    elif int(sys.argv[2])==3:
        for element in sys.argv[1].upper():
            display.clear()
            for x in range(8):
                for y in range(8):
                    show_alpha(element)
                    time.sleep(0.9)
            display.write_display()
    else:
        break
# Clear the display buffer.
display.clear()

# First create an 8x8 1 bit color image.
image = Image.new('1', (8, 8))

# Then create a draw instance.
draw = ImageDraw.Draw(image)

# Draw a rectangle with colored outline
#draw.rectangle((0,0,7,7), outline=255, fill=0)

# Draw an X with two lines.
#draw.line((0,0,7,7), fill=255)
#draw.line((0,7,7,0), fill=255)

mystr="abcde"

#for i in range(5)
#  if i
# Draw the image on the display buffer.
display.set_image(image)

# Draw the buffer to the display hardware.
display.write_display()

# See the SSD1306 library for more examples of using the Python Imaging Library
# such as drawing text: https://github.com/adafruit/Adafruit_Python_SSD1306
