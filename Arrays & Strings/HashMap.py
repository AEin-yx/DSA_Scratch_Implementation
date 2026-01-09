# Hash Map Implementation

class HashMap:
    def __init__(self, init_capacity:int=16,load_factor:float=0.75):
        self.capacity = init_capacity
        self.load_factor = load_factor
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    def _hash(self,key):
        return hash(key) % self.capacity

    def put(self,key,value):
        idx = self._hash(key) # to find the index of the bucket
        
        # Check if the key already exists and replace it
        bucket = self.buckets[idx]
        for i,(k,v) in enumerate(bucket):
            if k==key:
                bucket[i] = (key, value)
                return
        
        # Place the key-value pair in the bucket
        self.buckets[idx].append((key,value))
        self.size += 1
        
        # check if resize is needed
        if self.size / self.capacity > self.load_factor:
            self._resize(2*self.capacity) 
    
    def remove(self,key)->bool:
        idx = self._hash(key)
        bucket = self.buckets[idx]

        print("The bucket is removed: ")
        for i,(k,v) in enumerate(bucket):
            if k==key:
                bucket.pop(i)
                self.size -= 1
                print("The bucket with key: ",key," is removed: ")
                return True
        return False

    def get(self,key):
        idx = self._hash(key)
        bucket = self.buckets[idx]

        for i,(k,v) in enumerate(bucket):
            if k==key:
                print("The value with key: ",key," is : ",v)
                return v
        return None

    def retrieve(self):
        print("The buckets list is: ")
        for bucket in self.buckets:
            print(bucket)

    def _resize(self,new_capacity):
        old_buckets = self.buckets
        self.capacity = new_capacity
        self.size = 0
        self.buckets = [[] for _ in range(new_capacity)]

        # Rehash all the existing key-value pairs
        for bucket in old_buckets:
            for key,value in bucket:
                self.put(key,value)
    
    def _current_load_factor(self):
        return self.size / self.capacity
        
hmap = HashMap()
hmap.put("a","apple")
hmap.put("b","banana")
hmap.put("c","cherry")
hmap.put("d","date")
hmap.put("e","elderberry")
hmap.put("f","fig")
hmap.put("g","grape")
hmap.put("h","honeydew")
hmap.put("i","kiwi")
hmap.put("j","lemon")
hmap.put("k","lime")
hmap.put("l","lychee")
hmap.put("m","mango")
hmap.put("n","orange")
hmap.put("o","papaya")
hmap.put("p","pineapple")
hmap.put("q","quince")
hmap.put("r","raspberry")
hmap.put("s","strawberry")
hmap.put("t","tomato")
hmap.put("u","ugli")
hmap.put("v","vanilla")
hmap.put("w","watermelon")
hmap.put("x","xigua")
hmap.put("y","yellowberry")
hmap.put("z","zucchini")

hmap.retrieve()
hmap.get('s')
hmap.get('h')
hmap.get('i')
hmap.get('n')
hmap.put("i","irum")
hmap.put("n","nalo")
print("Testing............")
hmap.get('s')
hmap.get('h')
hmap.get('i')
hmap.get('n')

print("\n\nThe current load factor is: ",hmap._current_load_factor())
