import pickle

'''converts base 10 to base 2'''
def dectobin(num):
    bi = "" #innitialises an empty srting to add binary digits to
    while num != 0: #repeats the appending process untill Num==0
        bi = bi + str(num % 2)#gets the remainder and puts it onto the end of the bi string
        num = num // 2#divides and rounds down num
    bi=int(bi[::-1]) #mirrors the bi string so that it reads correctly
    return bi #returnes an INT value of the binary number

'''is used to get an intiger and validate it'''
def getnum(pos = False , minnum = 0 , maxnum = 0): #function structure with internal variable names
    if minnum < maxnum:
        minmax = True
    else:
        minmax = False
    while True: #a loop that repeats till the correct input is given
        usr = input() #gets the supposesd number
        try: #--------------V
            usr = int(usr)#will try for if the number is an intiger
            if pos == True and usr > 0 or minmax==True and minnum <= usr and maxnum >= usr or pos == False and minmax == False: #checks if its within the paramiters defined above
                break #this takes it out of the while loop only when the number is correctly inputted 
            else:
                print("invalid input")
        except: #if it is not an intiger will give out 'invalid input' and prompt for a retry of the intiger
             print("invalid input")
    return usr #returns the inputted number

'''creats rectangles and allows them to be edited'''
class Rectangle:

    '''assigns instance vairables'''
    def __init__(self , length , height):
        self.length = length
        self.height = height
        self.area = self.length * self.height
        self.parimiter = self.length * 2 + self.height * 2

    '''changes length'''
    def change_length(self,newlength):
        self.length = newlength
        
    '''increases or decreases length'''
    def add_length(self,mod):
        self.length = self.length + mod
    
    '''multilpies length'''
    def multiply_length(self,mod):
        self.length = self.length * mod

    '''changes height'''
    def change_height(self,mod):
        self.height = mod

    '''increase or decreases height'''
    def add_height(self,mod):
        self.height = self.height + mod

    '''multiply height'''
    def multiply_height(self,mod):
        self.height = self.height * mod

    '''prints the rectangle'''
    def show(self):
        print('#' * self.length)
        for i in range(self.height - 1):
            if self.length == 1:
                print('#')
            else:
                print('#{0}#'.format(' ' *(self.length - 2)))
        if self.height != 1:
            print('#' * self.length)

