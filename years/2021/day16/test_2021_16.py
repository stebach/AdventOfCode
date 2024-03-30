import solve_2021_16 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "D2FE28"
    ]

@pytest.fixture
def puzzle_input2():
    return [
        "38006F45291200"
    ]

@pytest.fixture
def puzzle_input3():
    return [
        "EE00D40C823060"
    ]

@pytest.fixture
def puzzle_input4():
    return [
        "8A004A801A8002F478"
    ]

@pytest.fixture
def puzzle_input5():
    return [
        "A0016C880162017C3686B18A3D4780"
    ]

@pytest.fixture
def puzzle_input6():
    return [
        "C200B40A82"
    ]

@pytest.fixture
def puzzle_input7():
    return [
        "04005AC33890"
    ]

@pytest.fixture
def puzzle_input8():
    return [
        "880086C3E88112"
    ]

@pytest.fixture
def puzzle_input9():
    return [
        "CE00C43D881120"
    ]

@pytest.fixture
def puzzle_input10():
    return [
        "D8005AC2A8F0"
    ]

@pytest.fixture
def puzzle_input11():
    return [
        "F600BC2D8F"
    ]

@pytest.fixture
def puzzle_input12():
    return [
        "9C005AC2F8F0"
    ]

@pytest.fixture
def puzzle_input13():
    return [
        "9C0141080250320F1802104A08"
    ]

def test_parse_lines(puzzle_input, puzzle_input2, puzzle_input3):
    assert subject.parse_lines(puzzle_input) == [1,1,0,1,0,0,1,0,1,1,1,1,1,1,1,0,0,0,1,0,1,0,0,0]
    assert subject.parse_lines(puzzle_input2) == [0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1,0,1,0,0,0,1,0,1,0,0,1,0,1,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0]
    assert subject.parse_lines(puzzle_input3) == [1,1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0]

def test_parse_code(puzzle_input, puzzle_input2, puzzle_input3):
    data = subject.parse_lines(puzzle_input)
    data2 = subject.parse_lines(puzzle_input2)
    data3 = subject.parse_lines(puzzle_input3)
    assert subject.parse_code(data) == {
        'version': 6,
        'type': 4,
        'sub': [],
        'value': 2021
    }

    assert subject.parse_code(data2) == {
        'version': 1,
        'type': 6,
        'sub': [
            {
                'version': 6,
                'type': 4,
                'sub': [],
                'value': 10
            },
            {
                'version': 2,
                'type': 4,
                'sub': [],
                'value': 20
            }
        ],
        'value': None
    }

    assert subject.parse_code(data3) == {
        'version': 7,
        'type': 3,
        'sub': [
            {
                'version': 2,
                'type': 4,
                'sub': [],
                'value': 1
            },
            {
                'version': 4,
                'type': 4,
                'sub': [],
                'value': 2
            },
            {
                'version': 1,
                'type': 4,
                'sub': [],
                'value': 3
            }
        ],
        'value': None
    }

def test_sumup_version_numbers(puzzle_input4, puzzle_input5):
    data4 = subject.parse_code(subject.parse_lines(puzzle_input4))
    data5 = subject.parse_code(subject.parse_lines(puzzle_input5))
    assert subject.sumup_version_numbers(data4) == 16
    assert subject.sumup_version_numbers(data5) == 31

def test_calc_value(puzzle_input6, puzzle_input7, puzzle_input8, puzzle_input9, puzzle_input10, puzzle_input11, puzzle_input12, puzzle_input13):
    data6 = subject.parse_code(subject.parse_lines(puzzle_input6))
    data7 = subject.parse_code(subject.parse_lines(puzzle_input7))
    data8 = subject.parse_code(subject.parse_lines(puzzle_input8))
    data9 = subject.parse_code(subject.parse_lines(puzzle_input9))
    data10 = subject.parse_code(subject.parse_lines(puzzle_input10))
    data11 = subject.parse_code(subject.parse_lines(puzzle_input11))
    data12 = subject.parse_code(subject.parse_lines(puzzle_input12))
    data13 = subject.parse_code(subject.parse_lines(puzzle_input13))

    assert subject.calc_value(data6) == 3
    assert subject.calc_value(data7) == 54
    assert subject.calc_value(data8) == 7
    assert subject.calc_value(data9) == 9
    assert subject.calc_value(data10) == 1
    assert subject.calc_value(data11) == 0
    assert subject.calc_value(data12) == 0
    assert subject.calc_value(data13) == 1
