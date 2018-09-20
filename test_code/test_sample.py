import sample

def test_answer_pass_failure():
    assert not sample.func(3) == 5

def test_answer_pass():
    assert sample.func(3) == 4    