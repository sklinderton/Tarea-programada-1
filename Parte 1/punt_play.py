class punt_play:
    def __init__(self, game_id, teams, yards, quarter):
        self._game_id = game_id
        self._teams = teams  
        self._yards = float(yards) if yards else 0.0
        self._quarter = int(quarter) if quarter else 0

    def __eq__(self, other):
        if not isinstance(other, punt_play):
            return NotImplemented
        return self._yards == other._yards

    def __lt__(self, other):
        if not isinstance(other, punt_play):
            return NotImplemented
        return self._yards < other._yards

    def __gt__(self, other):
        if not isinstance(other, punt_play):
            return NotImplemented
        return self._yards > other._yards

    def __le__(self, other):
        if not isinstance(other, punt_play):
            return NotImplemented
        return self._yards <= other._yards

    def __ge__(self, other):
        if not isinstance(other, punt_play):
            return NotImplemented
        return self._yards >= other._yards

    def __str__(self):
        return f"{self._game_id},{self._teams},{self._yards},{self._quarter}"