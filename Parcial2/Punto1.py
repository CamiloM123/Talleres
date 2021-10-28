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
  
  #Primer punto
  def punto1(self):
    print('Punto 1: Observe la siguiente lista ')
    self.show_elements()
    numero = int(input('\nIngrese un numero al final de la lista que cumpla la secuencia: '))
    if(self.validarValor(numero)):
      self.append(numero)
      print('\n ¡¡¡Felicitaciones, encontró el patrón!!!!')
      self.show_elements()
    else:
      print('Ese valor no es el siguiente en la secuencia')

  #Auxiliar del primer punto
  def validarValor(self,value):
    auxArray = []
    aux = 1
    for i in range (self.lenght):
      aux += 2
      auxArray.append(aux)
    #Obtener el numero para validar
    validar = auxArray[self.lenght-1] + self.tail.value

    #Validar
    if(validar == value):
      return True
    else:
      return False

  #Segundo punto
  

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