import solve_2021_08 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
        "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
        "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
        "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
        "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
        "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
        "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
        "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
        "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
        "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        (
            (
                "be","cfbegad","cbdgef","fgaecd","cgeb","fdcge","agebfd","fecdb","fabcd","edb"
            ),
            (
                "fdgacbe","cefdb","cefbgd","gcbe"
            )
        ),
        (
            (
                "edbfga","begcd","cbg","gc","gcadebf","fbgde","acbgfd","abcde","gfcbed","gfec"
            ),
            (
                "fcgedb","cgb","dgebacf","gc"
            )
        ),
        (
            (
                "fgaebd","cg","bdaec","gdafb","agbcfd","gdcbef","bgcad","gfac","gcb","cdgabef"
            ),
            (
                "cg","cg","fdcagb","cbg"
            )
        ),
        (
            (
                "fbegcd","cbd","adcefb","dageb","afcb","bc","aefdc","ecdab","fgdeca","fcdbega"
            ),
            (
                "efabcd","cedba","gadfec","cb"
            )
        ),
        (
            (
                "aecbfdg","fbg","gf","bafeg","dbefa","fcge","gcbea","fcaegb","dgceab","fcbdga"
            ),
            (
                "gecf","egdcabf","bgf","bfgea"
            )
        ),
        (
            (
                "fgeab","ca","afcebg","bdacfeg","cfaedg","gcfdb","baec","bfadeg","bafgc","acf"
            ),
            (
                "gebdcfa","ecba","ca","fadegcb"
            )
        ),
        (
            (
                "dbcfg","fgd","bdegcaf","fgec","aegbdf","ecdfab","fbedc","dacgb","gdcebf","gf"
            ),
            (
                "cefg","dcbef","fcge","gbcadfe"
            )
        ),
        (
            (
                "bdfegc","cbegaf","gecbf","dfcage","bdacg","ed","bedf","ced","adcbefg","gebcd"
            ),
            (
                "ed","bcgafe","cdgba","cbgef"
            )
        ),
        (
            (
                "egadfb","cdbfeg","cegd","fecab","cgb","gbdefca","cg","fgcdab","egfdb","bfceg"
            ),
            (
                "gbdfcae","bgc","cg","cgb"
            )
        ),
        (
            (
                "gcafb","gcf","dcaebfg","ecagb","gf","abcdeg","gaef","cafbge","fdbac","fegbdc"
            ),
            (
                "fgae","cfgab","fg","bagce"
            )
        ),
    )

def test_count_digits_with_unique_number_of_segments(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.count_digits_with_unique_number_of_segments(data) == 26

def test_get_output(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.get_output(data[0]) == 8394
    assert subject.get_output(data[1]) == 9781
    assert subject.get_output(data[2]) == 1197
    assert subject.get_output(data[3]) == 9361
    assert subject.get_output(data[4]) == 4873
    assert subject.get_output(data[5]) == 8418
    assert subject.get_output(data[6]) == 4548
    assert subject.get_output(data[7]) == 1625
    assert subject.get_output(data[8]) == 8717
    assert subject.get_output(data[9]) == 4315


def test_output_sum(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.output_sum(data) == 61229
