# player_name = "shebin"
# player_attack= 10
# player_heal= 16
# health= 100

# player =["shebin",10,16,100] ---list

player={"name":"shebin","attack":10,"heal": 16,"health":100}
monster={"name":"monster","attack":15,"health":110}

print(player['attack'])
print("please select action!")
print("1.attack")
print("2.heal !")
print("-------------------")

player_choice= input()
if player_choice == 1:
    print("attack")
    
else:
    pass 