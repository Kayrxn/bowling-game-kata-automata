class ScoreCard:
    
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


    def score(self):
        total = 0
        roll_index = 0

        for frame in range(10):
            if roll_index >= len(self.rolls):
                break

            if self._is_strike(roll_index):
                total += 10 + self._strike_bonus(roll_index)
                roll_index += 1
            elif self._is_spare(roll_index):
                total += 10 + self._spare_bonus(roll_index)
                roll_index += 2
            else:
                # protección para listas incompletas
                first = self.rolls[roll_index]
                second = self.rolls[roll_index + 1] if roll_index + 1 < len(self.rolls) else 0
                total += first + second
                roll_index += 2

        return total


    def _is_strike(self, index):
        return self.rolls[index] == 10


    def _is_spare(self, index):
        return (index + 1) < len(self.rolls) and (self.rolls[index] + self.rolls[index + 1] == 10)


    def _strike_bonus(self, index):
        bonus = 0
        if index + 1 < len(self.rolls):
            bonus += self.rolls[index + 1]
        if index + 2 < len(self.rolls):
            bonus += self.rolls[index + 2]
        return bonus


    def _spare_bonus(self, index):
        return self.rolls[index + 2] if (index + 2) < len(self.rolls) else 0