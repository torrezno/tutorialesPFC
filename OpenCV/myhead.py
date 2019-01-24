# myhead

def toCV(p,dim):
    x = p[0]
    y = p[1]
    mX =dim[0]
    mY =dim[1]
    return (x,mY-y)

def toNP(p,dim):
    x = p[0]
    y = p[1]
    mX =dim[0]
    mY =dim[1]
    return (mY-y,x)