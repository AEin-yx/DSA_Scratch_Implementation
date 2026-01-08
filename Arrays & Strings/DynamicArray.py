#Dynamic Array size doubles as we insert more elements

class DynamicArray:
    def __init__(self):
        self.n=0 # number of elements
        self.capacity=1 # capacity of array
        self.A=self.create_array(self.capacity) # create a array with the method create_array
    
    def create_array(self, new_capacity:int): # create a array with the method create_array
        hardarray:list=[0]*new_capacity # create a array with the method create_array
        return hardarray
    
    def append(self,elem:int): # append an element to the array
        if self.n< self.capacity: # when the space is empty inside the array
            self.A[self.n]=elem # append an element to the array
            self.n=self.n+1
        elif self.n==self.capacity: # when the space is full inside the array
            self._resize(2*self.capacity) # resize the array
            self.A[self.n]=elem
            self.n=self.n+1
    
    def _resize(self,new_capacity:int): # resize the array
        B=self.create_array(new_capacity) # create a proxy array
        for k in range(self.n): # copy the elements from the old array to the new array
            B[k]=self.A[k]
        self.A=B # assign the proxy array to the old array( reassigned the pointer)
        self.capacity=new_capacity # update the capacity
    
    def reveal(self): # print the array
        str=""
        for k in range(self.n):
            # str+="| "+str(self.A[k])+" |"
            print("| ",self.A[k]," |",end="")
        return str
    
    def __len__(self):
        return self.n
    
    def __getCapacity__(self):
        return self.capacity

arr=DynamicArray()
arr.append(3)
arr.append(5)
arr.append(7)
arr.append(9)
arr.append(11)
arr.append(13)
arr.append(15)
arr.append(17)
arr.append(19)
arr.reveal()
print("\n Audit: len: ",len(arr),"capacity: ",arr.__getCapacity__())
