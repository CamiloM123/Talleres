class ClassLinkedList:
  class Node:
    def __init__(self,value):
      self.value = value
      self.next = None
    def __str__(self):
      return str(self.value)
  
  def __init__(self):
    self.head = None
    self.lenght = 0
    self.tail = None

  #Menu
  def menu(self):
    flag = False
    option = 0
    option = int(input('\n    ¿Qué deseas hacer?\n    1.Hallar la raiz cuadrada y añadirlo al inicio\n    2.Eliminar nodo y añadir el cuadrado de este al final\n    3.Revertir la lista\n    4.Salir\n   >>>>>>> '))
    while flag != True:
      if option != 1 and option !=2 and option !=3 and option != 4:
        option = int(input('    ¿Qué deseas hacer?\n    1.Hallar la raiz cuadrada y añadirlo al inicio\n    2.Eliminar nodo y añadir el cuadrado de este al final\n    3.Revertir la lista\n    4.Salir\n   >>>>>>> '))
      elif option == 1:
        self.raiz_cuadrada()
        self.menu()
        flag = True
      elif option == 2:
        self.elevar_borrar()
        self.menu()
        flag = True
      elif option == 3:
        self.reverse()
        self.menu()
        flag = True
      else:
        print('**Gracias por acceder al menu**')
        flag = True

  #Funciones principales
  def reverse(self):
    head = self.head
    preview = None
    current= None
    while(head != None):
      current = head.next
      head.next = preview
      preview = head
      head = current

    self.head = preview
    print('\n')
    self.show_elements()
    return None

  def elevar_borrar(self):
    flag = False
    self.show_elements()
    while flag != True:
      try:
        index = int(input('Ingrese el indice: '))
        node = self.get(index)
        new_value = node.value**2
        self.remove(index)
        self.append(new_value)
        print('\n')
        self.show_elements()
        flag = True
      except ValueError:
        print('Error, se esperaba un numero')
    return None

  def raiz_cuadrada(self):
    flag = False
    self.show_elements()
    while flag != True:
      try:
        index = int(input('Ingrese el indice: '))
        node = self.get(index)
        new_value = node.value**0.5
        self.prepend(new_value)
        print('\n')
        self.show_elements()
        flag = True
      except ValueError:
        print('Error, se esperaba un numero')
    return None
  
  def delete_specific_value(self):
    value = int(input('Ingrese el valor de la lista que desea eliminar: '))
    count = 0
    delete_node = None
    current_node = self.head
    while current_node.next != None:
      if current_node.value == value:
        delete_node = current_node
        break   
      else:
        current_node = current_node.next
        count += 1
    if delete_node != None:
      self.remove(count)
      self.lenght -= 1
      return delete_node
    elif current_node.value == value:
      self.remove(count)
      self.lenght -= 1
      return current_node
    else:
      return None

  #Auxiliares

  def initialize_nodes(self):
    while True:
      try:
        cant = int(input('Ingrese la cantidad de nodos que quiere crear: '))
        for i in range (cant):
          value_node = int(input('Ingresa el valor del nodo: '))
          self.append(value_node)
        break
      except ValueError:
        print('Error, se esperaba un numero')

  def prepend(self ,value):
    new_Node = self.Node(value)
    if self.head == None and self.tail == None:
      self.head = new_Node
      self.tail = new_Node
    else:
      new_Node.next = self.head
      self.head = new_Node
    #Actualizamos el tamaño de la lista
    self.lenght +=1

  def append(self, value):
    new_node = self.Node(value)
    if self.head == None and self.tail == None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    self.lenght += 1
    
  def show_elements(self):
    array = []
    current_none = self.head
    while current_none != None:
      #Mientras si exista un elemento en la cabeza de la lista, el valor se añade a la lista array
      array.append(current_none.value)
      current_none = current_none.next
    print(array)    

  def pop(self):
    if self.lenght == 0:
      self.head = None
      self.tail = None
    else:
      #Recorremos toda la lista para identificar el ultimo elemento
      current_node = self.head
      while current_node.next != None:
        new_tail = current_node
        current_node = current_node.next
      self.tail = new_tail
      self.tail.next = None
      self.lenght -= 1
      return current_node

  def shift(self):
    if self.lenght == 0:
      self.head = None
      self.tail = None
    else:
      delete_node = self.head
      self.head = delete_node.next
      delete_node.next = None
    self.lenght -= 1
    return delete_node
  
  def remove(self,index):
    if index == 0:
      return self.shift()
    elif index == self.lenght -1:
      return self.pop()
    elif not( index >= self.lenght or index < 0):
      preview_node = self.get(index-1)
      delete_node = preview_node.next 
      preview_node.next = delete_node.next
      delete_node.next = None
      self.lenght -=1
      return delete_node
    else:
      return None 

  def get(self,index):
    if index == self.lenght-1:
      print(f'El valor del indice es {self.tail.value}')
      return self.tail
    elif index == 0:
      print(f'El valor del indice es {self.head.value}')
      return self.head
    elif not (index >= self.lenght or index<0):
      current_node = self.head
      visit_node_count = 0
      while visit_node_count != index:
        current_node = current_node.next
        visit_node_count += 1
      print(f'El valor del indice es {current_node.value}')
      return current_node
    else:
      return None 
