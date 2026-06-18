from logic_utils import check_guess

#FIX: Created tests for check_guess function to ensure the bounds are correct using agent mode.
def _outcome_of(result):
    # Support both return styles: either a string outcome or (outcome, message)
    return result[0] if isinstance(result, tuple) else result


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    outcome = _outcome_of(result)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    outcome = _outcome_of(result)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    outcome = _outcome_of(result)
    assert outcome == "Too Low"
