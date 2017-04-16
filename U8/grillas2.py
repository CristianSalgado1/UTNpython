import random
while True:
    rta=[]
    todosDados={}
    while(True):
        print('Cuantos dados?')
        dadosq=int(input())
        print('De cuanto?')
        dadosDe=int(input())
        todosDados[dadosDe]=dadosq
        print('alguno mas? y/n')
        fin=input()       
        if fin=='n':
            break
    for k, v in todosDados.items():
        b=int(v)
        c=[]
        while b>0:
            c.append(random.randint(1,int(k)))
            b=b-1
        d=sum(int(i) for i in c)
        todosDados[k]=d

    print(todosDados)
    print(sum(todosDados.values()))
    print('Quieres Continuar? y/n')
    salir=input()
    if salir=='n':
        break



