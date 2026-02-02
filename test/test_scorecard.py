from src.ScoreCard import ScoreCard

def test_hitting_pins_regular():
    pins = "12345123451234512345" 
    assert ScoreCard(pins).score() == 60


def test_symbol_zero():
    pins = "9-9-9-9-9-9-9-9-9-9-"  
    assert ScoreCard(pins).score() == 90


def test_spare_normal():
    pins = "5/5/5/5/5/5/5/5/5/5/5"
    assert ScoreCard(pins).score() == 150


def test_strike_normal():
    # X (10+9+0) + 9- (9) ...
    pins = "X9-9-9-9-9-9-9-9-9-"  
    assert ScoreCard(pins).score() == 100


def test_perfect_game():
    pins = "XXXXXXXXXXXX"  
    assert ScoreCard(pins).score() == 300


def test_complex_game():
    # Caso complejo del archivo original
    pins = "8/549-XX5/53639/9/X" 
    assert ScoreCard(pins).score() == 149