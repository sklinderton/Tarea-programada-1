class punt_play:
    def __init__(self, game_id, teams, yards, quarter, date, time):
        self._game_id = game_id
        self._teams = teams  
        self._yards = float(yards) if yards else 0.0
        self._quarter = int(quarter) if quarter else 0
        self._date = date 
        self._time = time  

    def __str__(self):
        return f"{self._game_id},{self._teams},{self._yards},{self._quarter},{self._date},{self._time}"