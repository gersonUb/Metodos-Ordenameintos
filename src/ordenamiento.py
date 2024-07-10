class MetodosDeOrdenamientos:
    def __init__(self, lista):
        self.lista = lista
        self.longitud = len(lista)

    def selectionSort(self):
        for i in range(self.longitud):
            minimo = i
            for j in range(i+1, self.longitud):
                if self.lista[minimo] > self.lista[j]:
                    minimo = j
            self.lista[i], self.lista[minimo] = self.lista[minimo], self.lista[i]
        return self.lista
                
    def insertionSort(self):
        for i in range(1, self.longitud):
            actual = self.lista[i]
            j = i - 1
            while j >= 0 and actual < self.lista[j]:
                self.lista[j + 1] = self.lista[j]
                j -= 1
            self.lista[j + 1] = actual
        return self.lista

    def quickSort(self, inicio=0, fin=None):
        if fin is None:
            fin = self.longitud - 1
        if inicio < fin:
            ip = self.particion(inicio, fin) # ip = índice partición
            self.quickSort(inicio, ip - 1)
            self.quickSort(ip + 1, fin)
        return self.lista

    def particion(self, inicio, fin):
        pivote = self.lista[fin]
        i = inicio - 1
        for j in range(inicio, fin):
            if self.lista[j] <= pivote:
                i += 1
                self.lista[i], self.lista[j] = self.lista[j], self.lista[i]
        self.lista[i + 1], self.lista[fin] = self.lista[fin], self.lista[i + 1]
        return i + 1
    
    def mergeSort(self):
        if len(self.lista) > 1:
            # Encuentra el punto medio para dividir el arreglo en dos mitades
            medio = len(self.lista) // 2
            mitad_izquierda = self.lista[:medio]
            mitad_derecha = self.lista[medio:]

            # Llamada recursiva a mergeSort para ambas mitades
            izq = MetodosDeOrdenamientos(mitad_izquierda)
            der = MetodosDeOrdenamientos(mitad_derecha)
            izq.mergeSort()
            der.mergeSort()

            # Índices iniciales para las dos sublistas y la lista principal
            i = j = k = 0

            # Copia los datos a la lista temporal de izquierda y derecha
            while i < len(mitad_izquierda) and j < len(mitad_derecha):
                if mitad_izquierda[i] < mitad_derecha[j]:
                    self.lista[k] = mitad_izquierda[i]
                    i += 1
                else:
                    self.lista[k] = mitad_derecha[j]
                    j += 1
                k += 1

            # Verifica si quedan elementos en la mitad izquierda
            while i < len(mitad_izquierda):
                self.lista[k] = mitad_izquierda[i]
                i += 1
                k += 1

            # Verifica si quedan elementos en la mitad derecha
            while j < len(mitad_derecha):
                self.lista[k] = mitad_derecha[j]
                j += 1
                k += 1
        return self.lista