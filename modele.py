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
        sum += math.pow(p_y - pt.y, 2)

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
        err = evaluerModele(poly, x_test)
        print "Xtest[%d] : %.06f" % (i, err)
