import random,sys
print("Welcome to Rock, Paper, Scissors!")
wins = 0
losses = 0      
ties = 0
while True:
    print('%s wins,%s losses, %s ties' %(wins,losses,ties))
    while True:
        print('Enter (r)ock,(p)aper, or (s)cissors or (q)uit:')
        playerMove = input().lower()
        if playerMove == 'q':
            print("Exiting the game.")
            sys.exit();
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        print("Enter r, p, s or q only.")
    if playerMove == 'r':
        print("Rock versus ....")
    elif playerMove == 'p':
        print("Paper versus ....")
    elif playerMove == 's':
        print("Scissors versus ....")
    computerMove = random.randint(1,3)
    if computerMove == 1:
        computerMove = 'r'
        print("Rock")
    elif computerMove == 2:
        computerMove = 'p'
        print("Paper")
    elif computerMove == 3:
        computerMove = 's'
        print("Scissors")
    if playerMove == computerMove:
        print("It is a tie!")
        ties += 1
    elif (playerMove == 'r' and computerMove == 's') or \
         (playerMove == 'p' and computerMove == 'r') or \
         (playerMove == 's' and computerMove == 'p'):
        print("You win!")
        wins += 1
    else:
        print("You lose!")
        losses += 1