class CricketPlayer:
    def __init__(self,name,matches,runs,wickets):
        self.name=name
        self.matches=matches
        self.runs=runs
        self.wickets=wickets
        
    def addMatch(self,runs,wickets):
        self.matches+=1
        self.runs+=runs
        self.wickets+=wickets
        
    def battingaverage(self):
        average=self.runs/self.matches
        return average
        
    def allrounder(self):
        if self.runs > 1000 and self.wickets > 50:
            return True
        else:
            return False
            
    def display(self):
        return f"Name:{self.name} \n Matches:{self.matches}  \n Runs:{self.runs} \n Wickets:{self.wickets}"
        
player = CricketPlayer("Virat", 0, 0, 0)

player.addMatch(80, 1)
player.addMatch(120, 0)
player.addMatch(45, 2)

print(player.battingaverage())
print(player.allrounder())
print(player.display())