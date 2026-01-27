from src.automaton import Automaton
from src.ScoreCard import ScoreCard

def test_hitting_pins_regular():
    automata = Automaton()
    pins = "12345123451234512345" # Total 60
    automata.set_input(ScoreCard(pins))
    assert automata.output() == 60

def test_symbol_zero():
    automata = Automaton()
    pins = "9-9-9-9-9-9-9-9-9-9-" # Total 90
    automata.set_input(ScoreCard(pins))
    assert automata.output() == 90

def test_spare_normal():
    automata = Automaton()
    # 5/ (10+5) + 5/ (10+5) ... = 150
    pins = "5/5/5/5/5/5/5/5/5/5/5" 
    automata.set_input(ScoreCard(pins))
    assert automata.output() == 150

def test_strike_normal():
    automata = Automaton()
    # X (10+9+0) + 9- (9) ...
    pins = "X9-9-9-9-9-9-9-9-9-" # Total 100
    automata.set_input(ScoreCard(pins))
    assert automata.output() == 100

def test_perfect_game():
    automata = Automaton()
    pins = "XXXXXXXXXXXX" # 12 strikes = 300
    automata.set_input(ScoreCard(pins))
    assert automata.output() == 300

def test_complex_game():
    # Caso complejo del archivo original
    automata = Automaton()
    pins = "8/549-XX5/53639/9/X" # Total 149
    automata.set_input(ScoreCard(pins))
    assert automata.output() == 149