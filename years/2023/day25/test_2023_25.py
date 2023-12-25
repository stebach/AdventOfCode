import solve_2023_25 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'jqt: rhn xhk nvd',
        'rsh: frs pzl lsr',
        'xhk: hfx',
        'cmg: qnr nvd lhk bvb',
        'rhn: xhk bvb hfx',
        'bvb: xhk hfx',
        'pzl: lsr hfx nvd',
        'qnr: nvd',
        'ntq: jqt hfx bvb xhk',
        'nvd: lhk',
        'lsr: lhk',
        'rzs: qnr cmg lsr rsh',
        'frs: qnr lhk lsr'
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == {
        'jqt':{'rhn':0,'xhk':0,'nvd':0,'ntq':0,},
        'rhn':{'jqt':0,'xhk':0,'bvb':0,'hfx':0,},
        'xhk':{'jqt':0,'hfx':0,'rhn':0,'bvb':0,'ntq':0,},
        'nvd':{'jqt':0,'cmg':0,'pzl':0,'qnr':0,'lhk':0,},
        'lhk':{'cmg':0,'nvd':0,'lsr':0,'frs':0,},
        'rsh':{'frs':0,'pzl':0,'lsr':0,'rzs':0,},
        'hfx':{'xhk':0,'rhn':0,'bvb':0,'pzl':0,'ntq':0,},
        'pzl':{'rsh':0,'lsr':0,'hfx':0,'nvd':0,},
        'bvb':{'cmg':0,'rhn':0,'xhk':0,'hfx':0,'ntq':0,},
        'ntq':{'jqt':0,'hfx':0,'bvb':0,'xhk':0,},
        'rzs':{'qnr':0,'cmg':0,'lsr':0,'rsh':0,},
        'lsr':{'rsh':0,'pzl':0,'lhk':0,'rzs':0,'frs':0,},
        'frs':{'rsh':0,'qnr':0,'lhk':0,'lsr':0,},
        'cmg':{'qnr':0,'nvd':0,'lhk':0,'bvb':0,'rzs':0,},
        'qnr':{'cmg':0,'nvd':0,'rzs':0,'frs':0,},
    }

def test_part1_example1(puzzle_input):
    assert subject.part1(subject.parse_lines(puzzle_input)) == 54

