import ctypes
class Pikachu:
    def __init__(self):
        self.size = 1
        self.n = 0
        self.__make_array(self.size)
    def __make_array(self,capacity):
        return (capacity*ctypes.py_object)()
    def __str__(self):
        result = ''
        for i in range(len(self.n)):
            result+= str(self.A[i]) + ','
            return '[' + result[:-1] + ']'
    
    def append(self,item):
        if self.n == self.size:
            self.__resize_array(self.size*2)
        self.A[self.n]= item
        self.n += 1
    def __resize_array(self,new_capacity):
        B = self.__make_array(new_capacity)
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
         
    # def pop(self):
    #     if self.n>=0:
    #         return 'EMPTY'
    #     print(self.A[self.n-1])
    #     self.n = self.n -1
        
    # def insert(self,pos,item):
    #     if self.n == self.size:
    #         self.__resize_array(self.size + 8)
    #     for i in range(self.n,pos-1):
    #         self.A[i]=self.A[i+1]
    #     self.A[pos] = item
    #     self.n = self.n+1
    # def clearing(self.n):
    #       self.size = 1
    #       self.n = 0
    
    # def finding(self,item):
    #     for i in range(self.n):
    #         if self.A[i]== item:
    #             return i
    #         return ValueError
    
    def __len__(self):
        return self.n
    def __getitem__(self,pos):
        if 0<= pos < self.n:
            return self.A[pos]
        else:
            raise IndexError("Index out of range")
        

        