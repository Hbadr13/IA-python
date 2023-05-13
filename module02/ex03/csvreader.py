import os


class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.header = header
        self.filename = filename
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.sep = sep
        self.alldata = []
        if not isinstance(self.skip_bottom, int) or self.skip_bottom < 0:
            raise ValueError
        if not isinstance(self.skip_top, int) or self.skip_top < 0:
            raise ValueError
        if not os.path.exists(self.filename):
            raise FileNotFoundError
    def __enter__(self):
            # return None
        self.file = open(self.filename)
        alldata = self.file.read()
        lines = str.split(alldata, '\n')
        lines = list(map(lambda l: l.split(self.sep), lines))
        for l in lines:
            l = [(j.rstrip().lstrip()) for j in l if len(l) > 0]
            if len(lines[0]) != len(l):
                return None
            self.alldata.append(l)
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.file.close()
        if exc_value != None:
            print("exc_type={}\nexc_value={}\nexc_tb={}".format(exc_type,exc_value,exc_tb))
        return True

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """
        data = []
        data = self.alldata[self.skip_top:self.skip_bottom]
        return data
    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        if self.header == True and len(self.alldata) > 0:
            return self.alldata[0]
        return None

