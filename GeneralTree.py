#SUCESSOR => HIJO
#PREDECESSOR => PADRE
class treeClass:
  class appendClass:
    #La clase árbol utiliza la clase nodo
    class treeNodeClass:
      def __init__(self, value, predecessor):
        self.value = value
        self.predecessor = predecessor
        #Generar el enlace entre niveles del árbol
        self.sucessor = None
        #next permite conectar sucesor con predecesor
        self.next = None
    
    #Constructor de la clase append_method (LL)
    def __init__(self):
      self.head = None
      self.tail = None
      self.length = 0
  
    #Crear un nuevo Nodo al final del recorrido de uno de los lados del árbol
    def append(self, value, predecessor):
      new_node = self.treeNodeClass(value, predecessor)
      #Si el árbol esta vacío
      if self.head == None and self.tail == None:
        self.head = new_node
        self.tail = new_node
        self.tail.next = self.head
      #El árbol no esta vacío
      else:
        self.tail.next = new_node
        new_node.next = self.head
        self.tail = new_node
      self.length += 1

  #Constructor del treeClass
  def __init__(self):
    self.root = None
    self.length = 0 
  
  #Para insertar un nuevo nodo se necesita conocer el value y el nodo predecessor
  def insert(self, value, predecessor):
    #Validar si el árbol no tiene raíz
    if self.root == None:
      #Instanciamos la clase de appendClass
      self.root = self.appendClass()
      #Como la raíz de un árbol NO tiene sucesor, se deja None
      self.root.append(value, None)

    #Caso contrario: ya existe el nodo raíz
    else:
      #Iniciamos el recorrido en la raíz
      current_node = self.root.head
      #El test_node esta un nivel más arriba de los niveles visitados a profundidad
      def tree_route(node, test_node=None):
        auxiliar_node = node.predecessor
        if value == predecessor:
          return False
        #Estamos en un nodo predecessor
        elif node.value == predecessor:
          #Si el nodo predecessor no tiene sucessor
          if node.sucessor == None:
            #Instanciamos la clase de appendClass
            node.sucessor = self.appendClass()
            node.sucessor.append(value, node)
            self.length += 1
            return True
          else:
            node.sucessor.append(value, node)
            self.length += 1
            return True
        else:
          #Si si hay un nodo sucessor
          if node.sucessor != None:
            #Validar si el Vvalue  del nodo sucessor es igual al del nodo de prueba
            if node.sucessor.head.value == test_node:
              if node.value == self.root.head.value:
                return False
              elif node.next.value != auxiliar_node.sucessor.head.value:
                return tree_route(node.next, node.value)
              else:
                return tree_route(node.predecessor, node.next.value)
            else:
              return tree_route(node.sucessor.head, node.sucessor.head.value)
          elif node.next.value != auxiliar_node.sucessor.head.value:
            return tree_route(node.next, node.value)
          #Si no hay nodo sucessor
          else:
            return tree_route(node.predecessor, node.next.value)
      return tree_route(current_node)

#SUCESSOR => HIJO
#PREDECESSOR => PADRE
  def find_node(self, value):
    current_node = self.root.head
    def tree_route(node, node_validator = None):
      node_aux = node.predecessor
      if node.value == value:
        return node.value
      elif node.sucessor != None:
        if node.sucessor.head.value == node_validator:
          if node.value == self.root.head.value:
            return "No existe el nodo  buscado"
          elif node.next.value != node_aux.sucessor.head.value:
            return tree_route(node.next, node.value)
          else:
            return tree_route(node.predecessor, node.next.value)
        else:
          return tree_route(node.sucessor.head, node.sucessor.head.value)
      elif node.next.value != node_aux.sucessor.head.value:
        return tree_route(node.next, node.value)
      else:
        return tree_route(node.predecessor, node.next.value)
    node_find = tree_route(current_node)
    return print(node_find)

  #Si el árbol tiene un único elemento, dicho elemento es el listado en preorden. 
  # Raíz - subárboles de izq a der
  def route_preorder(self):
    list_nodes = []
    current_node = self.root.head
    def route(nodo, node_test=None):
      nodo_aux = nodo.predecessor
      if nodo.sucessor != None:
          if nodo.sucessor.head.value  == node_test:
              if nodo.value  == self.root.head.value :
                  return None
              elif nodo.next.value  != nodo_aux.sucessor.head.value :
                  return route(nodo.next, nodo.value )
              else: 
                  return route(nodo.predecessor, nodo.next.value)
          else:
              list_nodes.append(nodo.value)
              return route(nodo.sucessor.head, nodo.sucessor.head.value)
      elif nodo.next.value != nodo_aux.sucessor.head.value:
          list_nodes.append(nodo.value)
          return route(nodo.next, nodo.value)
      else:
          list_nodes.append(nodo.value)
          return route(nodo.predecessor, nodo.next.value)
    route(current_node)
    return print(list_nodes)

  #Subárboles de izq a der - Raíz
  def postorder(self):
    list_nodes = []
    current_node = self.root.head
    def route(nodo, node_test=None):
        nodo_aux = nodo.predecessor
        if nodo.sucessor != None:
          if nodo.sucessor.head.value == node_test:
            list_nodes.append(nodo.value)
            if nodo.value == self.root.head.value:
              return None
            elif nodo.next.value != nodo_aux.sucessor.head.value:
              return route(nodo.next, nodo.value)
            else: 
                return route(nodo.predecessor, nodo.next.value)
          else:
            return route(nodo.sucessor.head, nodo.sucessor.head.value)
        elif nodo.next.value != nodo_aux.sucessor.head.value:
            list_nodes.append(nodo.value)
            return route(nodo.next, nodo.value)
        else:
            list_nodes.append(nodo.value)
            return route(nodo.predecessor, nodo.next.value)
    route(current_node)
    return print(list_nodes)