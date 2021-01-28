#!/usr/bin/python

def func01():
    return 3
    
def test_script():
    a = 23
    a = a + func01()
    assert a == 20
