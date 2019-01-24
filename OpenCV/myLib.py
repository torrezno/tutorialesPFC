# myhead


def toCV(p, dim):
    x = p[0]
    y = p[1]
    mX = dim[0]
    mY = dim[1]
    return (x, mY - y)


def toNP(p, dim):
    x = p[0]
    y = p[1]
    mX = dim[0]
    mY = dim[1]
    return (mY - y, x)


def CV2XY(p, dim):
    x = p[0]
    y = p[1]
    mX = dim[0]
    mY = dim[1]
    return (x, mY - y)


def NP2XY(p, dim):
    x = p[0]
    y = p[1]
    mX = dim[0]
    mY = dim[1]
    return (y, mY - x)


def CV2NP(p, dim):
    return (p[1], p[0])


def NP2CV(p, dim):
    return CV2NP(p, dim)


def rescale2(value, src_min, src_max, dst_min, dst_max):
    src_len = src_max - src_min
    dst_len = dst_max - dst_min
    aux = 1.0 * (value - src_min) / src_len
    return dst_min + aux * dst_len


def rescale(value, src, dst):
    src_min = src[0]
    src_max = src[1]
    dst_min = dst[0]
    dst_max = dst[1]
    return rescale2(value, src_min, src_max, dst_min, dst_max)
