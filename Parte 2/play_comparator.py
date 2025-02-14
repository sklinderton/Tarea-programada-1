class play_comparator:
    def compare(self, a, b):
        if a._date < b._date:
            return -1
        elif a._date > b._date:
            return 1

        if a._quarter < b._quarter:
            return -1
        elif a._quarter > b._quarter:
            return 1

        if a._yards < b._yards:
            return -1
        elif a._yards > b._yards:
            return 1

        if a._time < b._time:
            return -1
        elif a._time > b._time:
            return 1

        return 0