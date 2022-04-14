import random

class Character:

  def __init__(self, speed):
    self.speed = speed


class Item:

  def __init__(self, item_type, speed_change):
    self.item_type = item_type
    self.speed_change = speed_change


class Player:

  def __init__(self, name):
    self.name = name # save player's name
    self.speed = 0 # Player's speed
    self.round_speed = 0 # Player's speed after item
    self.play_records = [] # player records(seconds)


  def add_play_record(self, record_in_hr):
    
    record_in_sec = record_in_hr * 3600
    self.play_records.append(record_in_sec)
class Game:

  def __init__(self):
    self.num_rounds = 3
    self.player_list = [] 
    self.item_list = [] 
    self.character_list = []


  def set_players(self):
 
    i = 0
    while (i < 5):
        a = input("Name of Player" + str(i + 1))
        self.player_list.append(Player(a))
        i += 1
        


  def start_game(self):

    i = 0
    s = []
    while(i < 3):
        Character.speed = random.randint(100,180)
        self.character_list.append(Character.speed)
        i += 1

    w = 0
    i = 0
    while (w < 5):
        c = input(self.player_list[w].name + " turn to choose character. Choose from 1,2,3 ")
        if c == '1':
            print(self.player_list[w].name + " speed is "  + str(self.character_list[0]))
            self.player_list[w].speed = self.character_list[0]
            w += 1
            i += 1
        if c == '2':
            print(self.player_list[w].name + " speed is " + str(self.character_list[1]))
            self.player_list[w].speed = self.character_list[0]
            w += 1
            i += 1
        if c == '3':
            print(self.player_list[w].name + " speed is " + str(self.character_list[2]))
            self.player_list[w].speed = self.character_list[0]
            w += 1
            i += 1
    
        banana_slip = Item("banana_slip", random.randint(20, 40))
        booster = Item("booster", random.randint(30, 60))
        self.item_list.append("banana_slip")
        self.item_list.append("booster")
  def play_round(self):
      
    track = random.randint(5,30)
    print("Track length in this round is" + str(track))
    print("[Apply item]")
    i = 0
    while (i < 5):
        Itype = random.choice(self.item_list)
        if Itype == self.item_list[0]:
          drand = random.randint(-40,-20)
          self.player_list[i].round_speed =  self.player_list[i].speed + drand
          print("Player " + self.player_list[i].name + " speed is " + str(self.player_list[i].round_speed) + " due to banana_slip...")
          i += 1
        if Itype == self.item_list[1]:
          irand = random.randint(30, 60)
          self.player_list[i].round_speed = self.player_list[i].speed + irand
          print("Player " + self.player_list[i].name + " speed is " + str(self.player_list[i].round_speed) + " thanks to booster!!!")
          i += 1
      
    print("[Game in play...]")
    print("[Round result]")
    i = 0
    while i < 5:
      self.player_list[i].add_play_record(track / self.player_list[i].round_speed)
      l = len(self.player_list[i].play_records)
      print("Player " + self.player_list[i].name + " record: " + str(self.player_list[i].play_records[l - 1]))
      i += 1
              
        

  def game_result(self):
    i = 0
    sum_list = []
    sorted_list = []
    while i < 5:
      w =  0
      sum = 0
      while w < 3:
        sum += self.player_list[i].play_records[w]
        w += 1
      sum_list.append(sum)
      sorted_list.append(sum_list[i])

      i += 1
    sorted_list.sort()
    i = 0
    while i < 3:
      w = 0
      while w < 5:
        if sorted_list[i] == sum_list[w]:
          print(str(i+1) + " place " + str(self.player_list[w].name) + "(Track Time: " + str(sorted_list[i]) + "seconds)")
        w += 1
      i += 1
  def game(self):
   
    print("******************* Game Prep *******************")
    self.set_players()
    print()
    print("******************* Select Character *******************")
    self.start_game()
    print()
    print("******************* Game Start *******************")
    for i in range(3):
      print(f"============= ROUND {i+1} =============")
      self.play_round()
      print()
    print()

    print("******************* RESULTS *******************")
    self.game_result()
    



if __name__ == '__main__':
  game = Game()
  game.game()
