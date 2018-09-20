# content of test_sample.py
import sample_code

def test_answer_fail(): # Fail
    assert not sample_code.func(3) == 5

def test_answer_pass(): # Pass
    assert sample_code.func(4) == 5