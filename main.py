'''
4. Feladat
Írj egy programot, amely a felhasználótól bekér 3 szót, ezeket egy listában tárolja, és egy eljárás segítségével meghatározza, és a képernyőre kiírja, melyik a legrövidebb szó!
'''
lista = []

beker1 = (input('Kérek egy szót: '))
beker2 = (input('Kérek egy szót: '))
beker3 = (input('Kérek egy szót: '))

lista.append(beker1)
lista.append(beker2)
lista.append(beker3)

def legrovidebb():
    for i in range(1):
        print("A legrövidebb szó : ", min(lista, key=len))
legrovidebb()
    