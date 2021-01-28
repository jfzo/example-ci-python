#!/usr/bin/python

def func01():
    return None
    
if __name__ == '__main__':
    a = 23
    a = a + func01()
    assert a == 20
