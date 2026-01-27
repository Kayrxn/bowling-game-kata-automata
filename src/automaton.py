class Automaton:
    def __init__(self):
        self.rolls = []

    def set_input(self, score_card):
        self.rolls = score_card.rolls  #recibe el objeto scoreCard y extrae los lanzamientos que ya procesó

    def output(self):
        total_score = 0
        roll_index = 0
        #calcula la puntuación total recorriendo los 10 frames

        for frame in range(10):
            #protección por si la lista de rolls está incompleta
            if roll_index >= len(self.rolls):
                break

            if self._is_strike(roll_index):
                total_score += 10 + self.rolls[roll_index + 1] + self.rolls[roll_index + 2]
                roll_index += 1
            
            elif self._is_spare(roll_index):
                total_score += 10 + self.rolls[roll_index + 2]
                roll_index += 2
            
            else:
                total_score += self.rolls[roll_index] + self.rolls[roll_index + 1]
                roll_index += 2
        
        return total_score

    def _is_strike(self, roll_index):
        return self.rolls[roll_index] == 10