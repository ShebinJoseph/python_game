# player_name = "shebin"
# player_attack= 10
# player_heal= 16
# health= 100

# player =["shebin",10,16,100] ---list


game_running = True

while game_running == True:
  
    new_round = True
    player={"name":"shebin","attack":10,"heal": 16,"health":100}
    monster={"name":"monster","attack":15,"health":110}
    while new_round == True:
        player_won = False
        monster_won = False

        print("please select action!")
        print("1.attack")
        print("2.heal")
        print("3.Exit Game")

        player_choice = input()
        if player_choice == "1":
             print("Attack")
             monster["health"] = monster["health"] - player["attack"]
             if monster["health"] <= 0:
                 player_won = True
             else:
                 player["health"]=player["health"] - monster["attack"]
                 print(monster["health"])
                 print(player["health"])
             if player["health"] <=0:
                 monster_won= True         
        
        elif player_choice =="2":
            print("heal the player")
        
        elif player_choice =="3":
            new_round = False
            game_running = False     
        
        else:
            print("Invalid input")
        
        if player_won == True or monster_won == True:
            new_round = False
                    