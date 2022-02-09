#Oskar Svedlund / Oliver Stafferöd
#TEINF-20
#2021-10-05
#Frankenstein spelet
#Monsters tale! 
 
Murder_instinkt = False 
Frankenstain = True
key = False
x = 1
 
input("""
Greetings player, please pay attention to this text as it explains how to play.
 
this game is a text only game where you play as frankenstein's monster.
The objektiv of the game is to make your own story by choosing what to do.
the options will be shown with a number attached to it, you are to only write the number which is shown next to the choices you want to perform.
also as you probably noticed no other text is shown, that's because you have to press a button for the next bit of text to show up, 
We did this so you have the time to read all of the text.
 
Now i have taken enough of your time, please enjoy teh game and press enter/any letter or whatever to start the game proper.
""")
 
input("""
You slowly came to consciousness as your body is animated,
You do not know where you are, you have no memories and are not waking up as much as being born.
 
feeling your body convulse and breathe in life for the first time you can do nothing but be still.
As you slowly open your eyes you see someone, a man dressed in a coat,
he looks at you with disgust and leaves the room in a panik through a door.
""")
 
choice_1 = input("""Time moves past and without knowing how long you have been laying on the table you woke up on.
You slowly stand up, looking around all you see are shadows in different shapes, something is wrong with your vision.
As you are struggling to stand up you have three things you can do. Follow the man in to the other room, wait where you are, 
or leave through the only other door in the room.
\n
1. Follow 
2. Wait 
3. Leave
""")
 



while (x == 1):
#----------------------------------------------------------------------------------------- 
    if choice_1 == "2":
        choice_1 = input("""You decide that the best course of action is to whait. 
        You wait, wait and wait. After what feels like a lifetime of whait you come 
        to the conclution that you shall wait no more.
        What will you do?
        1. Follow.
        2. ...
        3. Leave.
        """)
    
    if choice_1 == "1":
        input("""You decide to follow the man with the cloak.
        You see the door he went trough, and when you press yourself against the door,
        it opens for you too see directly in front of you a window looking over a forest
        you find him, lying in a bead surrounded with draperies.
        """)
 
        choice_2 = input("""
        The man you saw when you first opened your eyes lies before you unconscious on a bed before you,
        what do you do? 
        1. Wake him up 
        2. Watch 
        3. Kill him
        """)
        if choice_2 == "1":
            
            Woke = input("""
            As you stretch your arm to lighty nudge him he wakes up before you touch him, 
            he notice you and you see terror spread in his eyes as he frantically jumps out of bed then runs out the door. 
            What do you do
            1. Go out the same door 
            2. wait
            """)
 
            if Woke == "1":
                choice_1 = input("""
                You decide to go out the same door as the man, you follow him for a while but soon you loose sight of him.  
                After a bit of wandering around you eventualy end upp before what seems like the door that leads outside.
                You dicide to leave.
                3. Leave
                """)
                key = True
 
 
        if choice_2 == "3" or "2":
            choice_1 = input("""
            You start watching this man sleep. It you start getting a calm feeling just sitting there.
            You try to caress him but as soon as your hand hovers above him, suddenly his eyes open and he jolt up frightening you.
            Not knowing what to do you feel an instinct to grab his neck.
            Uppon grabing this mans throat you suddenly hear a noticeble "CRACK!", uppon this sound you notice
            that the man has suddenly gone limp. On the night counter you find a key. 
            It must be the key that lets you exit the building.
            With the key in hand you dicide to leave.
            3. Leave
            """)
            Frankenstain = False
            Murder_instinkt = True
            key = True
#------------------------------------------------------------ 
 
 
    if choice_1 =="3":
 
        print("You approach the other door in the room \n")
 
        if key == False: input("as you try to open it you are met with a door as solid and unmoving as the wall it's surrounded by ")
        elif key == True: input("The door open upp before you. You take your first stepp outside and feel the fresh air in your lungs for the firtst time in your life")
        
 


    else:
        choice_1 = input("""
        You decide to stand up to explore your surroundings
        You stand in the middle of a dark room only lit by faint candle light.
        As far as you can see, you have three options, 
        1. follow 
        2. wait 
        3. leave 
        """)
    
 
 
 
print("""
 You exit the building feeling the fresh air against your bare skin. 
""")
 
village_1 = input("In the dark you approach a lonely village in the forest. You have to make a choice(ignore, approach): ")
 
if village_1 == "ignore":
    print("""You decided that approaching the village would be too much trubble so you decide to leave. 
    But just as you enter the forest again some humans exit the forest. Now wanting to be seen you are forced towards the village""")
 
elif village_1 == "approach":
    print("This tiny village intrigues you so you decide to approach it")
 
print(""" 
You are standing between 2 houses in the dark village. From this place you can see a few people wandering about in the village.
""")
 
if Murder_instinkt == True:
    village_2 = input("""
    For some reason you come to remember the first human you saw. The man that created you and how it felt as the life quickly drained 
    out of his body after you grabbed him. The slight sense of pride clouds your mind.
    You feel a slight burning inside you, a burning desire to take the life out of these homans also.
    But yet you hesitate, is it ok for you to kill? What will you choose?(rampage, approach, ...):
    """)
 
if Murder_instinkt == False:
    village_2 = input("""
    Något fint.
    """)
 
 
 
 
 
 
#remember to use:
# def scene_1():
