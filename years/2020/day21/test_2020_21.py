import solve_2020_21 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "mxmxvkd kfcds sqjhc nhms (contains dairy, fish)",
        "trh fvjkl sbzzf mxmxvkd (contains dairy)",
        "sqjhc fvjkl (contains soy)",
        "sqjhc mxmxvkd sbzzf (contains fish)",
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        (("mxmxvkd","kfcds","sqjhc","nhms"),("dairy","fish")),
        (("trh","fvjkl","sbzzf","mxmxvkd"),("dairy",)),
        (("sqjhc","fvjkl"),("soy",)),
        (("sqjhc","mxmxvkd","sbzzf"),("fish",)),
    )

def test_find_harmless_ingredients(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    harmless = subject.find_harmless_ingredients(data)
    assert len(harmless) == 5

def test_get_ordered_allergen_ingredients(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.get_ordered_allergen_ingredients(data) == 'mxmxvkd,sqjhc,fvjkl'
