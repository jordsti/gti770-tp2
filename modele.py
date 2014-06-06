__author__ = 'Jordan Guerin'
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

    fp = open("test.out", 'w')

    for i in range(10, 81, 5):
        x_test = x_train[len(x_train)-i:]
        w = entrainerModele(x_test, 3)

        poly = numpy.poly1d(w)
        err = evaluerModele(poly, x_sel)
        print "E_emp[%d] : %.06f" % (i, err)

        err2 = evaluerModele(poly, x_test)
        print "E_gen[%d] : %.06f" % (i, err2)
        fp.write(("%d\t%0.6f\t%0.6f\n" % (i, err, err2)).replace('.', ','))
    fp.close()
    print ""
    print "Influence de l'ordre de regression"

    x_train = data.points[0:60]

    x_valid = data.points[60:80]

    x_test = data.points[80:]

    e_emp = []
    e_gen = []

    degs = []

    fp = open('test2.out', 'w')

    for deg in range(21):
        degs.append(deg)
        w = entrainerModele(x_train, deg)

        poly = numpy.poly1d(w)
        err = evaluerModele(poly, x_train)
        print "E_emp[%d] : %0.6f" % (deg, err)
        e_emp.append(err)
        err2 = evaluerModele(poly, x_valid)
        print "E_gen[%d] : %0.6f" % (deg, err2)
        e_gen.append(err2)

        fp.write(("%d\t%0.6f\t%0.6f\n" % (deg, err, err2)).replace('.', ','))

    fp.close()
    import matplotlib.pyplot as plot
    #plot.plot(degs, e_emp, 'b.', degs, e_gen, "g.")
    #plot.show()


    #test p*

    fp = open('test3.out', 'w')

    #meilleur ordre est 1
    w = entrainerModele(x_train, 1)
    poly = numpy.poly1d(w)

    err = evaluerModele(poly, x_train)
    print err
