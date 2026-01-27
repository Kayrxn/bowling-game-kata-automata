class score_card:
    def __init__(self, score_string):
        self.string = score_string
        self.rolls = self._parse_rolls()

    def _parse_rolls(self):
        rolls = []
        for i, char in enumerate(self.string):
            if char == 'X':
                rolls.append(10)
            elif char == '-':
                rolls.append(0)
            elif char == '/':
                rolls.append(10 - rolls[-1])
            else:
                rolls.append(int(char))
        return rolls