import solve_2021_25 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "v...>>.vv>",
        ".vv>>.vv..",
        ">>.>v>...v",
        ">>v>>.>.v.",
        "v>v.vv.v..",
        ">.>>..v...",
        ".vv..>.>v.",
        "v.v..>>v.v",
        "....v..v.>"
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == {
        'width': 10,
        'height': 9,
        'moves': 0,
        'right':set([(4,0),(5,0),(9,0),(3,1),(4,1),(0,2),(1,2),(3,2),(5,2),(0,3),(1,3),(3,3),(4,3),(6,3),(1,4),(0,5),(2,5),(3,5),(5,6),(7,6),(5,7),(6,7),(9,8)]),
        'down':set([(0,0),(7,0),(8,0),(1,1),(2,1),(6,1),(7,1),(4,2),(9,2),(2,3),(8,3),(0,4),(2,4),(4,4),(5,4),(7,4),(6,5),(1,6),(2,6),(8,6),(0,7),(2,7),(7,7),(9,7),(4,8),(7,8)]),
    }

def test_step(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    subject.step(data)
    assert data2string(data) == '....>.>v.>\nv.v>.>v.v.\n>v>>..>v..\n>>v>v>.>.v\n.>v.v...v.\nv>>.>vvv..\n..v...>>..\nvv...>>vv.\n>.v.v..v.v'

    subject.step(data) # 2
    assert data2string(data) == '>.v.v>>..v\nv.v.>>vv..\n>v>.>.>.v.\n>>v>v.>v>.\n.>..v....v\n.>v>>.v.v.\nv....v>v>.\n.vv..>>v..\nv>.....vv.'

    subject.step(data) # 3
    assert data2string(data) == 'v>v.v>.>v.\nv...>>.v.v\n>vv>.>v>..\n>>v>v.>.v>\n..>....v..\n.>.>v>v..v\n..v..v>vv>\nv.v..>>v..\n.v>....v..'

    subject.step(data) # 4
    assert data2string(data) == 'v>..v.>>..\nv.v.>.>.v.\n>vv.>>.v>v\n>>.>..v>.>\n..v>v...v.\n..>>.>vv..\n>.v.vv>v.v\n.....>>vv.\nvvv>...v..'

    subject.step(data) # 5
    assert data2string(data) == 'vv>...>v>.\nv.v.v>.>v.\n>.v.>.>.>v\n>v>.>..v>>\n..v>v.v...\n..>.>>vvv.\n.>...v>v..\n..v.v>>v.v\nv.v.>...v.'

    for i in range(5):
        subject.step(data) # 10
    assert data2string(data) == '..>..>>vv.\nv.....>>.v\n..v.v>>>v>\nv>.>v.>>>.\n..v>v.vv.v\n.v.>>>.v..\nv.v..>v>..\n..v...>v.>\n.vv..v>vv.'


    for i in range(10):
        subject.step(data) # 20
    assert data2string(data) == 'v>.....>>.\n>vv>.....v\n.>v>v.vv>>\nv>>>v.>v.>\n....vv>v..\n.v.>>>vvv.\n..v..>>vv.\nv.v...>>.v\n..v.....v>'

    for i in range(10):
        subject.step(data) # 30
    assert data2string(data) == '.vv.v..>>>\nv>...v...>\n>.v>.>vv.>\n>v>.>.>v.>\n.>..v.vv..\n..v>..>>v.\n....v>..>v\nv.v...>vv>\nv.v...>vvv'


    for i in range(10):
        subject.step(data) # 40
    assert data2string(data) == '>>v>v..v..\n..>>v..vv.\n..>>>v.>.v\n..>>>>vvv>\nv.....>...\nv.v...>v>>\n>vv.....v>\n.>v...v.>v\nvvv.v..v.>'


    for i in range(10):
        subject.step(data) # 50
    assert data2string(data) == '..>>v>vv.v\n..v.>>vv..\nv.>>v>>v..\n..>>>>>vv.\nvvv....>vv\n..v....>>>\nv>.......>\n.vv>....v>\n.>v.vv.v..'


    for i in range(5):
        subject.step(data) # 55
    assert data2string(data) == '..>>v>vv..\n..v.>>vv..\n..>>v>>vv.\n..>>>>>vv.\nv......>vv\nv>v....>>v\nvvv...>..>\n>vv.....>.\n.>v.vv.v..'

    subject.step(data) # 56
    assert data2string(data) == '..>>v>vv..\n..v.>>vv..\n..>>v>>vv.\n..>>>>>vv.\nv......>vv\nv>v....>>v\nvvv....>.>\n>vv......>\n.>v.vv.v..'

    subject.step(data) # 57
    assert data2string(data) == '..>>v>vv..\n..v.>>vv..\n..>>v>>vv.\n..>>>>>vv.\nv......>vv\nv>v....>>v\nvvv.....>>\n>vv......>\n.>v.vv.v..'

    subject.step(data) # 58
    assert data2string(data) == '..>>v>vv..\n..v.>>vv..\n..>>v>>vv.\n..>>>>>vv.\nv......>vv\nv>v....>>v\nvvv.....>>\n>vv......>\n.>v.vv.v..'

def data2string(data):
    grid = []
    for y in range(data['height']):
        row = []
        for x in range(data['width']):
            if (x,y) in data['right']:
                row.append('>')
            elif (x,y) in data['down']:
                row.append('v')
            else:
                row.append('.')
        grid.append("".join(row))
    
    return "\n".join(grid)
