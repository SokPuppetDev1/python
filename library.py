'''imports needed'''
#used for saving to an encoded format
import pickle


'''converts base 10 to base 2'''
def dectobin(num):
    bi = "" #innitialises an empty srting to add binary digits to
    while num != 0: #repeats the appending process untill Num==0
        #gets remainder and appends to end of bi string
        bi = bi + str(num % 2)
        num = num // 2 #divides and rounds down num
    bi = int(bi[::-1]) #mirrors the bi string so that it reads correctly
    return bi #returnes an INT value of the binary number


'''is used to get an intiger and validate it'''
def getnum(pos = False, minnum = 0, maxnum = 0):
    #this if statement ditermins if there is a minium and maximum number
    if minnum < maxnum: 
        minmax = True
        pos = False #minmax overrides pos
    else: minmax = False

    validating = True #used to check that 
    while validating == True: #loops till the correct input is given
        usr = input("-") #gets the supposesd number
        try: #--------------V
            usr = int(usr)#will try for if the input is an intiger
            #checks if the number is positive
            if pos == True and usr > 0 \
               #or it is between the range limit
               or minmax == True and minnum <= usr and maxnum >= usr \
               #or if its even checking for ether of them
               or pos == False and minmax == False:
                validating = False #used to exit the wile loop
            else: print("invalid input") #gives back 'invalid input' if the-
        except: print("invalid input") #input wasn't a number or too hight/low
    return usr #returns the inputted number if it has met the requirements


'''creats rectangles and allows them to be edited'''
class Rectangle:


    '''assigns instance vairables'''
    def __init__(self, length, height):
        self.length = length
        self.height = height
        self.area = self.length * self.height
        self.parimiter = self.length*2 + self.height*2


    '''changes length'''
    def change_length(self, mod): self.length = mod

        
    '''increases or decreases length'''
    def add_length(self, mod): self.length = self.length + mod

    
    '''multilpies length'''
    def multiply_length(self, mod): self.length = self.length * mod


    '''changes height'''
    def change_height(self, mod): self.height = mod


    '''increase or decreases height'''
    def add_height(self, mod): self.height = self.height + mod


    '''multiply height'''
    def multiply_height(self, mod): self.height = self.height * mod


    '''prints the rectangle'''
    def show(self):
        print('#' * self.length)
        for i in range(self.height - 1):
            if self.length == 1: print('#')
            else: print('#{0}#'.format(' ' * (self.length-2)))
        if self.height != 1: print('#' * self.length)

