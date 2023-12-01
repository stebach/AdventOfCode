import solve_2023_01 as subject
import pytest

def test_part_1_calibration_value():
    assert subject.get_calibration_value("1abc2") == 12
    assert subject.get_calibration_value("pqr3stu8vwx") == 38
    assert subject.get_calibration_value("a1b2c3d4e5f") == 15
    assert subject.get_calibration_value("treb7uchet") == 77

def test_part1_example1():
    puzzle_input = ["1abc2","pqr3stu8vwx","a1b2c3d4e5f","treb7uchet"]
    assert subject.part1(puzzle_input) == 142

def test_part_2_calibration_value():
    assert subject.get_calibration_value("two1nine") == 11
    assert subject.get_calibration_value("two1nine", True) == 29

    assert subject.get_calibration_value("eightwothree", True) == 83

    assert subject.get_calibration_value("abcone2threexyz") == 22
    assert subject.get_calibration_value("abcone2threexyz", True) == 13

    assert subject.get_calibration_value("xtwone3four") == 33
    assert subject.get_calibration_value("xtwone3four", True) == 24

    assert subject.get_calibration_value("4nineeightseven2") == 42
    assert subject.get_calibration_value("4nineeightseven2", True) == 42

    assert subject.get_calibration_value("zoneight234") == 24
    assert subject.get_calibration_value("zoneight234", True) == 14

    assert subject.get_calibration_value("7pqrstsixteen") == 77
    assert subject.get_calibration_value("7pqrstsixteen", True) == 76

    assert subject.get_calibration_value("one22one", True) == 11
    assert subject.get_calibration_value("two11two", True) == 22
    assert subject.get_calibration_value("three11three", True) == 33
    assert subject.get_calibration_value("four11four", True) == 44
    assert subject.get_calibration_value("five11five", True) == 55
    assert subject.get_calibration_value("six11six", True) == 66
    assert subject.get_calibration_value("seven11seven", True) == 77
    assert subject.get_calibration_value("eight11eight", True) == 88
    assert subject.get_calibration_value("nine11nine", True) == 99


def test_part2_example1():
    puzzle_input = ["two1nine","eightwothree","abcone2threexyz","xtwone3four","4nineeightseven2","zoneight234","7pqrstsixteen"]
    assert subject.part2(puzzle_input) == 281

