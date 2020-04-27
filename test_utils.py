from utils.py import add, remove_spaces, validation_email
import pytest

@pytest.mark.parametrize('x, y, result', [
    (10,10,20),
    (15,15,30),
    (20,20,40),
    (5,5,10),
    (1.5, 1.5, 3)
])
def test_add(x, y, result):
    assert add(x, y) == result

@pytest.mark.parametrize('data, result', [
    ('john doe', 'johndoe'),
    (' ', ''),
    ('major   ', 'major'),
    ('abc abc   abc', 'abcabcabc')
])

def test_remove_spaces(data, result):
    assert remove_spaces(data) == result

@pytest.mark.parametrize('email, result', [
    ('asdasd@asd', True),
    ('sdfsdf', False),
    ('@mail.com', True)
])
def test_validation_email(email, result):
    assert validation_email(email) == result
