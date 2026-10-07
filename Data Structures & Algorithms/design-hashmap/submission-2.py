class MyList:
    def __init__(self):
        lst = []

class MyHashMap:

    def __init__(self):
        self.lst = []

    def put(self, key: int, value: int) -> None:
        if len(self.lst) == 0:
            self.lst.append([key,value])
            return

        for i in range(len(self.lst)):
            if key == self.lst[i][0]:
                self.lst[i][1] = value
                return 

        self.lst.append(list([key,value]))
    

    def get(self, key: int) -> int:
        for k in self.lst:
            if key == k[0]:
                return k[1]
        return -1

    def remove(self, key: int) -> None:
        if len(self.lst) == 0:
            return

        for k in self.lst:
            if key == k[0]:
                self.lst.remove(k)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)