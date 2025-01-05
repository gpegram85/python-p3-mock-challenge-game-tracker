class Game:

    all = []

    def __init__(self, title):
        
        # Validate title on initialization
        if not isinstance(title, str) or len(title) == 0:
            raise ValueError("Title must be a non-empty string.")
        
        # Use a private attribute to prevent modification
        self._title = title
        Game.all.append(self)

    @property
    def title(self):
        """Returns the game's title."""
        return self._title

    @title.setter
    def title(self, value):
        """Prevent modification of the title."""
        if hasattr(self, "_title"):
            raise AttributeError("Cannot modify title after instantiation.")
        self._title = value

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list({result.player for result in self.results()})

    def average_score(self, player):
        player_results = [result.score for result in self.results() if result.player == player]
        if not player_results:
            return 0
        return sum(player_results) / len(player_results)

class Player:
    def __init__(self, username):
        if not isinstance(username, str) or not (2 <= len(username) <= 16):
            raise ValueError("Username must be a string between 2 and 16 characters.")
        self.username = username

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Username must be a string between 2 and 16 characters.")
        self._username = value

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return list({result.game for result in self.results()})

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        return len([result for result in self.results() if result.game == game])

    @classmethod
    def highest_scored(cls, game):
        players_scores = {
            player: game.average_score(player) for player in {result.player for result in game.results()}
        }
        if not players_scores:
            return None
        return max(players_scores, key=players_scores.get)

class Result:
    all = []

    def __init__(self, player, game, score):
        if not isinstance(player, Player):
            raise ValueError("Player must be an instance of Player.")
        if not isinstance(game, Game):
            raise ValueError("Game must be an instance of Game.")
        if not isinstance(score, int) or not (1 <= score <= 5000):
            raise ValueError("Score must be an integer between 1 and 5000.")

        self._player = player
        self._game = game
        self._score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score

    @property
    def player(self):
        return self._player

    @property
    def game(self):
        return self._game