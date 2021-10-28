class Circular_SLL:
  class Node:
    def __init__(self, value):
      self.value = value
      self.next = None

  def __init__(self):
    self.head = None
    self.tail = None
    self.lenght = 0

  #Punto 2
  def punto2(self):
    intentosNodo1 = 3
    flag1 = False
    intentos1 = 1
    intentosNodo2 = 3
    flag2 = False
    intentos2 = 1
    print('Punto 2: Observe la siguiente lista\n')
    self.show_circular_SLL()
    print('\n*****El objetivo consiste en ingresar un valor en los nodos con valor "0" que cumpla la secuencia, va a tener tres intentos por cada nodo****** ')
    #Primero nodo
    
    while (intentosNodo1 != 0 and flag1 != True ):
      print(f'\n***Este es el intento {intentos1} del nodo 1***')
      numeroNodo1 = int(input('>>>>> '))
      validar = self.validarNodo(3)
      if(numeroNodo1 == validar):
        print('¡¡¡Correcto, ese es el numero!!\n')
        flag1 = True
        self.set(4,numeroNodo1)
      else:
        print('\n--- El numero no es el correcto :c ---')
        intentosNodo1 -= 1
        intentos1 += 1

    #Segundo nodo
    if(flag1):
      self.show_circular_SLL()
      while (intentosNodo2 != 0 or flag2 != True ):
        print(f'\n***Este es el intento {intentos2} del nodo 2***')
        numeroNodo2 = int(input('>>>>> '))
        validar = self.validarNodo(4)
        if(numeroNodo2 == validar):
          print('¡¡¡Correcto, ese es el numero!!!')
          print('El juego se ha completado')
          flag2 = True
          self.set(5,numeroNodo2)
          break
        else:
          print('***El numero no es el correcto :c***')
          intentosNodo2 -= 1
          intentos2 +=1
    else:
      print("Se acabó el juego, intentelo nuevamente")
      
    #Validar si perdió el juego en el segundo nodo
    if(intentosNodo2 == 0):
      print("Se acabó el juego, intentelo nuevamente")


  def validarNodo (self,index):
    auxNodo = self.get(index)
    validar = auxNodo.value + 7
    return validar

  #Auxiliares
  def show_circular_SLL(self):
    array = []
    current_node = self.head
    count = self.lenght
    while count != 0:
      array.append(current_node.value)
      current_node = current_node.next
      count -= 1
    return print(array)  
    
  def append(self, value):
    new_tail = self.Node(value)
    if self.lenght == 0:
      self.head = self.tail = new_tail
    else:
      new_tail.next = self.head
      self.tail.next = new_tail
      self.tail = new_tail
    self.lenght +=1
    return new_tail

  def get(self, index):
    index += 1
    if index == self.lenght:
      return self.tail
    elif index == 1:
      return self.head
    elif index > 0  and index < self.lenght:
      current_node = self.head
      count = 1
      while count != index:
        current_node = current_node.next
        count += 1
      return current_node
    else:
      return None

  def set(self,index,value):
    set_node = self.get(index)
    if set_node == None:
      print('El indice no se encuentra')
    else:
      set_node.value = value