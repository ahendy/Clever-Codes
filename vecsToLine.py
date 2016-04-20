# Params:
# Two 2D tuples in cartesian
# (x1,y1), (x2, y2)
# Return:
# Standard form of line y = mx+b / Ax + By = C
# Passing through (x1, y1): y - y1 = m(x-x1)
# m = (y1-y2) / (x1-x2)
# C = -m*x1 + y1


def cartesian_to_line(p1, p2):
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]

    numerator = y1 - y2
    denom     = x1 - x2
 	
    if denom is 0:
     	# Verticle line 
        # Use x = 
        print 'The Line is: x = ' + str(x1) + '.'
        return (None, x1)
    else: 
	    m = float(numerator)/denom
	    print m
	    C = -1*m*x1 + y1
	    A = m # *x
	    print "The Line is: y = " + str(m) + "x + " + str(C) + "."
	    return (m, C)

def test_func():
    test1_a,test1_b = cartesian_to_line((5,2),
							  (8,4))
    test2 = cartesian_to_line((5,2),
							  (5,4))
    

    assert (test1_a == 2.0/3), 'Test1_a failed'
    print "Test1_a passed"
    assert (test1_b - (-10.0/3 +2) < 10e-4)
    print "Test1_b passed"
    assert (test2 == (None, 5)), 'Verticle Line test failed'
    print "Test2 passed"



if __name__ == '__main__':
    test_func()
