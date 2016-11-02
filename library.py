def biconvert(num):
    bi=""
    while num>=1:
        r=str(num%2)
        bi=bi+r
        num=num//2
    bi=int(bi[::-1])
    return bi

#the function for getting a munber (returning an error if it isnt a number in the paramiters)#
def getnum(minmax,minnum,maxnum): #function structure with internal variable names
    while True: #a loop that repeats till the correct input is given
        usr=input() #gets the supposesd number
        try: #--------------V
            usr=int(usr)#will try for if the number is an intiger
            if usr>=minnum and usr<=maxnum or minmax==False: #checks if its within the paramiters defined above
                break #this takes it out of the while loop only when the number is correctly inputted 
            else:
                print("invalid input")
        except: #if it is not an intiger will give out 'invalid input' and prompt for a retry of the intiger
            print("invalid input")
    return usr; #returns the inputted number
