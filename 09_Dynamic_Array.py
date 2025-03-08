import ctypes
# to create C type ka array
     

class MeraList:

  def __init__(self):
    self.size = 1
    self.n = 0
    # create a C type ka array with size -> self.size
    self.A = self.__make_array(self.size)
    
  def __make_array(self,capacity):
    # referential array(C type)
    return (capacity*ctypes.py_object)()

    
  def __len__(self):
    return self.n

#Append
  def append(self,item):
    # check if vacant
    if self.n == self.size:
      # array is full -> resize
      self.__resize(self.size*2)

# append
    self.A[self.n] = item
    self.n = self.n + 1

# resize 
  def __resize(self,new_capacity):
    # create a new array with new capacity
    B = self.__make_array(new_capacity)
    self.size = new_capacity
    # copy the content of old array to new one
    for i in range(self.n):
      B[i] = self.A[i]
    # reassign A
    self.A = B


# Print
  def __str__(self):
    result = ''
    for i in range(self.n):
      result = result + str(self.A[i]) + ','

    return '[' + result[:-1] + ']'

  def __getitem__(self,index):

    if 0<= index < self.n:
      return self.A[index]
    else:
      return 'IndexError'

  
  

#pop 
  def pop(self):
    if self.n == 0:
      return 'Empty List'
    print(self.A[self.n-1])
    self.n = self.n - 1
    
# clear
  def clear(self):
    self.n = 0
    self.size = 1
    
    
#find
  def find(self,item):
    for i in range(self.n):
      if self.A[i] == item:
        return i
    return 'ValueError - not in list'

#Insert
  def insert(self,pos,item):

    if self.n == self.size:
      self.__resize(self.size*2)
    for i in range(self.n,pos,-1):
      self.A[i] = self.A[i-1]
    self.A[pos] = item
    self.n = self.n + 1
    
    # Delete

  def __delitem__(self,pos):
    # delete pos wala item
    if 0<= pos < self.n:
      for i in range(pos,self.n-1):
        self.A[i] = self.A[i+1]

      self.n = self.n - 1
      
      
#Remove
 
  def remove(self,item):
    # search and get pos
    pos = self.find(item)
    if type(pos) == int:
      # delete
      self.__delitem__(pos)
    else:
      return pos


#Sorting
  def sort(self):
    if self.n <= 1:
        return  # Already sorted if 0 or 1 element
    
    # Implementing Bubble Sort (can be replaced with another sorting algorithm)
    for i in range(self.n - 1):
        for j in range(self.n - 1 - i):
            if self.A[j] > self.A[j + 1]:  # Swap if elements are in the wrong order
                self.A[j], self.A[j + 1] = self.A[j + 1], self.A[j]

   
    
  
L=MeraList()

print(len(L))
L.append(1)
L.append('hello')
L.append(False)
L.append(4.5)
print(L)
print(L[2])

L.insert(2,50)
print(L)
L.remove("hello")
print(L)



L.append(1)
L.append(4)
L.append(3)
L.append(10)
L.append(12)
L.append(44)
L.append(31)
L.append(16)

print(L)
L.sort()
print(L)