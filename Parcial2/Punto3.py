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
  
  def punto3(self):
    for i in range(6):
      numero = int(input('Ingrese un numero de estacionamiento: '))
      self.append(numero)
    self.show_elements()

  #Auxiliares
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