#Clase arbol binario
class BinaryTree:
    #Clase nodo
    class Node:
        #Bloque de inicializacion para la clase nodo
        def __init__(self,value):
            self.value = value
            self.left = None
            self.right = None
    #Bloque de inicializacion para la clase arbol
    def __init__(self):
        self.root = None
        self.size = 0
        self.array = []

    #Menu
    def menu(self):
      root = 0
      root = int(input('Ingrese el valor de la raiz >>>>>>> '))
      verificar = self.verificarRaiz(root)
      if(verificar):
        self.array.append(root)
        self.add(root)
        numeroNodos = int(input('Ingrese la cantidad de nodos que quiere agregar >>>>>>> '))
        self.addMenu(numeroNodos)
      else:
        while True:
          print('*****El numero de la raiz no está entre los valores permitidos*****')
          root = int(input('Ingrese el valor de la raiz >>>>>>> '))
          verificar = self.verificarRaiz(root)
          if(verificar):
            self.add(root)
            numeroNodos = int(input('Ingrese la cantidad de nodos que quiere agregar >>>>>>> '))
            self.addMenu(numeroNodos)
            break
      print('\nEl recorrido en inorden es: ')
      self.inorden(self.root)
      

    #Auxiliares
    def addMenu(self,numeroNodos):
      for i in range (numeroNodos):
        number = int(input('Ingrese el valor del nodo, no debe haber valores duplicados: '))
        aux = self.verificarNodo(number)
        if (aux):
          self.array.append(number)
          self.add(number)
        else:
          while True:
            print('*****El numero no está entre los valores permitidos, no debe haber valores duplicados*****')
            number = int(input('Ingrese el valor del nodo, no debe haber valores duplicados: '))
            aux = self.verificarNodo(number)
            if (aux):
              self.array.append(number)              
              self.add(number)
              break

    def verificarRaiz(self,root):
      return True

    def verificarNodo(self, number):
      if number in self.array:
        return False
      else:
        return True

    #Funcion para agregar un nodo al arbol
    def add(self,value):
        self.addAux(self.root,value)

    def addAux(self,node,value):
        insertNode = self.Node(value)
        if node is None:
            self.root = insertNode
            self.size += 1
        elif value == node.value:
            return "El nodo no se puede agregar"
        elif value < node.value:
            if node.left is None:
                node.left = insertNode
                self.size += 1
            else:
                self.addAux(node.left,value)
        else:
            if node.right is None:
                node.right = insertNode
                self.size += 1
            else:
                self.addAux(node.right,value)

    #Recorridos
    def inorden(self, node:Node)-> None:
        if node is not None:
            self.inorden(node.left)
            print(node.value , end=", ")
            self.inorden(node.right)