class Game: #Defining Game class
    def __init__(self, id):
        self.p1Went = False #Checking if 1st player has made a move
        self.p2Went = False #Checking if 2nd player has made a move
        self.ready = False #If the players are ready
        self.id = id #Id of the game
        self.moves = [None, None] #Storing moves of players
        self.wins = [0,0]
        self.ties = 0

    def get_player_move(self, p): #Getting the move of the player
        return self.moves[p]

    def play(self, player, move): 
        self.moves[player] = move
        if player == 0:
            self.p1Went = True
        else:
            self.p2Went = True

    def connected(self):
        return self.ready

    def bothWent(self): #Checking is both made a move
        return self.p1Went and self.p2Went

    def winner(self):

        p1 = self.moves[0].upper()[0]
        p2 = self.moves[1].upper()[0]

        winner = -1

        #Rock Paper Scissors Logic
        if p1 == "R" and p2 == "S":
            winner = 0
        elif p1 == "S" and p2 == "R":
            winner = 1
        elif p1 == "P" and p2 == "R":
            winner = 0
        elif p1 == "R" and p2 == "P":
            winner = 1
        elif p1 == "S" and p2 == "P":
            winner = 0
        elif p1 == "P" and p2 == "S":
            winner = 1

        return winner
    

    def resetWent(self): #Resetting the moves
        self.p1Went = False
        self.p2Went = False