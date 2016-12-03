import library as l

mem = []

'''visually printing the rectangle'''
def printr():
    print('how many rectangles would you like to print')
    count = l.getnum(True)
    for i in range(count):
        print("which rectangle would you like to print")
        t = l.getnum(False,0,len(mem)-1)
        mem[t].show()

'''removes a rectangle from the list'''
def delete():
    conf=["YES","NO"]
    print("how many rectagles would you like to delete")
    count = l.getnum(True)
    i=0
    while i < count:
        valid = False
        print("which rectangle would you like to delete")
        t = l.getnum(False,0,len(mem)-1)
        data(mem[t],mem)
        while valid == False:
            print("""are you sure you would like to delete this rectangle
(type exactly what is in the brackets)

({0[0]})--yes
({0[1]})---no
""".format(conf))
            s=input()
            for x in conf:
                if s == x:
                    valid = True
        
            if valid == True:
                if s == conf[0]:
                    mem.remove(mem[t])
                    i=i+1
                elif s == conf[1]:
                    print("please chose a different rectangle then")
            else:
                print("please give a valid input")

'''calls the function for creating rectangle(s)'''
def create():
    measurements=['length','hight']
    print('how many times do you want to create a rectangle')
    amount=l.getnum(True)
    for i in range(amount):
        re=[]
        for mes in measurements:
            print('what is the {0} of rectangle {1}'.format(mes,i))
            re.append(l.getnum(True))
        rectangle=l.Rectangle(re[0],re[1])
        mem.append(rectangle)

'''prints out the data for rectangles'''
def data(ob,li):
    print("----------------------------------")
    print("rectangle-{0}".format(li.index(ob)))
    print("length----{0}".format(ob.length))
    print("height----{0}".format(ob.height))
    print("area------{0}".format(ob.area))
    print("parimiter-{0}".format(ob.parimiter))
    print("----------------------------------")
   
def mod():
    print("WIP")

def load():
    accessing = True
    while accessing == True:
        file_name = input("file (.p at the end of the file)\n")
        try:
            with open(file_name,'rb') as use:
                test = l.pickle.load(use)
                print("loading these objects")
                for i in test:
                    data(i,test)
                    mem.append(i)
            accessing = False
        except FileNotFoundError:
            print("file doenst exist")

def save():
    accessing = True
    while accessing == True:
        file_name = input("file (.p at end of file name)\n")
        try:
            with open(file_name,'rb') as use:
                test = l.pickle.load(use)
                for i in test:
                    exist = False
                    for j in mem:
                        if i == j:
                            exist = True
                    
                    if exist != True:
                        mem.append(i)

            with open(file_name,'wb') as use:
                l.pickle.dump(mem,use)
            accessing = False
        except FileNotFoundError:
            print("creating new file")
            with open(file_name, 'wb') as use:
                l.pickle.dump(mem,use)
            accessing = False
        print("save compleate")

'''check rectangles'''
def check():
    print('\nthere are {0} rectangles\n'.format(len(mem)))
    running = True
    paramt = ["length","height","area","parimiter"]
    options = ['LENGTH','HEIGHT','AREA','PARIMITER','ALL','INDEX','BACK']
    while running == True:
        print("""what would you like to check
(type exactly what is in the brackets)

({0[0]})----details of all rectangles with a spesific {1[0]}
({0[1]})----details of all rectangles with a spesific {1[1]}
({0[2]})------details of all rectangles with a spesific {1[2]}
({0[3]})-details of all rectangles with a spesific {1[3]}
({0[4]})-------gives back the details of all the rectangles
({0[5]})-----give the details of a single rectangle
({0[6]})------go back to main menu
""".format(options,paramt))
        choice = input()
        valid = False
        for h in options:
            if h == choice:
                valid = True

        if valid == True:
            for y in range(len(paramt)):
                if choice == options[y]:
                    print("what is the {0} you would like to search for".format(paramt[y]))
                    inp = l.getnum(True)
                    for x in mem:
                        param = [x.length,x.height,x.area,x.parimiter]
                        if param[y] == inp:
                            data(x,mem)
            if choice == options[4]:
                for x in mem:
                    data(x,mem)
            elif choice == options[5]:
                print("what rectangle would you like to search for")
                inp = l.getnum(False,0,len(mem)-1)
                data(mem[inp],mem)
            elif choice == options[6]:
                running = exit()
        else:
            print("\nplease give a valid input\n")

def exit(): return False

'''the interface'''
def menu():

    funct = [create,check,delete,mod,printr,load,save]
    running = True
    options = ['CREATE','CHECK','DELETE','MOD','PRINT','LOAD','SAVE','EXIT']

    while running == True:
        print("""what would you like to do?
(type exactly what is in the brackets)

({0[0]})----create rectangles
({0[1]})-----check what rectangles exist
({0[2]})----delete existing rectangles
({0[3]})-------modify a rectangle
({0[4]})-----print out a pictute of the rectangle on the screen
({0[5]})------load a file of existing rectangles
({0[6]})------save the loaded rectangles to a file
({0[7]})------exit the program
""".format(options))
        choice = input()
        valid = False
        for h in options:
            if h == choice:
                valid = True

        if valid == True:
            fc=0
            for f in funct:
                if choice == options[fc]:
                    f()
                fc=fc+1
            if choice == options[7]:
                running = exit()
        else:
            print('\nplease give a valid input\n')

'''main program'''
if __name__ == '__main__':
    print("\nwelcome to rectangle\n")
    menu()
    print("\nthankyou for using this program\n")
