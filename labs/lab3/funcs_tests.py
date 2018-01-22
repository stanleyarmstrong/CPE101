import funcs

def test_cube():
    found = funcs.cube(2)
    expected = 8
    assert found == expected

    found = funcs.cube(-2)
    expected = -8
    assert found == expected

    found = funcs.cube(0)
    assert found == 0
def test_hypotenuse():
    found = funcs.hypotenuse(3 ,4)
    expected = 5
    assert found == expected

    found = funcs.hypotenuse(3, -4)
    expected = 5
    assert found == expected

    found = funcs.hypotenuse(6, 8)
    expected = 10
    assert found == expected
def test_f():
    found = funcs.f(2, 2)
    expected = 5
    assert found == expected
    found = funcs.f(1,1)
    expected = 3.5
    assert found == expected
    found = funcs.f(3,3)
    expected = ((3*3**2) + (4*3))/ (2 * 3)
    assert found == expected
def test_is_positive():
    found = funcs.is_positive(-1)
    expected = False
    assert found == expected
    found = funcs.is_positive(1)
    expected = True
    assert found == expected
    found = funcs.is_positive(-2)
    expected = False
    assert found == expected
def test_both_positive():
    found = funcs.both_positive(2,2)
    expected = True
    assert found == expected
    found = funcs.both_positive(2, -2)
    expected = False
    assert found == expected
    found = funcs.both_positive(3,3)
    expected = True
    assert found == expected
def main():
    test_cube()
    test_hypotenuse()
    test_f()
    test_is_positive()
    test_both_positive()
if __name__ == '__main__':
    main()
