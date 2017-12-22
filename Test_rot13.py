from rot13 import rot_13

def rot13():
    assert rot_13('abc') == 'nop'
    assert rot_13('nop') == 'abc'
    assert rot_13('xyz ABC') == 'klm NOP'
    assert rot_13('XYZ abc') == 'KLM nop'