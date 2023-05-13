from csvreader import CsvReader
import logging

if __name__ == "__main__":
    with CsvReader('good.csv',header=1,skip_top=1,skip_bottom=2) as file:
        if file == None:
            print("file is corrupted")
        else:
            data = file.getdata()
            header = file.getheader()
            print(data)
            print(header)
            # raise ValueError