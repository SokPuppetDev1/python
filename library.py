#the function for converting base 10 to base 2
def dectobin(num):
    bi=""#innitialises an empty srting to add binary digits to
    while num!=0: #repeats the appending process untill Num==0
        bi=bi+str(num%2)#gets the remainder and puts it onto the end of the bi string
        num=num//2#divides and rounds down num
    bi=int(bi[::-1]) #mirrors the bi string so that it reads correctly
    return bi #returnes an INT value of the binary number

#the function for getting a munber (returning an error if it isnt a number in the paramiters)#
def getnum(minmax,minnum=0,maxnum=0): #function structure with internal variable names
    while True: #a loop that repeats till the correct input is given
        usr=input() #gets the supposesd number
        try: #--------------V
            usr=int(usr)#will try for if the number is an intiger
            if minmax==False or minmax==True and minnum<maxnum and minnum<=usr and maxnum>=usr: #checks if its within the paramiters defined above
                break #this takes it out of the while loop only when the number is correctly inputted 
            else:
                print("invalid input")
        except: #if it is not an intiger will give out 'invalid input' and prompt for a retry of the intiger
            print("invalid input")
    return usr; #returns the inputted number
