__author__ = 'Jordan Guerin'
class point:
    def __init__(self, x=0.000000, y=0.000000):
        self.x = x
        self.y = y

class dataset:

    def __init__(self, filename = 'dataset.txt'):

        self.filename = filename
        self.points = []

    def load(self):

        fp = open(self.filename, 'r')

        text = fp.read(4096)

        fp.close()

        data = text.split(' ')

        i = 0

        while i < len(data):
            pt = point()
            pt.x = float(data[i])
            pt.y = float(data[i+1])
            self.points.append(pt)
            i += 2



if __name__ == '__main__':

    dt = dataset()

    dt.load()

    for p in dt.points:
        print p.x, p.y
    
