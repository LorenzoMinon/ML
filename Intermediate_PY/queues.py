import queue

# Crear una cola vacía
# cola = Queue()

# # Agregar elementos a la cola
# cola.put(1)
# cola.put(2)
# cola.put(3)

# # Obtener el tamaño de la cola
# tamaño = cola.qsize()
# print("Tamaño de la cola:", tamaño)

# # Verificar si la cola está vacía
# vacía = cola.empty()
# print("¿La cola está vacía?", vacía)

# # Obtener el primer elemento de la cola
# primer_elemento = cola.get()
# print("Primer elemento de la cola:", primer_elemento)

# # Obtener el tamaño actualizado de la cola
# tamaño = cola.qsize()
# print("Tamaño de la cola:", tamaño)



q = queue.PriorityQueue()

q.put(3, "Hola")
q.put(1, "Mundo")
q.put(2, "Python")

print(q.qsize())
print(q.get())
print(q.empty())