import pytest
from grade import letter_grade


def test_score_error():
    with pytest.raises(TypeError):
        letter_grade("cat")

    with pytest.raises(ValueError):
        letter_grade(-1)
        
    with pytest.raises(ValueError):
        letter_grade(101)


def test_score_correct():
    assert letter_grade(90) == 'B'
    assert letter_grade(91) == 'A'
    assert letter_grade(80) == 'C'
    assert letter_grade(81) == 'B'
    assert letter_grade(70) == 'D'
    assert letter_grade(74) == 'C'
    assert letter_grade(79) == 'C'
    assert letter_grade(61) == 'D'
    assert letter_grade(60) == 'F'
    assert letter_grade(41) == 'F'