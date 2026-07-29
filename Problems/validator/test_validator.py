import pytest
from validator import check_password

def test_few_arguments():
    with pytest.raises(ValueError):
        check_password("gianijy")

def test_correct():
    assert check_password("gianijyp") == "gianijyp"
    assert check_password("1128003.") == "1128003." 