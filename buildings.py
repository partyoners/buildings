
# class big_building:
#     def __init__ (self, height, width):
#         self.height = height
#         self.width = width

# bh = input("big building height? ")

# bw= input("big building width? (odd numbers only) ")

# big_building.height = int(bh)
# big_building.width = int(bw)

big = [i for i in range (0, 7)]#width of building
small = [o for o in range (0, 5)]

def big_building():
    t=1
    roof = ("__")
    
    for i in big:
        if i<5:#witdh of roof
            print(roof, end="")
            

    while t < 6:#height of building
        if t>0:
            print("\n")
        for i in big:
            x= ("__")
            y= ("|")
            if i%2==0:
                print(y, end="")
            else:
                print(x, end="")
        
        t = t+1
    print("\n")


def small_building():
    t=1
    roof = ("___")
    
    for o in small:
        if o<2:#witdh of roof
            print(roof, end="")
            

    while t < 4:#height of building
        if t>0:
            print("\n")
        for o in small:
            x= ("__")
            y= ("|")
            if o%2==0:
                print(y, end="")
            else:
                print(x, end="")
        
        t = t+1
    print("\n")

big_building()
small_building()


# make dictionary for the value of the height and length of both big and small building
#amend the numbers via an input and store in the dictionary

#make buildings, then add the bridge in

#make it so it prints a bridge 3 lines of 30 then lines of 5 with a space in the middle for example

#def square():
    #make square as big as you want. "-" = input(1), "-----" = input(5) etc.
    #sides = "|\n" = 1, 
#a=1
#b=2
#print('variable a is', 'even' if (a%2==0) else 'odd')