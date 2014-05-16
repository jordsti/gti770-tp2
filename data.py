

class dataset:

    def __init__(self, filename = 'dataset.txt'):

        self.filename = filename


    def load(self):

        fp = open(self.filename, 'r')

        text = fp.read(4096)

        fp.close()

        data = text.split(' ')

        for d in data:

            #print d
            fl = float(d)
            print fl


if __name__ == '__main__':

    dt = dataset()

    dt.load()
    
