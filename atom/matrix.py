from neopixel import NeoPixel
from machine import Pin
from time import sleep

filled = [
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1]
    ]
BLANK = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    ]
star = [
    [1,0,1,0,1],
    [0,1,1,1,0],
    [1,1,1,1,1],
    [0,1,1,1,0],
    [1,0,1,0,1]
    ]
ONE = [
    [0,0,1,0,0],
    [0,1,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0]
    ]
TWO = [
    [0,0,1,0,0],
    [0,1,0,1,0],
    [0,0,1,0,0],
    [0,1,0,0,0],
    [0,1,1,1,0]
    ]
THREE = [
    [0,1,1,0,0],
    [0,0,0,1,0],
    [0,0,1,0,0],
    [0,0,0,1,0],
    [0,1,1,0,0]
    ]
FOUR = [
    [0,1,0,1,0],
    [0,1,0,1,0],
    [0,1,1,1,0],
    [0,0,0,1,0],
    [0,0,0,1,0]
    ]
FIVE = [
    [0,1,1,1,0],
    [0,1,0,0,0],
    [0,1,1,0,0],
    [0,0,0,1,0],
    [0,1,1,0,0]
    ]
SIX = [
    [0,0,1,0,0],
    [0,1,0,0,0],
    [0,0,1,0,0],
    [0,1,0,1,0],
    [0,0,1,0,0]
    ]
SEVEN = [
    [0,1,1,1,0],
    [0,0,0,1,0],
    [0,0,1,0,0],
    [0,1,0,0,0],
    [0,1,0,0,0]
    ]
EIGHT = [
    [0,0,1,0,0],
    [0,1,0,1,0],
    [0,0,1,0,0],
    [0,1,0,1,0],
    [0,0,1,0,0]
    ]
NINE = [
    [0,0,1,0,0],
    [0,1,0,1,0],
    [0,0,1,1,0],
    [0,0,0,1,0],
    [0,1,1,0,0]
    ]
ZERO = [
    [0,0,1,0,0],
    [0,1,0,1,0],
    [0,1,0,1,0],
    [0,1,0,1,0],
    [0,0,1,0,0]
    ]
A = [
    [0,0,1,0,0],
    [0,1,0,1,0],
    [0,1,1,1,0],
    [0,1,0,1,0],
    [0,1,0,1,0]
    ]
B = [
    [0,1,1,0,0],
    [0,1,0,1,0],
    [0,1,1,0,0],
    [0,1,0,1,0],
    [0,1,1,0,0]
    ]
C = [
    [0,0,1,0,0],
    [0,1,0,1,0],
    [0,1,0,0,0],
    [0,1,0,1,0],
    [0,0,1,0,0]
    ]
D = [
    [0,1,1,0,0],
    [0,1,0,1,0],
    [0,1,0,1,0],
    [0,1,0,1,0],
    [0,1,1,0,0]
    ]
E = [
    [0,1,1,1,0],
    [0,1,0,0,0],
    [0,1,1,0,0],
    [0,1,0,0,0],
    [0,1,1,1,0]
    ]
F = [
    [0,1,1,1,0],
    [0,1,0,0,0],
    [0,1,1,0,0],
    [0,1,0,0,0],
    [0,1,0,0,0]
    ]
G = [
    [0,0,1,0,0],
    [0,1,0,0,0],
    [0,1,1,1,0],
    [0,1,0,1,0],
    [0,0,1,1,0]
    ]
H = [
    [0,1,0,1,0],
    [0,1,0,1,0],
    [0,1,1,1,0],
    [0,1,0,1,0],
    [0,1,0,1,0]
    ]
I = [
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0]
    ]
J = [
    [0,1,1,1,0],
    [0,0,0,1,0],
    [0,0,0,1,0],
    [0,1,0,1,0],
    [0,1,1,0,0]
    ]
K = [
    [0,1,0,0,1],
    [0,1,0,1,0],
    [0,1,1,0,0],
    [0,1,0,1,0],
    [0,1,0,0,1]
    ]
L = [
    [0,1,0,0,0],
    [0,1,0,0,0],
    [0,1,0,0,0],
    [0,1,0,0,0],
    [0,1,1,1,0]
    ]
M = [
    [1,0,0,0,1],
    [1,1,0,1,1],
    [1,0,1,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1]
    ]
N = [
    [0,1,0,0,1],
    [0,1,0,0,1],
    [0,1,1,0,1],
    [0,1,0,1,1],
    [0,1,0,0,1]
    ]
O = [
    [0,0,1,1,0],
    [0,1,0,0,1],
    [0,1,0,0,1],
    [0,1,0,0,1],
    [0,0,1,1,0]
    ]
P = [
    [0,1,1,0,0],
    [0,1,0,1,0],
    [0,1,1,0,0],
    [0,1,0,0,0],
    [0,1,0,0,0]
    ]
Q = [
    [0,1,1,0,0],
    [1,0,0,1,0],
    [1,0,0,1,0],
    [1,0,1,1,0],
    [0,1,1,0,1]
    ]
R = [
    [0,1,1,0,0],
    [0,1,0,1,0],
    [0,1,1,0,0],
    [0,1,0,1,0],
    [0,1,0,1,0]
    ]
S = [
    [0,0,1,1,0],
    [0,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,0],
    [0,1,1,0,0]
    ]
T = [
    [0,1,1,1,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0]
    ]

U = [
    [0,1,0,1,0],
    [0,1,0,1,0],
    [0,1,0,1,0],
    [0,1,0,1,0],
    [0,1,1,1,0]
    ]
V = [
    [1,0,0,0,1],
    [1,0,0,0,1],
    [0,1,0,1,0],
    [0,1,0,1,0],
    [0,0,1,0,0]
    ]
W = [
    [1,0,0,0,1],
    [1,0,1,0,1],
    [1,0,1,0,1],
    [1,1,0,1,1],
    [1,0,0,0,1]
    ]
X = [
    [1,0,0,0,1],
    [0,1,0,1,0],
    [0,0,1,0,0],
    [0,1,0,1,0],
    [1,0,0,0,1]
    ]
Y = [
    [1,0,0,0,1],
    [0,1,0,1,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0]
    ]
Z = [
    [1,1,1,1,1],
    [0,0,0,1,0],
    [0,0,1,0,0],
    [0,1,0,0,0],
    [1,1,1,1,1]
    ]
alphabet = {
    "1": ONE,
    "2": TWO,
    "3": THREE,
    "4": FOUR,
    "5": FIVE,
    "6": SIX,
    "7": SEVEN,
    "8": EIGHT,
    "9": NINE,
    "0": ZERO,
    "*": star,
    " ": BLANK,
    "A": A,
    "B": B,
    "C": C,
    "D": D,
    "E": E,
    "F": F,
    "G": G,
    "H": H,
    "I": I,
    "J": J,
    "K": K,
    "L": L,
    "M": M,
    "N": N,
    "O": O,
    "P": P,
    "Q": Q,
    "R": R,
    "S": S,
    "T": T,
    "U": U,
    "V": V,
    "W": W,
    "X": X,
    "Y": Y,
    "Z": Z
}


class Color:
    RED = (10,0,0)
    GREEN = (0,10,0)
    BLUE = (0,0,10)
    
    WHITE = (10,10,10)
    ORANGE = (10,6,0)
    YELLOW = (10,10,0)
    ALL = [WHITE, RED, GREEN, BLUE, ORANGE, YELLOW]
    
    BLACK = (0,0,0)

    def dark(color):
        def darken(inp):
            return max(0, inp - 5)
        return darken(color[0]), darken(color[1]), darken(color[2])
    
    
    def get_all():
        return Color.ALL + [Color.dark(x) for x in Color.ALL]
    

def rotate_90(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]
    
def rotate_180(m):
    return [m[n] for n in range(len(m)-1, -1, -1)]
    
def rotate_270(m):
    return rotate_90(rotate_180(m))

class Matrix:
    def __init__(self, rotator=None):
        self.np = NeoPixel(Pin(27), 25)
        self.rotator = rotator
        
        self.btn = Pin(39, Pin.IN, Pin.PULL_UP)

    def wait_for_btn_pressed(self, seconds=60):
        poll_interval = 0.5
        time_left = seconds
        print("wait for btn")
        while time_left > 0:
            if self.btn.value() == 0:
                return True
            sleep(poll_interval)
            time_left -= poll_interval
        print("wait ended")
        return False


    def draw(self, matrix, color=(5,5,5), invert=False):
        if self.rotator:
            matrix = self.rotator(matrix)
        n=0
        background = Color.BLACK
        foreground = color
        if invert:
            background, foreground = foreground, background
        for line in matrix:
            for elem in line:
                if elem == 0:
                    self.np[n] = background
                else:
                    self.np[n] = foreground
                n+=1
        self.np.write()
    
    def draw_word(self, word, color=Color.WHITE, sleep_time=0.2, rotator=None):
        for char in word:
            #print(char)
            matrix = alphabet.get(char, [])
            try:
                if rotator:
                    matrix = rotator(matrix)
                self.draw(matrix, color=color)
                sleep(sleep_time)
            except Exception as e:
                print(e)
                print(matrix)
            
    def ticker(self, text):
        show_text = " "+text+" "
        end = 1
        while end < len(show_text):
            c1 = alphabet.get(show_text[end-1])
            c2 = alphabet.get(show_text[end])
            c = BLANK
            print(c1)
            print(c2)
            for row in range(5):
                print(row)
                c[row] = c1[row] + c2[row]
                
            for w in range(5):
                matrix = []
                for row in c:
                    matrix.append(row[w:w+5])
                print(matrix)
                self.draw(matrix)
                sleep(0.2)
            end +=1
    
    def fill(self, pixel_count, color=Color.WHITE):
        #print("fill " + str(pixel_count))
        for i in range(25):
            if i < (24-pixel_count):
                self.np[i] = Color.BLACK
                print("black " + str(i))
            else:
                self.np[i] = color
                print("color " + str(i))
            self.np.write()
    
    def clear(self):
        self.draw(filled, color=Color.BLACK)

    def blink(self, color=Color.WHITE, times=3, wait=0.1):
        self.clear()
        for i in range(times):
            self.draw(filled, color=color)
            sleep(wait)
            self.clear()
            sleep(wait)
        

def self_test():
    sleeper = 0.2
    m = Matrix()
    for key in sorted(alphabet.keys()):
        m.draw(alphabet.get(key))
        sleep(sleeper)
    for c in Color.ALL:
        m.blink(c)
    for i in range(26):
        m.fill(i)
        sleep(sleeper)
    m.clear()

    

def get_matrixes(input_str):
    mlist = []
    for c in input_str:
        mlist.append(alphabet.get(c, []))
    return mlist