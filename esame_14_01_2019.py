def massimo(lista):
    max_val = 0

    if len(lista) == 1:
        return lista[0]

    else:

        tmp = lista[len(lista)-1]

        max_val = massimo(lista[:-1])

        if tmp > max_val:
            return tmp
        else:
            return max_val

if __name__ == "__main__":
    l = [12, 45, 23, 88, 1, 9, 67]
    print(massimo(l))