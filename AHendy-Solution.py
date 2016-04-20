# Params:
# Two 2D tuples in cartesian
# (x1,y1), (x2, y2)
# Return:
# Standard form of line: Ax + By = C
# Slope Intercept form of line: y = mx+b
# Passing through (x1, y1): y - y1 = m(x-x1)
# m = (y1-y2) / (x1-x2)
# C = (x1-x2)*y1 - (y1-y2)*x1
# B = (x1-x2)
# A = -1*(y1-y2)


def cartesian_to_line(p1, p2):
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]

    numerator = (y1 - y2)
    denom = (x1 - x2)

    if denom is 0:
        # Verticle line
        # B = 0 in standard form
        # A = 1
        # C = common x value between 2 points

        A = 1
        B = 0
        C = x1
    else:
        # Regular line
        # m = float(numerator) / denom
        A = -numerator  #
        B = denom
        C = denom * y1 - numerator * x1
    print 'Standard form: %dx + %dy = %d' % (A, B, C)
    return (A, B, C)


def test_func():
    Test1 = (A1, B1, C1) = cartesian_to_line((5, 2),
                                             (8, 4))
    Test2 = (A2, B2, C2) = cartesian_to_line((5, 2),
                                             (5, 4))

    assert Test1 == (2, -3, 4), 'Test1 Failed'
    print 'Test 1 Passed'
    assert Test2 == (1, 0, 5), 'Test2 Failed'
    print 'Test 2 Passed'


if __name__ == '__main__':
    test_func()
