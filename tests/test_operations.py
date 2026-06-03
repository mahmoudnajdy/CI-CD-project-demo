from scr.math_operations import add,sub

def test_add():
    assert add(2,3)==5
    assert add(0,3)==3
    assert add(-1,1)==0

def test_sub():
    assert sub(5,3)==2
    assert sub(10,-1)==11
    assert sub(-5,0)==-5
    assert sub(-3,3)==-6

    
