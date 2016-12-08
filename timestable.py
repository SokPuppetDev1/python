################################## # # # # # # # # # # #
#this is the times table creator# # # # # # # # # # # # #
################################## # # # # # # # # # # # 

import library as l

##defined vairiables##

space=["   ","  "," ",""] #creats the space additions to make all the numbers 4 characters long

##getting inputs and user friendly outputs##

print("Welcome to the timestable generator.\nPlease input the 2 whole numbers bellow")
print("the first number cannot be higher than 99")
num1=l.getnum(1,99) #gets the ammount of rows
print("the second number cannot be higher than 45")
num2=l.getnum(1,45) #gets the amout of collums


##calculations and output##
for i in range(1,num1+1): #repeats for every row
    num=[] #the list of the numbers in the current row
    for j in range(1,num2+1): #repeats every number in the current row
        x=str(i*j) #gets the number that would be in said possition of the times table
        for h in range(4): #checks for how long the number is
            if len(x)==h+1: #-----^
                x=x+space[h] #adds amount of spaces depending on how long the number is
        num.append(x) #adds the number onto the end of the row
    num=str(num) #converts the entire row to a string
		########################################################################################
		#python is very good at string manipulation so thats why this next part is very usefull#
		########################################################################################
    num=num.replace('\', \'',' ')###
    num=num.replace('\']','')#######cleans it up so the row looks nice
    num=num.replace('[\'','')#######
    print(num) #prints the row
