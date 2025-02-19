from main import BinaryNumber, quadratic_multiply



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3*3
    assert quadratic_multiply(BinaryNumber(4), BinaryNumber(6)) == 4*6
    assert quadratic_multiply(BinaryNumber(7), BinaryNumber(8)) == 7*8

def test_multiply_by_zero():
    assert quadratic_multiply(BinaryNumber(0), BinaryNumber(0)) == 0
    assert quadratic_multiply(BinaryNumber(0), BinaryNumber(3)) == 0
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(0)) == 0

def test_multiply_by_one():
    assert quadratic_multiply(BinaryNumber(1), BinaryNumber(3)) == 3
    assert quadratic_multiply(BinaryNumber(5), BinaryNumber(1)) == 5
    assert quadratic_multiply(BinaryNumber(1), BinaryNumber(9)) == 9
    
def test_multiply_power_of_two():
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 4
    assert quadratic_multiply(BinaryNumber(5), BinaryNumber(5)) == 25
    assert quadratic_multiply(BinaryNumber(15), BinaryNumber(15)) == 225

def test_multiply_large_num():
    assert quadratic_multiply(BinaryNumber(234), BinaryNumber(567)) == 234*567
    assert quadratic_multiply(BinaryNumber(123), BinaryNumber(456)) == 123*456
    assert quadratic_multiply(BinaryNumber(987), BinaryNumber(654)) == 987*654
    assert quadratic_multiply(BinaryNumber(3456), BinaryNumber(9234)) == 3456*9234