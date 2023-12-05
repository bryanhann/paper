def line(ch="#", n=10, end='\n'):
    "Return a string of count ch."
    assert len(ch)==1
    return ch*n + end
