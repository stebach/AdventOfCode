import solve_2016_22 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'root@xxx# df -h',
        'Filesystem              Size  Used  Avail  Use%',
        '/dev/grid/node-x0-y0     85T    6T    79T   77%',
        '/dev/grid/node-x0-y1     93T   16T    77T   70%',
        '/dev/grid/node-x0-y2     93T   65T    28T   69%',
        '/dev/grid/node-x1-y0     90T   27T    63T   74%',
        '/dev/grid/node-x1-y1     94T   67T    27T   71%',
        '/dev/grid/node-x1-y2     92T   69T    23T   75%',
        '/dev/grid/node-x2-y0     88T   64T    24T   72%',
        '/dev/grid/node-x2-y1     86T   71T    15T   82%',
        '/dev/grid/node-x2-y2     94T   71T    23T   75%',
    ]

@pytest.fixture
def puzzle_input2():
    return [
        'Filesystem            Size  Used  Avail  Use%',
        '/dev/grid/node-x0-y0   10T    8T     2T   80%',
        '/dev/grid/node-x0-y1   11T    6T     5T   54%',
        '/dev/grid/node-x0-y2   32T   28T     4T   87%',
        '/dev/grid/node-x1-y0    9T    7T     2T   77%',
        '/dev/grid/node-x1-y1    8T    0T     8T    0%',
        '/dev/grid/node-x1-y2   11T    7T     4T   63%',
        '/dev/grid/node-x2-y0   10T    6T     4T   60%',
        '/dev/grid/node-x2-y1    9T    8T     1T   88%',
        '/dev/grid/node-x2-y2    9T    6T     3T   66%',
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == (
        (0, 0, 85, 6, 79),
        (0, 1, 93, 16, 77),
        (0, 2, 93, 65, 28),
        (1, 0, 90, 27, 63),
        (1, 1, 94, 67, 27),
        (1, 2, 92, 69, 23),
        (2, 0, 88, 64, 24),
        (2, 1, 86, 71, 15),
        (2, 2, 94, 71, 23),
    )

def test_count_pairs(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.count_pairs(data) == 17

def test_fewest_steps(puzzle_input2):
    data = subject.parse_lines(puzzle_input2)
    assert subject.fewest_steps(data) == 7
