import solve_2024_24 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'x00: 1',
        'x01: 1',
        'x02: 1',
        'y00: 0',
        'y01: 1',
        'y02: 0',
        '',
        'x00 AND y00 -> z00',
        'x01 XOR y01 -> z01',
        'x02 OR y02 -> z02'
    ]

@pytest.fixture
def puzzle_input2():
    return [
        'x00: 1',
        'x01: 0',
        'x02: 1',
        'x03: 1',
        'x04: 0',
        'y00: 1',
        'y01: 1',
        'y02: 1',
        'y03: 1',
        'y04: 1',
        '',
        'ntg XOR fgs -> mjb',
        'y02 OR x01 -> tnw',
        'kwq OR kpj -> z05',
        'x00 OR x03 -> fst',
        'tgd XOR rvg -> z01',
        'vdt OR tnw -> bfw',
        'bfw AND frj -> z10',
        'ffh OR nrd -> bqk',
        'y00 AND y03 -> djm',
        'y03 OR y00 -> psh',
        'bqk OR frj -> z08',
        'tnw OR fst -> frj',
        'gnj AND tgd -> z11',
        'bfw XOR mjb -> z00',
        'x03 OR x00 -> vdt',
        'gnj AND wpb -> z02',
        'x04 AND y00 -> kjc',
        'djm OR pbm -> qhw',
        'nrd AND vdt -> hwm',
        'kjc AND fst -> rvg',
        'y04 OR y02 -> fgs',
        'y01 AND x02 -> pbm',
        'ntg OR kjc -> kwq',
        'psh XOR fgs -> tgd',
        'qhw XOR tgd -> z09',
        'pbm OR djm -> kpj',
        'x03 XOR y03 -> ffh',
        'x00 XOR y04 -> ntg',
        'bfw OR bqk -> z06',
        'nrd XOR fgs -> wpb',
        'frj XOR qhw -> z04',
        'bqk OR frj -> z07',
        'y03 OR x01 -> nrd',
        'hwm AND bqk -> z03',
        'tgd XOR rvg -> z12',
        'tnw OR pbm -> gnj'
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == {
        'wires': {
            'x00': 1,
            'x01': 1,
            'x02': 1,
            'y00': 0,
            'y01': 1,
            'y02': 0
        },
        'gates': {
            'z00': ('AND', ('x00', 'y00')),
            'z01': ('XOR', ('x01', 'y01')),
            'z02': ('OR', ('x02', 'y02'))
        }
    }

def test_get_decimal(puzzle_input, puzzle_input2):
    data = subject.parse_lines(puzzle_input)
    assert subject.get_decimal(data) == 4

    data2 = subject.parse_lines(puzzle_input2)
    assert subject.get_decimal(data2) == 2024


def test_solve(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.solve(data) == (4, '')

