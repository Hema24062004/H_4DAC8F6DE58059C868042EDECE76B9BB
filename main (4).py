#define the base class player
class player:
  def play(self):
    print("the player is playing cricket.")

#define the derived class Batsman
class batsman(player):
  def play(self):
    print("the batsman is batting.")
    
#define the derived class Bowler
class bowler(player):
  def play(self):
      print("the bowler is bowling.")

#create objects of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

#call the play() method for each object
batsman.play()
bowler.play()