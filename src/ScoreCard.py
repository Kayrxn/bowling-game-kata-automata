class ScoreCard:
    
    #--------------------------------------------------------------------------
    #constructor que recibe una cadena de tiradas y la convierte en una lista de enteros para luego
    #--------------------------------------------------------------------------
    def __init__(self, score_string):
        self.string = score_string
        self.rolls = self._parse_rolls()


    #--------------------------------------------------------------------------
    #convierte la cadena de tiradas en una lista de enteros. Interpreta 'X' como 10, '-' como 0 y '/' como spare.
    #--------------------------------------------------------------------------

    def _parse_rolls(self):
        rolls = []
        for char in self.string:    #recorre cada carácter en la cadena de tiradas y lo convierte a su valor numérico correspondiente.
            if char == 'X':         #si el carácter es 'X', se interpreta como un strike y se agrega 10 a la lista de tiradas.
                rolls.append(10)
            elif char == '-':       #si el carácter es '-', se interpreta como una tirada sin bolos derribados y se agrega 0 a la lista de tiradas.
                rolls.append(0)
            elif char == '/':       #si el carácter es '/', se interpreta como un spare y se agrega a la lista de tiradas el número de bolos necesarios para completar 10 en el frame actual.
                rolls.append(10 - rolls[-1])
            else:                   #si el carácter es un número, se convierte a entero y se agrega a la lista de tiradas.
                rolls.append(int(char))
        return rolls


    #--------------------------------------------------------------------------
    #calcula la puntuación total del juego considerando strikes, spares y frames
    #--------------------------------------------------------------------------

    def score(self):
        total = 0
        roll_index = 0

        for _ in range(10):                     #se itera 10 veces (10 frames)

            if self._is_strike(roll_index):                     #si es un strike, se suma 10 más la bonificación de las siguientes dos tiradas.
                total += 10 + self._strike_bonus(roll_index)    #la bonificación de un strike se calcula sumando las siguientes dos tiradas.
                roll_index += 1
            elif self._is_spare(roll_index):                    #si es un spare, se suma 10 más la bonificación de la siguiente tirada.
                total += 10 + self._spare_bonus(roll_index)
                roll_index += 2
            else:                                               #si no es ni strike ni spare, se suman las dos tiradas del frame.

                first = self.rolls[roll_index]                                                      #la primera tirada del frame
                second = self.rolls[roll_index + 1] if roll_index + 1 < len(self.rolls) else 0      #la segunda tirada del frame, si existe
                total += first + second                                                             #se suman las dos tiradas del frame
                roll_index += 2

        return total


    #--------------------------------------------------------------------------
    #true si la tirada en 'index' es un strike (10 puntos).
    #--------------------------------------------------------------------------
    
    def _is_strike(self, index):
        return self.rolls[index] == 10  #un strike se representa con 'X' y se interpreta como 10 puntos.


    #true si las dos tiradas en el frame suman 10 (spare) y la segunda tirada existe.
    def _is_spare(self, index):
        return (index + 1) < len(self.rolls) and (self.rolls[index] + self.rolls[index + 1] == 10)  
    #retorna true si la suma de las dos tiradas del frame es igual a 10, por lo que es spare. 
    #y verifica que la segunda tirada exista para que no muera.


    #--------------------------------------------------------------------------
    #suma las dos tiradas siguientes para calcular la bonificación de un strike.
    #--------------------------------------------------------------------------

    def _strike_bonus(self, index):
        bonus = 0
        if index + 1 < len(self.rolls):         #si existe la siguiente tirada, se suma a la bonificación.
            bonus += self.rolls[index + 1]
        if index + 2 < len(self.rolls):         #si existe la segunda tirada después del strike, se suma a la bonificación.
            bonus += self.rolls[index + 2]
        return bonus


    #--------------------------------------------------------------------------
    #devuelve la siguiente tirada como bonificación de un spare, si existe.
    #--------------------------------------------------------------------------

    def _spare_bonus(self, index):
        return self.rolls[index + 2] if (index + 2) < len(self.rolls) else 0    #la bonificación de un spare es la siguiente tirada después del spare, si existe.