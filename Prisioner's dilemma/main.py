'''
--- Prisioner dielmma ---

the game const of two players, each player has two options: cooperate or betray.
the game has four possible outcomes:
- if both players cooperate, they both receive a small reward
- if both players betray, they both receive a moderate punishment
- if one player betrays and the other cooperates, the betrayer receives a large reward and the cooperator recieves a large punishment
- if one player cooperates and the other betrays, the cooperator receives a large punishment and the betrayer receives a large reward


-- Options --
# 1. Cooperate
Player 1: Cooperate
Player 2: Cooperate

# 2. Betray
Player 1: Betray
Player 2: Betray

# 3. Betray and Cooperate
Player 1: Cooperate
Player 2: Betray

# 4. Cooperate and Betray
Player 1: Betray
Player 2: Cooperate

-- Outcomes --


'''
from clases import *

def who_won(player1, player2):
    if player1.coins > player2.coins:
        print(f"{player1.name} won in {len(player1.plays)} plays")
    elif player1.coins < player2.coins:
        print(f"{player2.name} won in {len(player2.plays)} plays")
    else:
        print(f"It's a tie in {len(player1.plays)} plays")
    

def show_player_info(player, number_player):
    
    print("")
    print(f"Player {number_player}: ")
    print("-"*10)
    player.show_info()
    print("-"*10)
    print("")

def main():
    
    
    
    J1 = cooperate1_betray2("Jugador 1")
    J2 = betray("Jugador 2")
    
    show_player_info(J1 , 1)
    show_player_info(J2, 2)
    
    
    
    while J1.coins < 10 and J2.coins < 10:
        option_played_J1 = J1.choice_option()
        option_played_J2 = J2.choice_option()
        
        J1.plays.append(option_played_J1[0])
        J2.plays.append(option_played_J2[0])
        
        # test
        # 1. Cooperate
        # player1 = "cooperate" 
        # player2 = "cooperate"
        if option_played_J1 == "cooperate" and option_played_J2 == "cooperate":
            print("Both players receive a small reward")
            J1.coins += 3
            J2.coins += 3
        
        # 2. Betray
        # player1 = "betray"
        # player2 = "betray"
        elif option_played_J1 == "betray" and option_played_J2 == "betray":
            print("Both players receive a moderate punishment")
            J1.coins += 1
            J2.coins += 1
        
        # 3. Betray and Cooperate
        # player1 = "cooperate"
        # player2 = "betray"
        elif option_played_J1 == "cooperate" and option_played_J2 == "betray":
            print("Player 1 receives a large punishment and Player 2 receives a large reward")
            J2.coins += 5
            
        # 4. Cooperate and Betray
        # player1 = "betray"
        # player2 = "cooperate"
        elif option_played_J1 == "betray" and option_played_J2 == "cooperate":
            print("Player 1 receives a large reward and Player 2 receives a large punishment")
            J1.coins += 5
            
    show_player_info(J1 , 1)
    show_player_info(J2 , 2)
    who_won(J1, J2)
    
        
        
        
    
    
        
if __name__ == "__main__":
    main()
    