import solve_2015_11 as subject
import pytest

def test_string_to_password():
    assert subject.string_to_password('aaaaaa') == [97,97,97,97,97,97]
    assert subject.string_to_password('abcdef') == [97,98,99,100,101,102]

def test_password_to_string():
    assert subject.password_to_string([97,97,97,97,97,97]) == 'aaaaaa'
    assert subject.password_to_string([97,98,99,100,101,102]) == 'abcdef'


def test_increment_password():
    assert subject.password_to_string(subject.increment_password(subject.string_to_password('aaaaaa'))) == 'aaaaab'
    assert subject.password_to_string(subject.increment_password(subject.string_to_password('aaaazz'))) == 'aaabaa'

def test_validate_increasing_straight():
    assert subject.validate_increasing_straight(subject.string_to_password('hijklmmn')) == True
    assert subject.validate_increasing_straight(subject.string_to_password('abbceffg')) == False

def test_validate_no_forbidden_letters():
    assert subject.validate_no_forbidden_letters(subject.string_to_password('hijklmmn')) == False

def test_validate_two_pairs():
    assert subject.validate_two_pairs(subject.string_to_password('abbceffg')) == True
    assert subject.validate_two_pairs(subject.string_to_password('abbcegjk')) == False

def test_validate_password():
    assert subject.validate_password(subject.string_to_password('hijklmmn')) == False
    assert subject.validate_password(subject.string_to_password('abbceffg')) == False
    assert subject.validate_password(subject.string_to_password('abbcegjk')) == False
    assert subject.validate_password(subject.string_to_password('abcdffaa')) == True
    assert subject.validate_password(subject.string_to_password('ghjaabcc')) == True

def test_find_next_valid_password():
    assert subject.password_to_string(subject.find_next_valid_password(subject.string_to_password('abcdefgh'))) == 'abcdffaa'
    assert subject.password_to_string(subject.find_next_valid_password(subject.string_to_password('ghijklmn'))) == 'ghjaabcc'
