#cluedo cheatculator

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

confirmed = []
remaining = ['mustard','plum','green','peacock',
             'scarlet','white','knife','candlestick',
             'pistol','poison','trophy','rope',
             'bat','axe','dumbbell','hall',
             'dining room','kitchen','patio',
             'observatory','theatre',
             'living room','spa','guest house']
pNames = {}
pList = []

class user():

    
    def __init__(self, pos, name):
        self.pos = pos
        self.name = name
        self.hnot = []
        self.has = []
        self.conf = []


    def details(self):
        print(str(self.pos) + ":" + str(self.name))


    def cards(self):
        print("Has: " + str(self.conf))
        print("Might have:  " + str(self.has))
        print("Doesn't have: " + str(self.hnot))
        

    
    def skip(self, rmra, rmrb, rmrc):

        self.hnot.append(rmra)
        self.hnot.append(rmrb)
        self.hnot.append(rmrc)
        self.hnot = set(self.hnot)
        self.hnot = list(self.hnot)


    def show(self, rmra, rmrb, rmrc):
        rmr = [rmra, rmrb, rmrc]
        self.has.append(rmr)

    def check(self):
        
        for lst in self.has:
            for item in lst:
                if item in self.hnot:
                    lst.remove(item)
            for item in lst:
                if item in self.hnot:
                    lst.remove(item)                    
            if len(lst) == 1:
                confirm(lst[0])
                self.conf.append(lst[0])
                self.has.remove(lst)
                    

def confirm(val):
    confirmed.append(val)
    for item in remaining:
        if val == item:
            remaining.remove(item)

    
def add_player(num):

    num = int(num)
    if num >= 3:
        global p1
        n1 = input("Name of player 1: ")
        p1 = user(1, n1)
        pNames["p1"] = n1
        pList.append(p1)
        
        global p2
        n2 = input("Name of player 2: ")
        p2 = user(2, n2)
        pNames["p2"] = n2
        pList.append(p2)
        
        global p3
        n3 = input("Name of player 3: ")
        p3 = user(3, n3)
        pNames["p3"] = n3
        pList.append(p3)
       
        
        if num >= 4:
            global p4
            n4 = input("Name of player 4: ")
            p4 = user(4, n4)
            pNames["p4"] = n4
            pList.append(p4)
            
            if num == 5:
                global p5
                n5 = input("Name of player 5: ")
                p5 = user(5, n5)
                pNames["p5"] = n5
                pList.append(p5)


def new_round(rmra, rmrb, rmrc):
    
    for player in pList:
        player.details()
        
        a = input("Show, skip or unknown(sh, sk, u): ")
        print(" ")
        
        if a == 'sh':
            player.show(rmra, rmrb, rmrc)
            player.check()
        elif a == 'sk':
            player.skip(rmra, rmrb, rmrc)
            player.check()
        elif a == 'u':
            continue



def main():

        pNum = input("Number of players(3 - 5 excluding self): ")
        add_player(pNum)
        
        numCard = int(input("How many cards are confirmed: "))
        
        for i in range(numCard):
            cVal = input("Card value: ")
            confirm(cVal)

        while len(remaining) != 3:
            choice = input("Next round(n), game info(p) or confirm(c): ")
            print("\n")
            if choice == 'n':
                per = input("Person: ")
                wep = input("Weapon: ")
                room = input("Room: ")
                new_round(per, wep, room)

            elif choice == 'p':
                for player in pList:
                    player.details()
                    player.cards()
                    print("\n")
                print("The remaining items are: " + str(remaining))
                print(" ")
                print("The confirmed items are: " + str(confirmed))
                print(" ")

            elif choice == 'c':
                cnfm = input("Enter a single value to be confirmed: ")
                confirm(cnfm)

            else:
                continue

        print("The answer is " + str(remaining))
        input("Enter any value to exit: ")

        
main()




