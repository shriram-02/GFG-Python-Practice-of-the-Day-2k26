def pf(dq,x):
    #code here
    dq.appendleft(x)
def pb(dq,x):
    #code here
    dq.append(x)
def front_dq(dq):
    #code here
    return dq[0] if dq else -1 
def ppb(dq):
    #code here
    if dq:
        dq.pop()