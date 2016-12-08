'''imports needed'''
import library as l


'''creating global vairables'''
mem = []
save_type = ".p"


'''visually printing the rectangle'''
def printr():
    print('how many rectangles would you like to print')
    count = l.getnum(True)
    for i in range(count):
        print("which rectangle would you like to print")
        t = l.getnum(False, 0, len(mem) - 1)
        mem[t].show()


'''removes a rectangle from the list'''
def delete():
    conf = ["YES", "NO"] 
    menu = """are you sure you would like to delete this rectangle
(type exactly what is in the brackets)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
({0[0]})--yes
({0[1]})---no
""".format(conf)
    print("how many rectagles would you like to delete")
    count = l.getnum(True)
    i = 0
    while i < count:
        print("which rectangle would you like to delete")
        t = l.getnum(False, 0, len(mem) - 1)
        data(mem[t], mem)
        usr = validate(conf, menu)
        if usr == conf[0]:
            mem.remove(mem[t])
            i += 1
        elif usr == conf[1]: print("please chose a different rectangle then")


'''calls the function for creating rectangle(s)'''
def create():
    measurements = ['length','hight']
    print('how many times do you want to create a rectangle')
    amount = l.getnum(True)
    x = len(mem)
    for i in range(amount):
        re = []
        for mes in measurements:
            print('what is the {0} of rectangle {1}'.format(mes, x + i))
            re.append(l.getnum(True))
        rectangle = l.Rectangle(re[0], re[1])
        mem.append(rectangle)


'''checking if an input is the same as an item in a list of objects'''
def validate(listx, text):
    validating = True
    print(text)
    while validating == True:
        usr = input("-")
        for x in listx:
            if usr == x: validating = False
        if validating == True: print("\nplease give a valid input\n")
    return usr                


'''prints out the data for rectangles'''
def data(ob, li):
    print("----------------------------------")
    print("rectangle-{0}".format(li.index(ob)))
    print("length----{0}".format(ob.length))
    print("height----{0}".format(ob.height))
    print("area------{0}".format(ob.area))
    print("parimiter-{0}".format(ob.parimiter))
    print("----------------------------------")
   

'''the function for modifying rectangles'''
def mod(): print("WIP")


'''checks for a certain save type at the end of the file'''
def file_type(t):
    is_type = False
    while is_type == False:
        usr = input("-")
        if usr.find(t, len(usr) - len(t)) != -1: is_type = True
        else: print("please put {0} at the end of the file name".format(t))
    return usr


'''loads a data from a file'''
def load():
    accessing = True
    while accessing == True:
        print("""please give a file name
({0} at the end of the file)
""".format(save_type))
        file_name = file_type(save_type)
        try:
            with open(file_name, 'rb') as use:
                loading = l.pickle.load(use)
                print("loading these objects")
                for i in loading:
                    data(i, loading)
                    mem.append(i)
            accessing = False
        except FileNotFoundError: print("file doenst exist")


'''saves the data to a file'''
def save():
    print("""please give a file name
({0} at the end of the file)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
##############################   
#THIS WILL OVERWRITE THE FILE#
##############################
""".format(save_type))
    file_name = file_type(save_type)
    with open(file_name, 'wb') as use: l.pickle.dump(mem, use)
    print("save compleate")


'''check rectangles'''
def check():
    print('\nthere are {0} rectangles\n'.format(len(mem)))
    running = True
    paramt = ["length", "height", "area", "parimiter"]
    options = ['LENGTH', 'HEIGHT', 'AREA',
               'PARIMITER', 'ALL', 'INDEX', 'BACK']
    menu = """what would you like to check
(type exactly what is in the brackets)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
({0[0]})----details of all rectangles with a spesific {1[0]}
({0[1]})----details of all rectangles with a spesific {1[1]}
({0[2]})------details of all rectangles with a spesific {1[2]}
({0[3]})-details of all rectangles with a spesific {1[3]}
({0[4]})-------gives back the details of all the rectangles
({0[5]})-----give the details of a single rectangle
({0[6]})------go back to main menu
""".format(options, paramt)
    validate(options, menu)
    for y in range(len(paramt)):
        if choice == options[y]:
            print("what is the {0} you would like to search for".format(
                  paramt[y]))
            inp = l.getnum(True)
            for x in mem:
                param = [x.length, x.height, x.area, x.parimiter]
                if param[y] == inp: data(x, mem)
    if choice == options[4]:
        for x in mem: data(x, mem)
    elif choice == options[5]:
        print("what rectangle would you like to search for")
        inp = l.getnum(False, 0, len(mem)-1)
        data(mem[inp], mem)
    elif choice == options[6]: running = exit()


'''the exit function'''
def exit(): return False


'''the interface'''
def menu():
    funct = [create, check, delete,
             mod, printr, load, save]
    running = True
    options = ['CREATE', 'CHECK', 'DELETE', 'MOD',
               'PRINT', 'LOAD', 'SAVE', 'EXIT']
    menu = """what would you like to do?
(type exactly what is in the brackets)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
({0[0]})----create rectangles
({0[1]})-----check what rectangles exist
({0[2]})----delete existing rectangles
({0[3]})-------modify the lengths and heights of a rectangle
({0[4]})-----print out a pictute of the rectangle on the screen
({0[5]})------load a file of existing rectangles
({0[6]})------save the loaded rectangles to a file
({0[7]})------exit the program
""".format(options)
    while running == True:
        choice = validate(options, menu)
        for f in funct:
            if choice == options[funct.index(f)]: f()
        if choice == options[7]: running = exit()


'''main program'''
if __name__ == '__main__':
    print("\nwelcome to rectangle\n")
    menu()
    print("\nthankyou for using this program\n")
