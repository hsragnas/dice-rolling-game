import random

dice_art = {
    1: [
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
    ],
    2: [
        "┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"
    ],
    3: [
        "┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"
    ],
    4: [
        "┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"
    ],
    5: [
        "┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"
    ],
    6: [
        "┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘"
    ]
}

def display_dice(dice_values):
    dice_to_display = [dice_art[value] for value in dice_values]
    

    for line in range(5):  
        for die in dice_to_display:
            print(die[line], end="  ")
        print()  

def roll_dice():
    """Main dice rolling function"""
    print("\n🎲 Dice Rolling Game 🎲")
    
    while True:
        try:
            num_of_dice = int(input("\nHow many dice to roll? (1-5, 0 to quit): "))
            
            if num_of_dice == 0:
                print("\nThanks for playing!")
                break
                
            if num_of_dice < 1 or num_of_dice > 5:
                print("Please enter a number between 1 and 5")
                continue
                
            dice = [random.randint(1, 6) for _ in range(num_of_dice)]
            total = sum(dice)
            
            print("\nYour roll:")
            display_dice(dice)
            print(f"\nTotal: {total}")
            
        
            if num_of_dice == 2 and dice[0] == dice[1]:
                print("🎉 Doubles!")
            elif all(val == dice[0] for val in dice):
                print("🔥 Yahtzee! All dice match!")
                
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    roll_dice()