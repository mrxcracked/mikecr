"""
author : Miguel Camargo
date: 2020/03/25 10:10pm
documented in Spanish
"""

import matplotlib.pyplot as plt


def pide():
    lista = [1, 2, 3, 4, 5, 6, 7]
    opc = []
    i = 1
    print("""\nIngrese las 3 opciones de codificación (Separadas por un Enter):\n
    1) TTL
    2) NRZ-L
    3) NRZ-I
    4) BIPOLAR
    5) PSEUDOTERNARIA
    6) MANCHESTER
    7) MANCHESTER DIFERENCIAL
    """)
    while i < 4:
        print('\n', i, ': ', end='')
        res = int(input())
        if res in lista:
            opc.append(res)
            i += 1

        else:
            print('Opción inválida!')

    return opc


def selecciona(opc, pos, li):
    if opc == 1:
        plt.subplot(4, 1, pos)
        plt.ylabel("TTL")
        plt.grid(linestyle='-', linewidth=2)
        plt.plot(ttl(li),color='cyan',drawstyle='steps-post', marker='>', linewidth=2)
    if opc == 2:
        plt.subplot(4, 1, pos)
        plt.ylabel("NRZ-L")
        plt.grid(linestyle='-', linewidth=2)
        plt.plot(polar_nrz_l(li),color='blue',drawstyle='steps-post',marker='>', linewidth=2)
    if opc == 3:
        plt.subplot(4, 1, pos)
        plt.ylabel("NRZ-I")
        plt.grid(linestyle='-', linewidth=2)
        plt.plot(polar_nrz_i(li),color='green',drawstyle='steps-post',marker='>', linewidth=2)
    if opc == 4:
        plt.subplot(4, 1, pos)
        plt.ylabel("Bipolar") #A-M-I
        plt.grid(linestyle='-', linewidth=2)
        plt.plot(AMI(li),color='blue',drawstyle='steps-post',marker='>', linewidth=2)
    if opc == 5:
        plt.subplot(4, 1, pos)
        plt.ylabel("Pseudoternaria")
        plt.grid(linestyle='-', linewidth=2)
        plt.plot(pseudoternary(li),color='red',drawstyle='steps-post',marker='>', linewidth=2)
    if opc == 6:
        plt.subplot(4, 1, pos)
        plt.ylabel("Manchester")
        plt.grid(linestyle='-', linewidth=2)
        plt.plot(manchester(li),color='violet',drawstyle='steps-post',marker='>', linewidth=2)
    if opc == 7:
        plt.subplot(4, 1, pos)
        plt.ylabel("Manchester Diferencial")
        plt.grid(linestyle='-', linewidth=2)
        plt.plot(Differential_manchester(li),color='red',drawstyle='steps-pre',marker='>', linewidth=2)


def plot(li):
    plt.subplot(4, 1, 1)
    plt.ylabel("CLK")
    plt.grid(linestyle='-', linewidth=2)
    plt.plot(clock(li), drawstyle='steps-post', linewidth=2, marker='o')
    plt.show()


def clock(inp1):
    tam = 2 * len(inp1) + 1
    c = [0, 1]
    c = c * tam
    li = []
    for i in range(tam):
        li.append(c[i])

    return li


def ttl(inp):
    li = []
    inp1 = list(inp)
    inp1.append(inp1[len(inp1)-1])
    for i in range(len(inp1)):
        if inp1[i] == 0:
            li.append(0)
        if inp1[i] == 1:
            li.append(5)
    return li

def polar_nrz_l(inp):
    inp1=list(inp)
    li = []
    inp1.append(inp1[len(inp1)-1])
    for i in range(len(inp1)):
        if inp1[i] == 0:
            li.append(5)
        if inp1[i] == 1:
            li.append(-5)
    return li


def polar_nrz_i(inp):
    inp2=list(inp)
    lock=False
    inp2.append(inp2[len(inp2)-1])
    for i in range(len(inp2)):
        if inp2[i]==1 and not lock:
            lock=True
            continue
        if lock and inp2[i]==1:
            if inp2[i-1]==0:
                inp2[i]=5
                continue
            else :
                inp2[i]=0
                continue
        if lock:
            inp2[i]=inp2[i-1]
    inp2=[-5 if i==0 else 5 for i in inp2]
    return inp2


def manchester(inp):
    inp1=list(inp)
    li, lock =[], False
    inp1.append(inp1[len(inp1) - 1])
    for i in range(len(inp1) - 1):
        if inp1[i]==0:
            li.append(5)
            li.append(-5)
        if inp1[i]==1:
            li.append(-5)
            li.append(5)
    if inp1[len(inp1) - 1] == 0:
        li.append(-5)
    elif inp1[len(inp1) - 1] == 1:
        li.append(5)
    return li


def Differential_manchester(inp):
    inp1=list(inp)
    li,lock,pre=[],False,''
    inp1.append(inp1[len(inp1) - 1])
    for i in range(len(inp1) - 1):
        if inp1[i]==0 and not lock:
            li.append(-5)
            li.append(-5)
            li.append(5)
            lock=True
            pre='S'
        elif inp1[i]==1 and not lock :
            li.append(5)
            li.append(5)
            li.append(-5)
            lock=True
            pre='Z'
        else:
            if inp1[i]==0:
                if pre=='S':
                    li.append(-5);li.append(5)
                else:
                    li.append(5);li.append(-5)
            else:
                if pre=='Z':
                    pre='S'
                    li.append(-5);li.append(5)
                else:
                    pre='Z'
                    li.append(5);li.append(-5)
        if li[len(li) - 1] == 5: li.append(5)
        elif li[len(li) - 1] == -5: li.append(-5)
    return li


def AMI(inp):
    inp1=list(inp)
    li = []
    lock=False
    inp1.append(inp1[len(inp1)-1])
    for i in range(len(inp1)):
        if inp1[i] == 0:
            li.append(0)
        if inp1[i]==1 and not lock:
            li.append(5)
            lock=True
            continue
        elif lock and inp1[i]==1:
            li.append(-5)
            lock=False
    return li


def pseudoternary(inp):
    li, lock = [], False
    inp1=list(inp)
    inp1[0] = 5
    inp1.append(inp1[len(inp1)-1])
    for i in range(len(inp1)):
        if inp1[i] == 5:
            li.append(5)
        if inp1[i] == 1:
            li.append(0)
        if inp1[i] == 0 and not lock:
            li.append(-5)
            lock = True
            continue
        elif lock and inp1[i] == 0:
            li.append(5)
            lock = False

    return li


if __name__ == '__main__': # Parte principal del programa
    li = []  # Lista que contiene los números binarios
    lista = ['hex', 'oct', 'h', 'o', 'b', 'bin'] # Valida opciones
    base = input("Elija la base de su número (hex/oct/bin): ").lower()
    if (base not in lista): # Rechaza opciones no listadas
        print("Opción incorrecta.")
        exit() # Termina la ejecución del programa
    num = input("Ingrese su numero: ") # Recoge el número tecleado
    if (base == 'hex' or base == 'h'): # Opción hexadecimal
        base = len(num) * 4 # 4 bits por cada cifra hexa.
        b = bin(int(num, 16))[2:].zfill(base) # Rellena con 0s
        # a la izquierda de ser necesario
        print('num. a binario: ', b) # Imprime la conversión hex. a bin.

    elif (base == 'oct' or base == 'o'): # Opción octal
        base = len(num) * 3 # 3 bits por cada cifra hexa.
        b = bin(int(num, 8))[2:].zfill(base) # Rellena con 0s
        print('num. a binario: ', b) # Imprime la conversión oct. a bin.

    elif base == 'bin' or base == 'b': # Opción binaria
        b = '' # String auxiliar
        for i in range(len(num)): # Recorre el número ingresado (list)
            b += num[i] # Las copia en el String

    for j in str(b): # Recorre el String
        li.append(int(j)) # Los convierte a enteros y
        # Copia los elementos en una lista


    query = pide() # Función para pedir número, base y 3 opciones
    # Vuelve con las 3 opciones en una lista

    for r in range(len(query)): # Recorre lista de opciones
        pos = r + 2 # Posición de subplot
        opc = query[r] # Número de opción en lista
        selecciona(opc, pos, li)
        '''
        Función para selección de técnica de
        codificación. Se envía opción elegida, la posición de subplot,
        y el número binario almacenado en una lista.
        '''

    plot(li) # Función que muestra los resultados
