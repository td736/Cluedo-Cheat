from Player import Player



class Game():


    def __init__(self):
        
        self.confirmed = []
        self.remaining = ['mustard','plum','green','peacock',
                         'scarlet','white','knife','candlestick',
                         'pistol','poison','trophy','rope',
                         'bat','axe','dumbbell','hall',
                         'dining room','kitchen','patio',
                         'observatory','theatre',
                         'living room','spa','guest house']
        self.playerList = []
        self.own_cards = []
        ## move below to main
        #self.add_player(int(input("Number of players to be added: ")))


    def add_player(self, number):

        player1 = Player(input("Name of player 1: "))
        self.playerList.append(player1)
        
        player2 = Player(input("Name of player 2: "))
        self.playerList.append(player2)
        
        player3 = Player(input("Name of player 3: "))
        self.playerList.append(player3)

        if number > 3:
            player4 = Player(input("Name of player 4: "))
            self.playerList.append(player4)

        if number > 4:
            player5 = Player(input("Name of player 5: "))
            self.playerList.append(player5)


    def confirm_own_cards(self, number): ## add to all others_have lists

        for card in range(number):
            cardValue = input("Card value: ")
            self.own_cards.append(cardValue)
            self.remaining.remove(cardValue)


    def new_round(self, rumour): ## rumour = list of 3
        for player in self.playerList:
            player.get_name()
            action = input("Show, skip or unknown (sh, sk, u): ")

            if action == 'sh':
                player.show(rumour)
                
            elif action == 'sk':
                player.skip(rumour)
                
            elif action == 'u':
                continue
            

