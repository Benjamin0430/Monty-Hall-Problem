import random

# Mounty Hall Definition:
# 1) A door set of size 3, one of them is the prize
# 2) Player picks one of the doors
# 3) Host reveals a door other than a) the prize b) player's pick
# 4) Player makes final decision a) stay with original choice b) switch to the other one

# Function Define:
# Parameter: True for staying, false for switching
# output: 1 for pick is the prize, 0 if not

def pick(switch = False):
    options = list(range(1, 3 + 1)) # A set of all possible choices for doors
    prize = random.randint(1, 3) # Set one of the door as the prize's door
    pick = random.randint(1, 3) # Set one of the door as the player's pick
    reveal = random.choice([n for n in options if ((n != prize) & (n != pick))]) # Host reveal a door other than the prize and the player's pick
    if (switch): # if the player decide to switch to the other choice
        pick = random.choice([n for n in options if ((n != pick) & (n != reveal))]) # switch the player's pick to the other choice
    if (pick == prize): # if the final pick is the prize
        return 1
    return 0 # if the final pick is not the prize
    
stay = 0 # cumulative success if the player decide to stay with the original choice
switch = 0 # cumulative success if the player decide to switch to another choice
for i in range (0,5000): # repeat the experiment 5000 time
    stay += pick() # keep track of the number of success if not switch
    switch += pick(True) # keep track of the number of success if switch
P_stay = stay/5000 * 100 # success rate if not switch
P_switch = switch/5000 * 100 # success rate if switch
print("You will have " + str(P_stay) + "% chance of winning if staying with original choice.") # 33.68%
print("You will have " + str(P_switch) +  "% chance of winning if switching to the other choice.") # 66.68%
