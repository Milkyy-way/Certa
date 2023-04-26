import random as ran

DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
dice_height= len(DICE_ART[1])
dice_weidth= len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "

#generate a list for dice face
def dice_face_diagram_generator(dice_value):
    dice_face=[]
    for x in dice_value:
        dice_face.append(DICE_ART[x])
        
    dice_faces_rows = []
    for dice_row in range(dice_height):
        dice_set=[]
        for value in dice_face:
            dice_set.append(value[dice_row])
        raw_dice=DIE_FACE_SEPARATOR.join(dice_set)
        dice_faces_rows.append(raw_dice)
        
    width = len(dice_faces_rows[0])
    header="Result".center(width,"~")
    final_result="\n".join([header] + dice_faces_rows)
    return final_result       
            
def roll_dice(num_dice):
    roll_result=[]
    for _ in range(num_dice):
        roll = ran.randint(1,6)
        roll_result.append(roll)
    return (roll_result)


def parse_input(input_string):
    if input_string.strip() in {"1","2","3","4","5","6"}:
        return int(input_string)
    else:
        print("Please enter valid number between 1 to 6")
        #this will execute with exception and its code
        raise SystemExit(1)



#~~~~~~~~~ MAIN CODE BLOCK~~~~~~~~~~~~~~~~~~~~~

#Take user input
num_roll=input("How many dice do you want to roll? [0-6]")
#this parse input will take input as string and check if its valid integer and will return integer
num_dice = parse_input(num_roll)


roll_results = roll_dice(num_dice)

output=dice_face_diagram_generator(roll_results)
print(output)
