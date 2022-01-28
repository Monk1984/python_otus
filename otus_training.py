import pytest

@pytest.fixture




def test():
    a = [5,2,3]
    a.sort()
    print(a)

def test_tools():
    b = [2,5,8,9,1]
    b.append('app')
    print(b)
    print(len(b))
    e = b
    print(e[3])

def test_def():
    c = (1,4,6,8)
    v = c
    print(len(v))
