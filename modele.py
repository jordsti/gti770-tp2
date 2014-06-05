__author__ = 'JordSti'
import numpy
import math
from data import dataset

data = dataset()
data.load()

x_train = data.points[0:80]
#x_valid = data.points[60:80]
x_test = data.points[80:]

def entrainerModele(pts, deg=0):

    a_x = []
    a_y = []

    for p in pts:
        a_x.append(p.x)
        a_y.append(p.y)

    w = numpy.polynomial.polynomial.polyfit(a_x, a_x, deg)

    return w

def evaluerModele(p, x_sel):

    n = float(len(x_sel))

    sum = 0.0000000
    for pt in x_sel:
        p_y = numpy.polyval(p, pt.x)
        #print p_y
        sum += math.pow(pt.y - p_y, 2)

    return sum/n


if __name__ == '__main__':
    print "Influence du nombre de donnee"
    x_sel = x_train[0:10]

    w = entrainerModele(x_sel, 3)
    poly = numpy.poly1d(w)
    err = evaluerModele(poly, x_sel)
    print "Xsel : %.06f" % err

    for i in range(10, 81, 5):
        x_test = x_train[len(x_train)-i:]
        w = entrainerModele(x_test, 3)

        poly = numpy.poly1d(w)
        err = evaluerModele(poly, x_sel)
        print "E_emp[%d] : %.06f" % (i, err)

        err = evaluerModele(poly, x_test)
        print "E_gen[%d] : %.06f" % (i, err)

    print ""
    print "Inflience de l'ordre de regression"

    x_train = data.points[0:60]

    x_valid = data.points[60:80]

    x_test = data.points[80:]

    for deg in range(21):
        w = entrainerModele(x_train, deg)

        poly = numpy.poly1d(w)
        err = evaluerModele(poly, x_train)
        print "E_emp[%d] : %0.6f" % (deg, err)

        err = evaluerModele(poly, x_valid)
        print "E_gen[%d] : %0.6f" % (deg, err)