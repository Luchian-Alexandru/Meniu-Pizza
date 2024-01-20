import time
print('''
    Meniu Pizza
    
1. Margherita   - 4.2 RON
2. Diavolo      - 4.5 RON
3. Funghi       - 4.5 RON
4. Prosciuto    - 4.8 RON
5. Mamamia      - 6.1 RON
6. Dracula      - 5.5 RON
7. Piedone      - 6.8 RON
8. Americana    - 4.3 RON
9. Mexicana     - 5.2 RON
0. Finalizare comanda
''')
total = float(0)
Pizza_1 = 4.2
Pizza_2 = 4.5
Pizza_3 = 4.5
Pizza_4 = 4.8
Pizza_5 = 6.1
Pizza_6 = 5.5
Pizza_7 = 6.8
Pizza_8 = 4.3
Pizza_9 = 5.2
while True:
    pizza = int(input('Alege comanda: ',))
    if pizza == 1:
        total += Pizza_1
    elif pizza == 2:
        total += Pizza_2
    elif pizza == 3:
        total += Pizza_3
    elif pizza == 4:
        total += Pizza_4
    elif pizza == 5:
        total += Pizza_5
    elif pizza == 6:
        total += Pizza_6
    elif pizza == 7:
        total += Pizza_7
    elif pizza == 8:
        total += Pizza_8
    elif pizza == 9:
        total += Pizza_9
    elif pizza == 0:
        print('Totalul este :', total,'Ron')
        print('Introduceti adresa de livrare')
        Oras = input('Oras: ')
        Strada = input('Stada: ')
        Numar = input('Numar: ')
        print('Cum doriti sa platit:')
        print('''
1.La livrare
2.Cu cardul
''')
        Plata = int(input())
        if Plata == 1:
            print('Comanda dumneavoastra:')
            time.sleep(1)
            print('Total comanda :', total, "Ron")
            time.sleep(1)
            print('Adresa de livreare: ', 'Oras : ', Oras, 'Strada : ', Strada, 'Numar : ', Numar)
            time.sleep(1)
            print('Comanda va ajunge la dumneavoastra in maxim 30 minute!')
            break
        elif Plata == 2:
            print(input('Introduceti numarul cardului: '))
            print(input('Introduceti numele complet: '))
            print(input('Introduceti codul de securitate de pe spatele cardului: '))
            print('Procesare plata...')
            time.sleep(1)
            print('Plata finalizata!')
            time.sleep(1)
            print('Comanda dumneavoastra:')
            time.sleep(1)
            print('Totalul comenzi :', total, "Ron")
            time.sleep(1)
            print('Adresa de livrare: ', 'Oras : ', Oras, 'Stada : ', Strada, 'Numar : ', Numar)
            time.sleep(1)
            print('Comanda va ajunge la dumneavoastra in maxim 30 minute!')
            break
