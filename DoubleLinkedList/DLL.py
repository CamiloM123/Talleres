class DoubleLinkedList:
  class Node:
    #Contructor de la clase Node
    def __init__(self,value):
      self.value = value
      self.prev = None
      self.next = None
  #Constructor de la clase DLL   
  def __init__(self):
    self.head = None
    self.tail = None
    self.lenght = 0
  
  def show_elements(self):
    array=[]
    current_node = self.head
    while (current_node != None):
      array.append(current_node.value)
      current_node = current_node.next
    return print(array)

  def append(self,value):
    new_node = self.Node(value)
    if(self.head == None and self.tail == None):
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
    self.lenght += 1
    return new_node.value
  
  def unshift(self,value):
    new_node = self.Node(value)
    if(self.head == None and self.tail == None):
      self.head = new_node
      self.tail = new_node
    else:
      self.head.prev = new_node
      new_node.next = self.head
      self.head = new_node
    self.lenght += 1
    return new_node.value
  
  def show_lenght(self):
    return print(self.lenght)
  
  def pop(self):
    if(self.lenght == 1):
      self.head = self.tail = None
    elif self.lenght == 0:
      return None
    else:
      remove_node = self.tail
      self.tail = remove_node.prev
      self.tail.next = None
      remove_node.prev = None
    self.lenght -= 1
    return None

  def shift(self):
    if(self.lenght == 1):
      self.head = self.tail = None
      self.lenght -= 1
    elif self.lenght == 0:
      return None
    else:
      remove_node = self.head
      self.head = remove_node.next
      remove_node.prev = None
      self.lenght -= 1
    return None

  def get (self,index):
    count = 1
    current_node = self.head
    if(index < 0 or index > self.lenght):
      return None
    else:
      while(count != index ):
        current_node = current_node.next
        count += 1
      return current_node
    
  def set(self, index, value):
    update_node = self.get(index)
    if update_node != None:
      update_node.value = value
    else:
      return None

  def insert(self,index ,value):
    if index == self.lenght+1:
      return self.append(value)
    elif  (index > 1 and index <= self.lenght):
      new_node = self.Node(value)
      index_node = self.get(index)
      current_node = index_node.prev
      current_node.next = new_node
      index_node.prev = new_node
      new_node.next = index_node
      new_node.prev = current_node
      self.lenght += 1
      return new_node.value
    elif index == 1:
      return self.unshift(value)
    else:
      return None

  def delete(self,index):
    if index == self.lenght:
      self.pop()
      return self.tail.value
    elif  (index > 1 and index < self.lenght):
      delete_node = self.get(index)
      prev_node = delete_node.prev
      next_node = delete_node.next
      prev_node.next = next_node
      next_node.prev = prev_node
      self.lenght -= 1
      return delete_node.value
    elif index == 1:
      self.shift()
      return self.head.value
    else:
      return None

  def reverse_elements(self):
    array=[]
    current_node = self.tail
    while (current_node != None):
      array.append(current_node.value)
      current_node = current_node.prev
    return print(array)
  
  def reverse(self):
    reverse = None
    current_node = self.head
    self.tail = current_node
    while current_node != None:
      reverse = current_node.prev
      current_node.prev = current_node.next
      current_node.next = reverse
      current_node = current_node.prev
    self.head = reverse.prev
  
  def reverse_and_pow(self):
    self.reverse()
    count = 1
    current_node = self.head
    while (count<=self.lenght):
      node = self.get(count)
      self.set(count, node.value**2)
      current_node = current_node.next
      count +=1

