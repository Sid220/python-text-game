print("\nYou are alone in the frigged woods of a hidden country.\nYou where sent here by the CLIA (Central Linux Intelligence Authority) to find out about this new world.\nYou have a computer running Servbuntu v.0.0.1 with a IRC server which you plan to contact the CLIA with.\nIt is off\nThe night is getting colder and you need help")
def end_game(reason):
    exit(reason)
class q:
    def fasas():
        fasa = input("\nWhat would you like to do? [start a fire/turn on the computer]: ").lower()
        if(fasa == "start a fire"):
            print("\nYou look around and find no wood")
            q.knkls()
        elif(fasa == "turn on the computer"):
            print("\nThe computer is too cold to start\nYou have lost your last way to find help")
            end_game("You die of hypothermia")
        else:
            print("Command not understood!")
            q.fasas()
    def knkls():
        knkl = input("What would you like to do? [find wood/turn on the computer]: ").lower()
        if(knkl == "find wood"):
            print("\nYou walk into the forest bringing you computer with you\nEventually you find wood, but you also find a strange badge that looks simmilair to the following:")
            print("""           ,-~Â¨^  ^Â¨-,           _,
           /          / ;^-._...,Â¨/
          /          / /         /
         /          / /         /
        /          / /         /
       /,.-:''-,_ / /         /
       _,.-:--._ ^ ^:-._ __../
     /^         / /Â¨:.._Â¨__.;
    /          / /      ^  /
   /          / /         /
  /          / /         /
 /_,.--:^-._/ /         /
^            ^Â¨Â¨-.___.:^""")
            q.llls()
        elif(knkl == "turn on the computer"):
            print("\nThe computer is too cold to start\nYou have lost your last way to find help")
            end_game("You die of hypothermia")
        else:
            print("Command not understood!")
            q.knkls()
    def llls():
        lll = input("What would you like to do? [sus it out/take the wood]: ").lower()
        if(lll == "sus it out"):
            print("\nYou spend hours in a fruitless search and you are about to turn around when you see a logo:")
            print("""                        .8 
                      .888
                    .8888'
                   .8888'
                   888'
                   8'
      .88888888888. .88888888888.
   .8888888888888888888888888888888.
 .8888888888888888888888888888888888.
.&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%.
`%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%.
 `00000000000000000000000000000000000'
  `000000000000000000000000000000000'
   `0000000000000000000000000000000'
     `###########################'
       `#######################'
         `#########''########'
           `\"\"\"\"\"\"'  `\"\"\"\"\"\'""")
            q.sdfbs()
        elif(lll == "take the wood"):
            print("\nYou take the wood and successfully start a fire\nYou turn on the computer and make it back home safely.")
            end_game("The CLIA is very disappointed in you but at least you live to tell the tale.")
        else:
            print("Command not understood!")
            q.llls()
    def sdfbs():
        sdfb = input("What would you like to do? [continue search/go back]: ").lower()
        if(sdfb == "continue search"):
            print("\nYou continue your search until you find a corparate looking building bearing the flag of the first badge.")
            q.sutfs()
        elif(sdfb == "go back"):
            print("\nYou take the wood and successfully start a fire\nYou turn on the computer and make it back home safely.")
            end_game("The CLIA is very disappointed in you but at least you live to tell the tale.")
        else:
            print("Command not understood!")
            q.sdfbs()
    def sutfs():
        sutf = input("What would you like to do? [enter/go back]: ").lower()
        if(sutf == "enter"):
            end_game("You enter and immediately have all your rights and freedoms taken away.\nLike ruthless animals the employees enslave you and force you to develop their OS which in anti-trust levels they force people to use.")
        elif(sutf == "go back"):
            print("\nYou take the wood and successfully start a fire\nYou turn on the computer and make it back home safely.")
            end_game("The CLIA is very disappointed in you but at least you live to tell the tale.")
        else:
            print("Command not understood!")
            q.sutfs()
q.fasas()
