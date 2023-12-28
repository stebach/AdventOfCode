import solve_2018_20 as subject
import pytest

def test_part1_example1():
    assert subject.part1("^WNE$") == 3
    assert subject.part1("^ENWWW(NEEE|SSE(EE|N))$") == 10
    assert subject.part1("^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$") == 18
    assert subject.part1("^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$") == 23
    assert subject.part1("^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$") == 31

