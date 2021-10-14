from DLL import DoubleLinkedList
DLL = DoubleLinkedList()
DLL.append(5)
DLL.append(10)
DLL.append(15)
print('\nLista inicial: ')
DLL.show_elements()
print(f'\nValor insertado: {DLL.insert(3,21)} ')
DLL.show_elements()
print(f'\nValor eliminado: {DLL.delete(2)}')
DLL.show_elements()
print('\nLista invertida')
DLL.reverse()
DLL.show_elements()
print('\nLista invertida y elevar al cuadrado')
DLL.reverse_and_pow()
DLL.show_elements()




