"""
Course: Introduction to Python Programming
Student Name: Sparsh Kumar
"""
#%% 
from random import randint


'''
Method: HumanPlayer
Parameter: GameRecord (the record of both players' choices and outcomes)
Return: ChoiceOfHumanPlayer, a string that can only be rock, paper, scissors, or quit
Description:
    This function asks the user to make a choice (i.e. input a string)
    This function will NOT return/exit until it gets a valid input from the user
    valid inputs are: rock or r, paper or p, scissors or s, game or g, quit or q
    quit means the user wants to quit the game
    game means the user wants to see the GameRecord
'''
def HumanPlayer(GameRecord):

    print(f"let's play ....................\n rock(r), paper(p), scissors(s) ?.\n or you want to see a record of the game (g) ? \n or you want to quit (q) ?.")
    ChoiceOfHumanPlayer = input("please make your choice now: ").lower().strip()
    if ChoiceOfHumanPlayer == "game" or ChoiceOfHumanPlayer == 'g':
        PrintGameRecord(GameRecord)
    elif ChoiceOfHumanPlayer in ["rock", "r", "paper", "p", "scissors", "s", "quit", "q"]:
        return ChoiceOfHumanPlayer
    else:
        print("The computer does not understand your input.")
    return HumanPlayer(GameRecord)


'''
Method: Computer Player
Parameter: GameRecord (the record of both players' choices and outcomes)
Return: ChoiceOfComputerPlayer, a string that can only be rock, paper, scissors
Description:
    ComputerPlayer will randomly make a choice
    ComputerPlayer should not look at the current choice of HumanPlayer
'''
def ComputerPlayer(GameRecord):

    ChoicesOfComputerPlayer = ["rock", "paper", "scissors"]
    return ChoicesOfComputerPlayer[randint(0, 2)]


'''
Method: Judge
Parameters:
    ChoiceOfComputerPlayer is a string from ComputerPlayer
    ChoiceOfHumanPlayer is a string from HumanPlayer
Return: Outcome
    Outcome is 0 if it is a draw/tie
    Outcome is 1 if ComputerPlayer wins
    Outcome is 2 if HumanPlayer wins
Description:
    this function determines the outcome of a game
'''
def Judge(ChoiceOfComputerPlayer, ChoiceOfHumanPlayer):

    outcome = None

    if ChoiceOfComputerPlayer == 'r':
        ChoiceOfComputerPlayer = 'rock'
    elif ChoiceOfComputerPlayer == 'p':
        ChoiceOfComputerPlayer = 'paper'
    elif ChoiceOfComputerPlayer == 's':
        ChoiceOfComputerPlayer = 'scissors'

    if ChoiceOfHumanPlayer == 'r':
        ChoiceOfHumanPlayer = 'rock'
    elif ChoiceOfHumanPlayer == 'p':
        ChoiceOfHumanPlayer = 'paper'
    elif ChoiceOfHumanPlayer == 's':
        ChoiceOfHumanPlayer = 'scissors'

    if ChoiceOfComputerPlayer == 'rock' and ChoiceOfHumanPlayer == 'scissors':
        outcome = 1
    elif ChoiceOfHumanPlayer == 'rock' and ChoiceOfComputerPlayer == 'scissors':
        outcome = 2
    elif ChoiceOfComputerPlayer == 'scissors' and ChoiceOfHumanPlayer == 'paper':
        outcome = 1
    elif ChoiceOfHumanPlayer == 'scissors' and ChoiceOfComputerPlayer == 'paper':
        outcome = 2
    elif ChoiceOfComputerPlayer == 'paper' and ChoiceOfHumanPlayer == 'rock':
        outcome = 1
    elif ChoiceOfHumanPlayer == 'paper' and ChoiceOfComputerPlayer == 'rock':
        outcome = 2
    elif ChoiceOfHumanPlayer == ChoiceOfComputerPlayer:
        outcome = 0
    return outcome


'''
Method: PrintOutcome
Parameters:
    Outcome is from Judge
    ChoiceOfComputerPlayer is a string from ComputerPlayer
    ChoiceOfHumanPlayer is a string from HumanPlayer
Return: None
Description:
    print Outcome, Choices and Players to the console window
    the message should be human readable
'''
def PrintOutcome(Outcome, ChoiceOfComputerPlayer, ChoiceOfHumanPlayer):

    winner = ''
    statement = ''
    if Outcome == 1:
        winner = 'Computer'
    elif Outcome == 2:
        winner = 'Human'
    if Outcome == 0:
        statement = f"It is a tie: "
    else:
        statement = f"{winner} wins: "

    if ChoiceOfHumanPlayer == 'p':
        ChoiceOfHumanPlayer = 'paper'
    elif ChoiceOfHumanPlayer == 'r':
        ChoiceOfHumanPlayer = 'rock'
    elif ChoiceOfHumanPlayer == 's':
        ChoiceOfHumanPlayer = 'scissors'

    if ChoiceOfComputerPlayer == 'p':
        ChoiceOfComputerPlayer = 'paper'
    elif ChoiceOfComputerPlayer == 'r':
        ChoiceOfComputerPlayer = 'rock'
    elif ChoiceOfComputerPlayer == 's':
        ChoiceOfComputerPlayer = 'scissors'

    statement = f"{statement} Computer chose {ChoiceOfComputerPlayer} {';' if Outcome else ''} Human chose {ChoiceOfHumanPlayer}"
    print (f"-----------------------------Outcome-----------------------------\n{statement}\n-----------------------------------------------------------------\n")


'''
Method: UpdateGameRecord
Parameters: 
    GameRecord is the record of both players' choices and and outcomes
    ChoiceOfComputerPlayer is a string from ComputerPlayer
    ChoiceOfHumanPlayer is a string from HumanPlayer
    Outcome is an integer from Judge
Return: None
Description:
    this function updates GameRecord, a list of three lists
'''
def UpdateGameRecord(GameRecord, ChoiceOfComputerPlayer, ChoiceOfHumanPlayer, Outcome):

    if ChoiceOfHumanPlayer == 'p':
        ChoiceOfHumanPlayer = 'paper'
    elif ChoiceOfHumanPlayer == 'r':
        ChoiceOfHumanPlayer = 'rock'
    elif ChoiceOfHumanPlayer == 's':
        ChoiceOfHumanPlayer = 'scissors'

    GameRecord.append([ChoiceOfComputerPlayer, ChoiceOfHumanPlayer, Outcome])


'''
Method: PrintGameRecord
Parameters: GameRecord (the record of both players' choices and outcomes)
Return: None
Description: this function prints the record of the game (see the sample run)
    the number of rounds. human wins x rounds. computer wins y rounds.
    the record of choices.
'''
def PrintGameRecord(GameRecord):

    ComputerWins = 0
    HumanWins = 0
    Tie = 0
    Details = 'Human, Computer\n'

    print (f"--------------Record of the Game--------------\n")
    print (f"The number of rounds is {len(GameRecord)}")

    for record in GameRecord:
        if record[2] == 1:
            ComputerWins = ComputerWins + 1
        elif record[2] == 2:
            HumanWins = HumanWins + 1
        elif record[2] == 0:
            Tie = Tie + 1
        Details = Details + record[0] + ',' + record[1] + "\n"
    print (f"Human wins {HumanWins} round (s).")
    print (f"Computer wins {ComputerWins} round (s).")
    print (f"Tie {Tie} round (s).")
    print (Details)
    print (f"-----------------------------------------------\n")


'''
Method: PlayGame
Description:
    This is the "main" function
    In this function, human and computer play the game until the human/user wants to quit
'''
def PlayGame():

    print("Welcome to rock-paper-scissors !")
    GameRecords = []
    while True:
        ChoiceOfHumanPlayer = HumanPlayer(GameRecords)
        if ChoiceOfHumanPlayer == 'q' or ChoiceOfHumanPlayer == 'quit':
            break;
        ChoiceOfComputerPlayer = ComputerPlayer(GameRecords)
        GameOutcome = Judge(ChoiceOfComputerPlayer, ChoiceOfHumanPlayer)
        if GameOutcome != None:
            UpdateGameRecord(GameRecords, ChoiceOfComputerPlayer, ChoiceOfHumanPlayer, GameOutcome)
            PrintOutcome(GameOutcome, ChoiceOfComputerPlayer, ChoiceOfHumanPlayer)
    print (f"-------------------Game Over-------------------\n")

if __name__ == '__main__':
    PlayGame()
