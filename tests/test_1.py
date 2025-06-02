import pytest
from add.Task1 import get_sq  

def test_square_positive():  
    assert get_sq(2) == 4    

def test_square_zero():
    assert get_sq(0) == 0   

def test_square_negative():
    assert get_sq(-3) == 9   