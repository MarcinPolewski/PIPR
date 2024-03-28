class WrongList:
    def __init__(self, list=[]):
        self._list = list

    def appendList(self):
        self._list.append("do")


wl1 = WrongList()
wl1.appendList()

wl2 = WrongList()
print(wl2._list)
# wypisze nam ["do"]


def funkcja(a=None):
    a.append("dodo")


a = []
funkcja(a)
print(a)
# WYPISUJE: ["dodo"]

s = "dudasdlkjf"
print(s.count("d"))
print(s[-1])
