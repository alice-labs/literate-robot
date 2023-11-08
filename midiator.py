'''
The mediator pattern is a way of making different things talk to each other without knowing too much about each other. Imagine you have a bunch of friends who want to play a game together, but they don’t have each other’s phone numbers. How can they communicate and decide what game to play, where to meet, and when to start? One way is to use a mediator, which is someone who knows everyone’s phone numbers and can pass messages between them. The mediator can also help them agree on the rules of the game and make sure everyone is ready to play. The mediator is like a middleman who helps the friends coordinate their actions.

In Python, you can use the mediator pattern to create a class that acts as a mediator for other classes. For example, let’s say you have a class called Player that represents a friend who wants to play a game, and a class called Game that represents the game they want to play. The Player class has methods like join_game, send_message, and receive_message that allow it to interact with the game and other players. The Game class has methods like add_player, remove_player, broadcast_message, and start_game that allow it to manage the players and the game logic. The Mediator class is the one that connects the Player and Game classes and handles the communication between them.
'''


# The Mediator class that acts as a middleman between players and games
class Mediator:
    def __init__(self):
        self.players: Player = (
            {}
        )  # A dictionary that maps player names to player objects
        self.game = None  # The game object that the players want to play

    def register_player(self, player):
        # Add a player to the mediator and assign them a unique name
        name = f"Player {len(self.players) + 1}"
        self.players[name] = player
        player.name = name
        player.mediator = self
        print(f"{name} joined the mediator.")

    def register_game(self, game):
        # Set the game that the players want to play
        self.game = game
        game.mediator = self
        print(f"The game is set to {game.name}.")

    def relay_message(self, sender, message):
        # Relay a message from one player to another or to the game
        if message.startswith("@"):
            # The message is addressed to a specific player
            recipient_name = message.split()[0][
                1:
            ]  # Extract the name after the @ symbol
            if recipient_name in self.players:
                # The recipient is a valid player
                recipient = self.players[recipient_name]
                recipient.receive_message(sender, message)
            else:
                # The recipient is not a valid player
                print(f"{sender.name} sent an invalid message: {message}")
        else:
            # The message is addressed to the game
            self.game.receive_message(sender, message)


# The Player class that represents a friend who wants to play a game
class Player:
    def __init__(self):
        self.name = None  # The name of the player assigned by the mediator
        self.mediator: Mediator = None  # The mediator object that the player belongs to

    def join_game(self):
        # Join the game that the mediator has set
        if self.mediator and self.mediator.game:
            # The mediator and the game are valid
            self.mediator.game.add_player(self)
        else:
            # The mediator or the game are not valid
            print(f"{self.name} cannot join the game.")

    def send_message(self, message):
        # Send a message to another player or to the game through the mediator
        if self.mediator:
            # The mediator is valid
            self.mediator.relay_message(self, message)
        else:
            # The mediator is not valid
            print(f"{self.name} cannot send a message.")

    def receive_message(self, sender, message):
        # Receive a message from another player or from the game
        print(f"{self.name} received a message from {sender.name}: {message}")


# The Game class that represents the game that the players want to play
class Game:
    def __init__(self, name):
        self.name = name  # The name of the game
        self.mediator = None  # The mediator object that the game belongs to
        self.players = []  # A list of players who have joined the game
        self.started = (
            False  # A flag that indicates whether the game has started or not
        )

    def add_player(self, player):
        # Add a player to the game
        if not self.started:
            # The game has not started yet
            self.players.append(player)
            print(f"{player.name} joined the game {self.name}.")
        else:
            # The game has already started
            print(
                f"{player.name} cannot join the game {self.name} because it has already started."
            )

    def remove_player(self, player):
        # Remove a player from the game
        if not self.started:
            # The game has not started yet
            if player in self.players:
                # The player is in the game
                self.players.remove(player)
                print(f"{player.name} left the game {self.name}.")
            else:
                # The player is not in the game
                print(f"{player.name} is not in the game {self.name}.")
        else:
            # The game has already started
            print(
                f"{player.name} cannot leave the game {self.name} because it has already started."
            )

    def broadcast_message(self, message):
        # Broadcast a message to all players in the game
        for player in self.players:
            player.receive_message(self, message)

    def receive_message(self, sender, message):
        # Receive a message from a player in the game
        print(f"The game {self.name} received a message from {sender.name}: {message}")
        if message == "start":
            # The player wants to start the game
            self.start_game()
        elif message == "stop":
            # The player wants to stop the game
            self.stop_game()
        else:
            # The player sent an unknown message
            print(f"The game {self.name} does not understand the message: {message}")

    def start_game(self):
        # Start the game if there are enough players
        if len(self.players) >= 2:
            # There are enough players
            self.started = True
            self.broadcast_message("The game has started!")
        else:
            # There are not enough players
            print(
                f"The game {self.name} cannot start because there are not enough players."
            )

    def stop_game(self):
        # Stop the game if it has started
        if self.started:
            # The game has started
            self.started = False
            self.broadcast_message("The game has stopped!")
        else:
            # The game has not started
            print(f"The game {self.name} cannot stop because it has not started.")


# Create a mediator object
mediator = Mediator()

# Create four player objects and register them with the mediator
alice = Player()
bob = Player()
charlie = Player()
david = Player()
mediator.register_player(alice)
mediator.register_player(bob)
mediator.register_player(charlie)
mediator.register_player(david)

# Create a game object and register it with the mediator
tic_tac_toe = Game("Tic-Tac-Toe")
mediator.register_game(tic_tac_toe)

# Alice and Bob join the game
alice.join_game()
bob.join_game()

# Alice sends a message to Bob
alice.send_message("@Bob Hi, are you ready to play?")

# Bob sends a message to Alice
bob.send_message("@Alice Yes, I am ready.")

# Alice sends a message to the game to start it
alice.send_message("start")

# Charlie tries to join the game but fails because it has already started
charlie.join_game()

# David sends a message to Charlie
david.send_message("@Charlie Do you want to play another game?")

# Charlie sends a message to David
charlie.send_message("@David Sure, what game do you have in mind?")

# Bob sends a message to the game to stop it
bob.send_message("stop")

# Charlie and David join the game
charlie.join_game()
david.join_game()

# David sends a message to the game to start it
david.send_message("start")
