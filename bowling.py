from re import L


class Game:

    def __init__(self,frames=0,players=[]):
        self.frames = frames
        self.players = players

    def add_player(self,name,score=0):
        self.name = name
        self.score = score
        players.append(name)
        return self.players
    
    def frame(self,score1, score2):
        self.score1 = score1
        self.score2 = score2
        if self.score1 == 10:
            return "X"
        elif (self.score1 + self.score2) == 10:
            return "/"

class Frame:
    def __init__(self,balls):
         self.balls = balls
         # example: [3,7] is a spare
         # example: [10] is a strike

    def is_strike(self):
        return self.balls[0] == 10

    def is_spare(self):
        return len(self.balls >1 and self.balls[0] + self.balls[1] == 10)