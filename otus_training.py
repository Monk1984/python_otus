import pytest

@pytest.fixture

def test_a():
    a = [5,2,3]
    a.sort()
    print(a)

def test_b():
    b = [2,5,8,9,1]
    b.append('app')
    print(b)
    print(len(b))
    e = b
    print(e[3])
    del e[0]
    print(e)

def test_c():
    c = (1,4,6,8)
    v = c
    print(len(v))

def test_d():
    a = [11,4,13,17,1,3,9,10]
    if len(a) == 8:
        print('cool')
    else:
        print('bad')
