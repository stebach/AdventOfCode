import solve_2015_05 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'ugknbfddgicrmopn',
        'aaa',
        'jchzalrnumimnmhp',
        'haegwjzuvuyypxyu',
        'dvszwmarrgswjxmb',
    ]


def test_three_vowels():
    assert subject.three_vowels('aei') == True
    assert subject.three_vowels('xazegov') == True
    assert subject.three_vowels('aeiouaeiouaeiou') == True
    assert subject.three_vowels('ugknbfddgicrmopn') == True
    assert subject.three_vowels('aaa') == True
    assert subject.three_vowels('jchzalrnumimnmhp') == True
    assert subject.three_vowels('haegwjzuvuyypxyu') == True
    assert subject.three_vowels('dvszwmarrgswjxmb') == False

def test_one_letter_twice():
    assert subject.one_letter_twice('xx') == True
    assert subject.one_letter_twice('xx') == True
    assert subject.one_letter_twice('aabbccdd') == True
    assert subject.one_letter_twice('ugknbfddgicrmopn') == True
    assert subject.one_letter_twice('aaa') == True
    assert subject.one_letter_twice('jchzalrnumimnmhp') == False
    assert subject.one_letter_twice('haegwjzuvuyypxyu') == True
    assert subject.one_letter_twice('dvszwmarrgswjxmb') == True

def test_does_not_contain_forbidden_strings():
    assert subject.does_not_contain_forbidden_strings('ugknbfddgicrmopn') == True
    assert subject.does_not_contain_forbidden_strings('aaa') == True
    assert subject.does_not_contain_forbidden_strings('jchzalrnumimnmhp') == True
    assert subject.does_not_contain_forbidden_strings('haegwjzuvuyypxyu') == False
    assert subject.does_not_contain_forbidden_strings('dvszwmarrgswjxmb') == True

def test_is_nice():
    assert subject.is_nice('ugknbfddgicrmopn') == True
    assert subject.is_nice('aaa') == True
    assert subject.is_nice('jchzalrnumimnmhp') == False
    assert subject.is_nice('haegwjzuvuyypxyu') == False
    assert subject.is_nice('dvszwmarrgswjxmb') == False

def test_count_nice(puzzle_input):
    assert subject.count_nice(puzzle_input) == 2

def test_two_letters_twice():
    assert subject.two_letters_twice('xyxy') == True
    assert subject.two_letters_twice('aabcdefgaa') == True
    assert subject.two_letters_twice('qjhvhtzxzqqjkmpb') == True
    assert subject.two_letters_twice('xxyxx') == True
    assert subject.two_letters_twice('uurcxstgmygtbstg') == True
    assert subject.two_letters_twice('ieodomkazucvgmuy') == False

def test_one_letter_twice_with_one_between():
    assert subject.one_letter_twice_with_one_between('xyx') == True
    assert subject.one_letter_twice_with_one_between('abcdefeghi') == True
    assert subject.one_letter_twice_with_one_between('qjhvhtzxzqqjkmpb') == True
    assert subject.one_letter_twice_with_one_between('xxyxx') == True
    assert subject.one_letter_twice_with_one_between('uurcxstgmygtbstg') == False
    assert subject.one_letter_twice_with_one_between('ieodomkazucvgmuy') == True

def test_is_nice2():
    assert subject.is_nice2('qjhvhtzxzqqjkmpb') == True
    assert subject.is_nice2('xxyxx') == True
    assert subject.is_nice2('uurcxstgmygtbstg') == False
    assert subject.is_nice2('ieodomkazucvgmuy') == False
    
