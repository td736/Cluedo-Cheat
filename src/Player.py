



class Player():


    def __init__(self, name):
        
        self.name = name
        self.doesnt_have = []
        self.might_have = []
        self.others_have = []
        self.has = []


    def get_name(self):
        print(self.name)


    def cards(self):
        print("Has: %s" % self.has)
        print("Might have: %s" % self.might_have)
        print("Doesn't have: %s" %self.doesnt_have)

    """
    Rumour(R) is a list containing the three items that were asked about this round.
    self.skip()  Adds any element in R that isn't already in doesnt_have(DH) to DH, keeping dh as a list of unique elements. Then calls self.check()
    self.show()  Removes any elements from R that are in DH. If R contains one item, adds it to has(H), else, adds R to might_have(MH)
    self.check() Looks through the items of list in MH and removes the item if also in DH. Moves lists that contain a single item from MH to H
    """
    def skip(self, rumour):                 
        for element in range(len(rumour)):
            if rumour[element] not in self.doesnt_have:
                self.doesnt_have.append(rumour[element])
        self.check()


    def show(self, rumour):
        count = 0
        while count < len(rumour):
            if rumour[count] in self.doesnt_have or rumour[count] in self.others_have:
                rumour.pop(count)
            else:
                count += 1
                
        if len(rumour) == 1:
            self.has.append(rumour[0])

        else:
            self.might_have.append(rumour)


    def check(self):
        for lst in self.might_have:
            for item in lst:
                if item in self.doesnt_have or item in self.others_have:
                    lst.remove(item)
            if len(lst) == 1:
                self.has.append(lst[0])
                self.might_have.remove(lst)
            



