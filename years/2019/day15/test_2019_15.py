import solve_2019_15 as subject
import pytest

def test_intcode():
    data = [1,9,10,3,2,3,11,0,99,30,40,50]
    subject.intcode(data)
    assert data == [3500,9,10,70,2,3,11,0,99,30,40,50]
    data = [1,0,0,0,99]
    subject.intcode(data)
    assert data == [2,0,0,0,99]
    data = [2,3,0,3,99]
    subject.intcode(data)
    assert data == [2,3,0,6,99]
    data = [2,4,4,5,99,0]
    subject.intcode(data)
    assert data == [2,4,4,5,99,9801]
    data = [1,1,1,4,99,5,6,0,99]
    subject.intcode(data)
    assert data == [30,1,1,4,2,5,6,0,99]
    data = [1002,4,3,4,33]
    subject.intcode(data)
    assert data == [1002,4,3,4,99]
    output = []
    for x in range(7,10):
        input = [x]
        subject.intcode([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99], input, output)
    assert output == [999, 1000, 1001]
    output = []
    subject.intcode([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99],[],output)
    assert output == [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    subject.intcode([1102,34915192,34915192,7,4,7,99,0],[],output)
    assert len(str(output[-1])) == 16
    subject.intcode([104,1125899906842624,99],[],output)
    assert output[-1] == 1125899906842624
