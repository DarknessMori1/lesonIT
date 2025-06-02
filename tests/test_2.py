import pytest
from add.Task2 import is_triangle

def test_one():  
    assert is_triangle(3,3,3) == True    

def test_two():  
    assert is_triangle(1,2,3) == False    
    
def test_three():  
    assert is_triangle(1,3,1) == False    
