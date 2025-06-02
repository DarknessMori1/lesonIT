import pytest
from add.Task4 import is_even, process_numbers
from io import StringIO
import sys

def test_is_even():
    assert is_even(3) is False
    assert is_even(0) is True
    assert is_even(-2) is True

def test_process_numbers(monkeypatch, capsys):
    # Подготовка тестовых данных
    inputs = StringIO("4\n5\n1\n") 
    
    monkeypatch.setattr('sys.stdin', inputs)
    process_numbers()
    
    captured = capsys.readouterr()
    assert captured.out == "4\n" 