from Game import Game
from Player import Player

if __name__ == "__main__":
    ## Initializing game     ##
    game = Game()
    game.add_player(int(input("Number of players to be added: ")))
    game.confirm_own_cards(int(input("Number of known cards: ")))
    for item in game.own_cards:
        game.confirmed.append(item)
        
    for player in game.playerList:
        for item in game.own_cards:
            player.others_have.append(item)
    ## Initializing complete ## 

    while len(game.remaining) != 3:
        choice = input("Next round(n) or print game info(p): ")

        if choice == "n":
            rumour = [input("Item1: "), input("Item2: "), input("Item3: ")]
            game.new_round(rumour)
            for player in game.playerList:
                player.check()
            
        elif choice == "p":
            print("\n")
            for player in game.playerList:
                player.get_name()
                player.cards()
                print("\n")

            print("The remaining items are: " + str(game.remaining) + "\n")
            print("The confirmed items are: " + str(game.confirmed) + "\n")

        else:
            continue

    print("The answer is " + str(game.remaining))
    input("Enter any value to exit...")

