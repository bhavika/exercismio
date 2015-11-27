# -*- coding: utf-8 -*-

def slicecall(call):
    return call.strip()
    
def is_silence(call):
    return call.strip()
    
def is_anger(call):
    if call.isupper():
        return True
    else:
        return False
        
def is_question(call):
    if call.endswith('?'):
        return True
    else:    
        return False
    
def hey(call):
    x = slicecall(call)
    if is_anger(x):
        return unicode('Whoa, chill out!')
    if is_silence(x) == '':
        return unicode('Fine. Be that way!')
    elif is_question(x):
        return unicode('Sure.')        
    else:
        return unicode('Whatever.')
