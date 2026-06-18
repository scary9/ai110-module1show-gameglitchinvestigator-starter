from logic_utils import check_guess

#Default tests for check_guess function.
def _outcome_of(result):
    """Return the outcome string whether `check_guess` returns a tuple or a bare string."""
    return result[0] if isinstance(result, tuple) else result


def test_secret_max_with_nonmax_guess_is_too_low():
    """When the secret is the max value, a lower guess should be 'Too Low'."""
    outcome = _outcome_of(check_guess(99, 100))
    assert outcome == "Too Low"


def test_secret_min_with_nonmin_guess_is_too_high():
    """When the secret is the min value, a higher guess should be 'Too High'."""
    outcome = _outcome_of(check_guess(2, 1))
    assert outcome == "Too High"
