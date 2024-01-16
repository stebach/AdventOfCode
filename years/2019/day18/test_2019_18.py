import solve_2019_18 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '#########',
        '#b.A.@.a#',
        '#########'
    ]

@pytest.fixture
def puzzle_input2():
    return [
        '########################',
        '#f.D.E.e.C.b.A.@.a.B.c.#',
        '######################.#',
        '#d.....................#',
        '########################'
    ]

@pytest.fixture
def puzzle_input3():
    return [
        '########################',
        '#...............b.C.D.f#',
        '#.######################',
        '#.....@.a.B.c.d.A.e.F.g#',
        '########################'
    ]

@pytest.fixture
def puzzle_input4():
    return [
        '#################',
        '#i.G..c...e..H.p#',
        '########.########',
        '#j.A..b...f..D.o#',
        '########@########',
        '#k.E..a...g..B.n#',
        '########.########',
        '#l.F..d...h..C.m#',
        '#################'
    ]

@pytest.fixture
def puzzle_input5():
    return [
        '########################',
        '#@..............ac.GI.b#',
        '###d#e#f################',
        '###A#B#C################',
        '###g#h#i################',
        '########################'
    ]

@pytest.fixture
def puzzle_input6():
    return [
        '#######',
        '#a.#Cd#',
        '##...##',
        '##.@.##',
        '##...##',
        '#cB#Ab#',
        '#######'
    ]

@pytest.fixture
def puzzle_input7():
    return [
        '###############',
        '#d.ABC.#.....a#',
        '######...######',
        '######.@.######',
        '######...######',
        '#b.....#.....c#',
        '###############'
    ]

@pytest.fixture
def puzzle_input8():
    return [
        '#############',
        '#DcBa.#.GhKl#',
        '#.###...#I###',
        '#e#d#.@.#j#k#',
        '###C#...###J#',
        '#fEbA.#.FgHi#',
        '#############'
    ]

@pytest.fixture
def puzzle_input9():
    return [
        '#############',
        '#g#f.D#..h#l#',
        '#F###e#E###.#',
        '#dCba...BcIJ#',
        '#####.@.#####',
        '#nK.L...G...#',
        '#M###N#H###.#',
        '#o#m..#i#jk.#',
        '#############'
    ]


def test_find_shortest(puzzle_input, puzzle_input2, puzzle_input3, puzzle_input4, puzzle_input5):
    assert subject.find_shortest(puzzle_input) == 8
    assert subject.find_shortest(puzzle_input2) == 86
    assert subject.find_shortest(puzzle_input3) == 132
    assert subject.find_shortest(puzzle_input4) == 136
    assert subject.find_shortest(puzzle_input5) == 81

def test_find_shortest2(puzzle_input6, puzzle_input7, puzzle_input8, puzzle_input9):
    assert subject.find_shortest2(puzzle_input6) == 8
    assert subject.find_shortest2(puzzle_input7) == 24
    assert subject.find_shortest2(puzzle_input8) == 32
    assert subject.find_shortest2(puzzle_input9) == 72


