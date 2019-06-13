
import copy

class Record:

    username = ""
    password = ""
    winTimes = 0
    lossTimes = 0
    money = 0

    def __init__(self):
        pass
    def __str__(self):
        s = "%s,%s,%d,%d,%d" % (self.username,self.password,self.winTimes,self.lossTimes,self.money)
        return s

class DataBase:

    __filePath = "db.txt"

    def __init__(self):
        self.records = []
        self.readFile()

    def readFile(self):

        fp = open(self.__filePath,"r")
        for line in fp:
            words = line.split(",")
            # print(words)
            record = Record()
            record.username = words[0]
            record.password = words[1]
            record.winTimes = int(words[2])
            record.lossTimes = int(words[3])
            record.money = int(words[4])
            self.records.append(record)
        fp.close()

    def writeFile(self):

        fp = open(self.__filePath,"w")
        for record in self.records:
            line = str(record) + "\n"
            fp.write(line)
        fp.close()

    def sortByMoney(self):
        records = copy.deepcopy(self.records)
        records = sorted(records,key=lambda x:x.money,reverse=True)
        return records


    def sortByWinTimes(self):
        records = copy.deepcopy(self.records)
        records = sorted(records,key=lambda x:x.winTimes,reverse=True)
        return records


def main():
    db = DataBase()
    for i in db.sortByWinTimes():
        print(i)


if __name__ == '__main__':
    main()
