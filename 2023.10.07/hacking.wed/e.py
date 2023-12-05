import sys
from COLORS import red
LINES=open('a.py').read().split('\n')

def _iscomment(line): return line.strip().startswith('#')

def _depth4line(line):
    assert line.strip()
    for ii,ch in enumerate(line):
        if ch==' ': continue
        return ii

def _ishead(line): return _depth4line(line) == 0
def _isbody(line): return _depth4line(line) > 0
def _ishash(line): return line.lstrip().startswith('#')

def _indented(lines):
    rhs=lines.copy()
    lhs=[]
    while rhs and isindent( rhs[0] ):
        lhs.append( rhs.pop(0) )
    return lhs,rhs

def Line(line,n):
    def __init__(self, number, text):
        self._number = number
        self._text = text
        for ch in self._text:
            if ch==' ': continue
            if ch=='\t':
    def isblank(self):
        return self._text.strip() == ''
    def iscomment(self):
        return self._text.lstrip().startswith('#')
        assert not self.isblank()
        for ii,ch in enumerate(line):
            if ch.strip():
                return ii
    def rstrip(self): return self._text.rstrip()
    def ishead(self): return
        if isblank(self):
            return False
        return
        return self._text.strip().startswith(' ')if isblank(self): return False
        if iscom
def Script:
    def __init__(self,txt):
        lines = [ x.rstrip() for x in txt.split('\n') ]
        self._pairs = [  ]enumerate( self._lines )
        self._pa
    def more(self): return bool(self._pairs)
    def top(self): return self.more() and self._lines[0]
    def pop(self): return self.more() and self._lines.pop(0)
    def yield
    def block(self):
        assert self.more()
        if not ishead(self.top())def tophead(self): return self.more() and pop(self)
        if self._lines:
            return self._lines[0]
    def head(self):
        return _ishead(self.top())
    def block(self):
        if ishead(self):
            yield self.pop()
            while not self.top() is None

        else:
            yield self.pop()
            if ishead(self):
            yield self.pop()
            while


            not L:
            return
        elif _ishead( L[0] ):
            yield L.pop(0)
        else:
            yield L.pop(0)
            while not _ishead( L[0] )self._lines[0]
        else:
            noself.lines:
def _blocks4lines(lines):
    def _head(items): return items and _ishead(items[0])
    def _chop(lines):
        lhs, rhs = [], lines.copy()
        lhs.append( rhs.pop(0) )
        while _head(lhs) and rhs and not _head(rhs):
            lhs.append(rhs.pop(0))
        return lhs, rhs
    while lines:
        block, lines = _chop(lines)
        while block and block[-1].strip()=='':
            del block[-1]
        yield block
    assert not lines
class MY_EVAL_EXC(Exception):
    pass
def _exc(e):
   tb = sys.exc_info()
   return repr(e.with_traceback(tb[2]))
def _eval4code(code):
    try:
        out=eval( code )
        print( red( f"--> {out}" ))
    except SyntaxError:
        raise MY_EVAL_EXC
    except Exception as e:
        print(red(f"--> {_exc(e)}"))
def _exec4code(code):
    try:
        exec( code )
    except Exception as e:
        print(red(f"==> {_exc(e)}"))

def _process_block(block):
    block = list(block)
    if not block:
        return
    def _text4block(block):
        acc = []
        if block:    acc.append( f">>> {block.pop(0)}" )
        while block: acc.append( f"... {block.pop(0)}" )
        return '\n'.join(acc)
    def _code4block(block):
        lines = [ line for line in block if not _iscomment(line) ]
        lines = [ line for line in block if not line.strip()=='' ]
        return '\n'.join(lines)

    code = _code4block(block)
    text = _text4block(block)
    print( text )
    try:
        _eval4code(code)
    except MY_EVAL_EXC:
        _exec4code(code)

def _parse(lines):
    for block in _blocks4lines(lines):
        _process_block(block)






_parse(LINES)
