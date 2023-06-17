class Player:
    def __init__(self, name):
        self.name = name
        self.at_bats = 0
        self.hits = 0

    def record_hit(self):
        self.at_bats += 1
        self.hits += 1

    def record_out(self):
        self.at_bats += 1

    def calculate_batting_average(self):
        if self.at_bats > 0:
            average = self.hits / self.at_bats
            return round(average, 3)
        else:
            return 0.0


class BaseballTracker:
    def __init__(self):
        self.players = {}

    def add_player(self, player):
        self.players[player.name] = player

    def record_hit(self, player_name):
        if player_name in self.players:
            player = self.players[player_name]
            player.record_hit()
        else:
            print(f"Player '{player_name}' does not exist.")

    def record_out(self, player_name):
        if player_name in self.players:
            player = self.players[player_name]
            player.record_out()
        else:
            print(f"Player '{player_name}' does not exist.")

    def get_batting_average(self, player_name):
        if player_name in self.players:
            player = self.players[player_name]
            return player.calculate_batting_average()
        else:
            print(f"Player '{player_name}' does not exist.")


# Create baseball tracker instance
tracker = BaseballTracker()

# Create players
player1 = Player("John")
player2 = Player("Jane")

# Add players to the tracker
tracker.add_player(player1)
tracker.add_player(player2)

# Record hits and outs
tracker.record_hit("John")
tracker.record_out("John")
tracker.record_out("Jane")
tracker.record_hit("Jane")
tracker.record_hit("Jane")

# Get batting averages
john_average = tracker.get_batting_average("John")
jane_average = tracker.get_batting_average("Jane")

print("Batting Averages:")
print(f"John: {john_average}")
print(f"Jane: {jane_average}")

