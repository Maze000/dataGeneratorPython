import random
lista=["uno","dos","tres","cuatro","cinco"]
def  cuenta():
 a=0
 for le in range(8):
     if a<4:
          print(lista[a])
     else:
         a=0
         print(lista[a])
     a=a+1
def cadena():
    print(str(round(random.random()+random.randint(1,100),2)))
 
def formato():
 print ("%.2f"%random.random())
 
let=["uno","dos","tres"]
num=[1,2]
def doble():
     for a in range(3):
           for b in range(2):
               print(let[a]+str(num[b]))
               
def fecha(mes,dia,ano):
    dias=[0]*(mes*dia)
    for a in range(mes):
         for b in range(dia):
              dias[b]=(str(b+1)+"/"+str(a+1)+"/"+str(ano))
    #print(dias)
    return dias
def fecha0():
    for a in range(1):
        for b in range(28):
            print(str(b+1)+"/"+str(a+1)+"/"+"2020")
 
def  fecha1(dias):
    s=[0]*dias
    for a in range(1):
         for b in range(dias):
              
              s[b]=str(b+1)+"/"+str(a+1)+"/"+"2020"
    return s
 
def listaAleatorios(n):
    s=[0]*n
    for i in range(n):
        s[i]=random.random()
    return s
    
def enBalde(lista,minimo,maximo):
    cuenta=0
    for num in lista:
        if minimo<num<maximo:
            cuenta=cuenta+1
    return cuenta
    

def  fin2(dias,gasT):
     paquete=[0]*dias
     anchura=1.0/dias
     for i in range(dias):
         min=i*anchura
         max=min+anchura
         paquete[i]=str(enBalde(listaAleatorios(gasT),min,max))+"-"+fecha1(dias)[i]
         
         print(paquete[i])
 
def  fin3(dias,gasT):
     paquete=[0]*dias
     anchura=1.0/dias
     for i in range(dias):
         min=i*anchura
         max=min+anchura
         paquete[i]=enBalde(listaAleatorios(gasT),min,max)
         
     return paquete
 
                         
                          
lista2=[2,4,3,5]
x=0
def rec(lista,x):
    if x> len(lista)-1:
          return
    for i in range(lista[x]):
          print("hola")
    print("otro")
    rec(lista,x+1)

 
def rec2(lista,x):
    if x> len(lista)-1:
          return
    for i in range(lista[x]):
          print("hola"+fecha1(5)[x])
    print("otro")
    rec2(lista,x+1)
matrix3=[["COCA COLA VENDING AUCKLAND","COCA COLA VENDING AUCKLAND","COCA COLA VENDING AUCKLAND","THE WAREHOUSE","THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "PAK N SAVE R","PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "FAMILY BAR","FAMILY BAR", "FAMILY BAR", "NEW WORLD METRO","NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "AT HOP AUCKLAND","AT HOP AUCKLAND", "AT HOP AUCKLAND", "AT HOP AUCKLAND", "AT HOP AUCKLAND", "MS*BASEAUCKLAND","MS*BASEAUCKLAND", "INTA LIQUOR STORE","INTA LIQUOR STORE", "INTA LIQUOR STORE", "INTA LIQUOR STORE", "INTA LIQUOR STORE", "QUEEN STREET BACKPACKERS","QUEEN STREET BACKPACKERS","POINTERS BAR AND GRI","POINTERS BAR AND GRI", "POINTERS BAR AND GRI","PROVEDOR AUCKLAND", "PROVEDOR AUCKLAND","PROVEDOR AUCKLAND","FORT STREET BACKPACKERS","SUMO SUSHI", "SUMO SUSHI","SUMO SUSHI","SUMO SUSHI","SUMO SUSHI","MCDONALS BRITOMART AUCKLAND", "MCDONALS BRITOMART AUCKLAND","MCDONALS BRITOMART AUCKLAND","MCDONALS BRITOMART AUCKLAND","MCDONALS BRITOMART AUCKLAND","DOMINO’S POINT","DOMINO’S POINT", "DOMINO’S POINT", "DOMINO’S POINT", "DOMINO’S POINT", "DOMINO’S POINT", "KFC FORT STREET","KFC FORT STREET", "KFC FORT STREET", "KFC FORT STREET", "KFC FORT STREET", "KFC FORT STREET", "KFC FORT STREET", "KFC FORT STREET ", "KFC FORT STREET", "KFC FORT STREET", "DOMINO’S POINT","DOMINO’S POINT", "DOMINO’S POINT", "DOMINO’S POINT", "DOMINO’S POINT", "DOMINO’S POINT","BURGER KING AUCKLAND CENTER","BURGER KING AUCKLAND CENTER","BURGER KING AUCKLAND CENTER","KMART AUCKLAND","KMART AUCKLAND","KMART AUCKLAND","KMART AUCKLAND","24 CONVENIENCE STORE","24 CONVENIENCE STORE","24 CONVENIENCE STORE","24 CONVENIENCE STORE","77 CONVENIENCE STORE","77 CONVENIENCE STORE","77 CONVENIENCE STORE","77 CONVENIENCE STORE"],["MS*BASEAUCKLAND","MS*BASEAUCKLAND","MS*BASEAUCKLAND","FORT STREET HOSTEL","FORT STREET HOSTEL","QUEEN STREET BACKPACKERS","QUEEN STREET BACKPACKERS","FORT STREET HOSTEL","FORT STREET HOSTEL","PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R","NEW WORLD METRO", "NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","AT HOP AUCKLAND","AT HOP AUCKLAND", "AT HOP AUCKLAND", "AT HOP AUCKLAND", "AT HOP AUCKLAND", "AT HOP AUCKLAND", "AT HOP AUCKLAND", "AT HOP AUCKLAND", "AT HOP AUCKLAND", "AT HOP AUCKLAND", "INTA LIQUOR STORE", "INTA LIQUOR STORE","INTA LIQUOR STORE","INTA LIQUOR STORE","INTA LIQUOR STORE","INTA LIQUOR STORE","INTA LIQUOR STORE","INTA LIQUOR STORE","INTA LIQUOR STORE","INTA LIQUOR STORE","UBER*EATS HELP.UBER.COM","UBER*EATS HELP.UBER.COM","UBER*EATS HELP.UBER.COM","UBER*EATS HELP.UBER.COM"]]
nivel1=[["COCA COLA VENDING AUCKLAND","COCA COLA VENDING AUCKLAND","COCA COLA VENDING AUCKLAND","THE WAREHOUSE","THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "PAK N SAVE R","PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "FAMILY BAR","FAMILY BAR", "FAMILY BAR", "NEW WORLD METRO","NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "AT HOP AUCKLAND","AT HOP AUCKLAND", "AT HOP AUCKLAND", "AT HOP AUCKLAND", "AT HOP AUCKLAND", "MS*BASEAUCKLAND","MS*BASEAUCKLAND", "INTA LIQUOR STORE","INTA LIQUOR STORE", "INTA LIQUOR STORE", "INTA LIQUOR STORE", "INTA LIQUOR STORE", "QUEEN STREET BACKPACKERS","QUEEN STREET BACKPACKERS","POINTERS BAR AND GRI","POINTERS BAR AND GRI", "POINTERS BAR AND GRI","PROVEDOR AUCKLAND", "PROVEDOR AUCKLAND","PROVEDOR AUCKLAND","FORT STREET BACKPACKERS","SUMO SUSHI", "SUMO SUSHI","SUMO SUSHI","SUMO SUSHI","SUMO SUSHI","MCDONALS BRITOMART AUCKLAND", "MCDONALS BRITOMART AUCKLAND","MCDONALS BRITOMART AUCKLAND","MCDONALS BRITOMART AUCKLAND","MCDONALS BRITOMART AUCKLAND","DOMINO’S POINT","DOMINO’S POINT", "DOMINO’S POINT", "DOMINO’S POINT", "DOMINO’S POINT", "DOMINO’S POINT", "KFC FORT STREET","KFC FORT STREET", "KFC FORT STREET", "KFC FORT STREET", "KFC FORT STREET", "KFC FORT STREET", "KFC FORT STREET", "KFC FORT STREET ", "KFC FORT STREET", "KFC FORT STREET", "DOMINO’S POINT","DOMINO’S POINT", "DOMINO’S POINT", "DOMINO’S POINT", "DOMINO’S POINT", "DOMINO’S POINT","BURGER KING AUCKLAND CENTER","BURGER KING AUCKLAND CENTER","BURGER KING AUCKLAND CENTER","KMART AUCKLAND","KMART AUCKLAND","KMART AUCKLAND","KMART AUCKLAND","24 CONVENIENCE STORE","24 CONVENIENCE STORE","24 CONVENIENCE STORE","24 CONVENIENCE STORE","77 CONVENIENCE STORE","77 CONVENIENCE STORE","77 CONVENIENCE STORE","77 CONVENIENCE STORE"],["MS*BASEAUCKLAND","MS*BASEAUCKLAND","MS*BASEAUCKLAND","FORT STREET HOSTEL","FORT STREET HOSTEL","QUEEN STREET BACKPACKERS","QUEEN STREET BACKPACKERS","FORT STREET HOSTEL","FORT STREET HOSTEL","PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R","NEW WORLD METRO", "NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","AT HOP AUCKLAND","AT HOP AUCKLAND", "AT HOP AUCKLAND", "AT HOP AUCKLAND", "AT HOP AUCKLAND", "AT HOP AUCKLAND", "AT HOP AUCKLAND", "AT HOP AUCKLAND", "AT HOP AUCKLAND", "AT HOP AUCKLAND", "INTA LIQUOR STORE", "INTA LIQUOR STORE","INTA LIQUOR STORE","INTA LIQUOR STORE","INTA LIQUOR STORE","INTA LIQUOR STORE","INTA LIQUOR STORE","INTA LIQUOR STORE","INTA LIQUOR STORE","INTA LIQUOR STORE","UBER*EATS HELP.UBER.COM","UBER*EATS HELP.UBER.COM","UBER*EATS HELP.UBER.COM","UBER*EATS HELP.UBER.COM"]]
nivel2=[["COCA COLA VENDING AUCKLAND","COCA COLA VENDING AUCKLAND","COCA COLA VENDING AUCKLAND","THE WAREHOUSE","THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "PAK N SAVE R","PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R","NEW WORLD METRO","NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "AT HOP AUCKLAND","AT HOP AUCKLAND", "AT HOP AUCKLAND", "AT HOP AUCKLAND", "AT HOP AUCKLAND", "MS*BASEAUCKLAND","MS*BASEAUCKLAND", "INTA LIQUOR STORE","INTA LIQUOR STORE", "INTA LIQUOR STORE", "INTA LIQUOR STORE", "INTA LIQUOR STORE", "QUEEN STREET BACKPACKERS","QUEEN STREET BACKPACKERS","FORT STREET BACKPACKERS","SUMO SUSHI", "SUMO SUSHI","SUMO SUSHI","SUMO SUSHI","SUMO SUSHI","MCDONALS BRITOMART AUCKLAND", "MCDONALS BRITOMART AUCKLAND","MCDONALS BRITOMART AUCKLAND","MCDONALS BRITOMART AUCKLAND","MCDONALS BRITOMART AUCKLAND","DOMINO’S POINT","DOMINO’S POINT", "DOMINO’S POINT", "DOMINO’S POINT", "DOMINO’S POINT", "DOMINO’S POINT", "KFC FORT STREET","KFC FORT STREET", "KFC FORT STREET", "KFC FORT STREET", "KFC FORT STREET", "KFC FORT STREET", "KFC FORT STREET", "KFC FORT STREET ", "KFC FORT STREET", "KFC FORT STREET", "DOMINO’S POINT","DOMINO’S POINT", "DOMINO’S POINT", "DOMINO’S POINT", "DOMINO’S POINT", "DOMINO’S POINT","BURGER KING AUCKLAND CENTER","BURGER KING AUCKLAND CENTER","BURGER KING AUCKLAND CENTER","KMART AUCKLAND","KMART AUCKLAND","KMART AUCKLAND","KMART AUCKLAND","24 CONVENIENCE STORE","24 CONVENIENCE STORE","24 CONVENIENCE STORE","24 CONVENIENCE STORE","77 CONVENIENCE STORE","77 CONVENIENCE STORE","77 CONVENIENCE STORE","77 CONVENIENCE STORE"],["MS*BASEAUCKLAND","MS*BASEAUCKLAND","MS*BASEAUCKLAND","FORT STREET HOSTEL","FORT STREET HOSTEL","FAT CAMEL BACKPACKERS","FAT CAMEL BACKPACKERS","FORT STREET HOSTEL","FORT STREET HOSTEL","PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R","NEW WORLD METRO", "NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","AT HOP AUCKLAND","AT HOP AUCKLAND", "AT HOP AUCKLAND", "AT HOP AUCKLAND", "AT HOP AUCKLAND", "AT HOP AUCKLAND", "AT HOP AUCKLAND", "AT HOP AUCKLAND", "AT HOP AUCKLAND", "AT HOP AUCKLAND", "INTA LIQUOR STORE", "INTA LIQUOR STORE","INTA LIQUOR STORE","INTA LIQUOR STORE","INTA LIQUOR STORE","INTA LIQUOR STORE","INTA LIQUOR STORE","INTA LIQUOR STORE","INTA LIQUOR STORE","INTA LIQUOR STORE","UBER*EATS HELP.UBER.COM","UBER*EATS HELP.UBER.COM","UBER*EATS HELP.UBER.COM","UBER*EATS HELP.UBER.COM"]]
nivel2_5=[["COCA COLA VENDING AUCKLAND","COCA COLA VENDING AUCKLAND","COCA COLA VENDING AUCKLAND","THE WAREHOUSE","THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "THE WAREHOUSE", "PAK N SAVE R","PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R","NEW WORLD METRO","NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "AT HOP AUCKLAND","AT HOP AUCKLAND", "AT HOP AUCKLAND", "AT HOP AUCKLAND", "AT HOP AUCKLAND", "MS*BASEAUCKLAND","MS*BASEAUCKLAND", "INTA LIQUOR STORE","INTA LIQUOR STORE", "INTA LIQUOR STORE", "INTA LIQUOR STORE", "INTA LIQUOR STORE", "QUEEN STREET BACKPACKERS","QUEEN STREET BACKPACKERS","FORT STREET BACKPACKERS","SUMO SUSHI", "SUMO SUSHI","SUMO SUSHI","SUMO SUSHI","SUMO SUSHI","MCDONALS BRITOMART AUCKLAND", "MCDONALS BRITOMART AUCKLAND","MCDONALS BRITOMART AUCKLAND","MCDONALS BRITOMART AUCKLAND","MCDONALS BRITOMART AUCKLAND","DOMINO’S POINT","DOMINO’S POINT", "DOMINO’S POINT", "DOMINO’S POINT", "DOMINO’S POINT", "DOMINO’S POINT", "KFC FORT STREET","KFC FORT STREET", "KFC FORT STREET", "KFC FORT STREET", "KFC FORT STREET", "KFC FORT STREET", "KFC FORT STREET", "KFC FORT STREET ", "KFC FORT STREET", "KFC FORT STREET", "DOMINO’S POINT","DOMINO’S POINT", "DOMINO’S POINT", "DOMINO’S POINT", "DOMINO’S POINT", "DOMINO’S POINT","BURGER KING AUCKLAND CENTER","BURGER KING AUCKLAND CENTER","BURGER KING AUCKLAND CENTER","KMART AUCKLAND","KMART AUCKLAND","KMART AUCKLAND","KMART AUCKLAND","24 CONVENIENCE STORE","24 CONVENIENCE STORE","24 CONVENIENCE STORE","24 CONVENIENCE STORE","77 CONVENIENCE STORE","77 CONVENIENCE STORE","77 CONVENIENCE STORE","77 CONVENIENCE STORE"],["MS*BASEAUCKLAND","MS*BASEAUCKLAND","MS*BASEAUCKLAND","FORT STREET HOSTEL","FORT STREET HOSTEL","FAT CAMEL BACKPACKERS","FAT CAMEL BACKPACKERS","FORT STREET HOSTEL","FORT STREET HOSTEL","PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R","NEW WORLD METRO", "NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","AT HOP AUCKLAND","AT HOP AUCKLAND", "AT HOP AUCKLAND", "AT HOP AUCKLAND", "AT HOP AUCKLAND", "AT HOP AUCKLAND", "AT HOP AUCKLAND", "AT HOP AUCKLAND", "AT HOP AUCKLAND", "AT HOP AUCKLAND", "INTA LIQUOR STORE", "INTA LIQUOR STORE","INTA LIQUOR STORE","INTA LIQUOR STORE","INTA LIQUOR STORE","INTA LIQUOR STORE","INTA LIQUOR STORE","INTA LIQUOR STORE","INTA LIQUOR STORE","INTA LIQUOR STORE","UBER*EATS HELP.UBER.COM","UBER*EATS HELP.UBER.COM","UBER*EATS HELP.UBER.COM","UBER*EATS HELP.UBER.COM"]]
nivel3=[["COCA COLA VENDING AUCKLAND","COCA COLA VENDING AUCKLAND","COCA COLA VENDING AUCKLAND", "PAK N SAVE R","PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R","NEW WORLD METRO","NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "MS*BASEAUCKLAND","MS*BASEAUCKLAND", "FAT CAMEL BACKPACKERS","FAT CAMEL BACKPACKERS","FORT STREET BACKPACKERS","SUMO SUSHI", "SUMO SUSHI","SUMO SUSHI","SUMO SUSHI","SUMO SUSHI","MCDONALS BRITOMART AUCKLAND", "MCDONALS BRITOMART AUCKLAND","MCDONALS BRITOMART AUCKLAND","MCDONALS BRITOMART AUCKLAND","MCDONALS BRITOMART AUCKLAND","DOMINO’S POINT","DOMINO’S POINT", "DOMINO’S POINT", "DOMINO’S POINT", "DOMINO’S POINT", "DOMINO’S POINT", "KFC FORT STREET","KFC FORT STREET", "KFC FORT STREET", "KFC FORT STREET", "KFC FORT STREET", "KFC FORT STREET", "KFC FORT STREET", "KFC FORT STREET ", "KFC FORT STREET", "KFC FORT STREET", "DOMINO’S POINT","DOMINO’S POINT", "DOMINO’S POINT", "DOMINO’S POINT", "DOMINO’S POINT", "DOMINO’S POINT","BURGER KING AUCKLAND CENTER","BURGER KING AUCKLAND CENTER","BURGER KING AUCKLAND CENTER","24 CONVENIENCE STORE","24 CONVENIENCE STORE","24 CONVENIENCE STORE","24 CONVENIENCE STORE","77 CONVENIENCE STORE","77 CONVENIENCE STORE","77 CONVENIENCE STORE","77 CONVENIENCE STORE","UNICHEM 280 QUEEN STREETAUCKLAND"],["FAT CAMEL BACKPACKERS","FAT CAMEL BACKPACKERS","FAT CAMEL BACKPACKERS","FAT CAMEL BACKPACKERS","FAT CAMEL BACKPACKERS","FAT CAMEL BACKPACKERS","FAT CAMEL BACKPACKERS","FORT STREET HOSTEL","FORT STREET HOSTEL","PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R","NEW WORLD METRO", "NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","AT HOP AUCKLAND","UBER*EATS HELP.UBER.COM","UBER*EATS HELP.UBER.COM","UBER*EATS HELP.UBER.COM","UBER*EATS HELP.UBER.COM"]]
nivel4=[["COCA COLA VENDING AUCKLAND","COCA COLA VENDING AUCKLAND","COCA COLA VENDING AUCKLAND", "PAK N SAVE R","PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R","NEW WORLD METRO","NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "NEW WORLD METRO", "MS*BASEAUCKLAND","MS*BASEAUCKLAND", "FAFT CAMEL BACKPACKERS","FAFT CAMEL BACKPACKERS","FORT STREET BACKPACKERS","24 CONVENIENCE STORE","24 CONVENIENCE STORE","24 CONVENIENCE STORE","24 CONVENIENCE STORE","77 CONVENIENCE STORE","77 CONVENIENCE STORE","77 CONVENIENCE STORE","77 CONVENIENCE STORE","UNICHEM 280 QUEEN STREETAUCKLAND"],["FAT CAMEL BACKPACKERS","FAT CAMEL BACKPACKERS","FAT CAMEL BACKPACKERS","FAT CAMEL BACKPACKERS","FAT CAMEL BACKPACKERS","FAT CAMEL BACKPACKERS","FAT CAMEL BACKPACKERS","PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R", "PAK N SAVE R","NEW WORLD METRO", "NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","NEW WORLD METRO","UBER*EATS HELP.UBER.COM","UBER*EATS HELP.UBER.COM","UBER*EATS HELP.UBER.COM","UBER*EATS HELP.UBER.COM","UBER*EATS HELP.UBER.COM","UBER*EATS HELP.UBER.COM","UBER*EATS HELP.UBER.COM","UBER*EATS HELP.UBER.COM","UBER*EATS HELP.UBER.COM","UBER*EATS HELP.UBER.COM"]]
def many5(dias):
   lis=[0]*dias
   for i in range(dias):
       
       
       a=random.randint(3,10)+random.random()
       b=random.randint(10,90)+random.random()
       
       z=random.randint(1,100)
       if z<90:
           
           uno= matrix3[0][int(random.random()*len(matrix3[0]))]
           
           lis[i]= uno+"-"+" US "+"%.2f"%a
       if z>90:
           
           dos= matrix3[1][int(random.random()*len(matrix3[1]))] 
           lis[i]= dos+"-"+" US "+"%.2f"%b                  
           
          
   return lis
   
def rec3(lista,x):
    if x> len(lista)-1:
          return
    for i in range(lista[x]):
          print("hi"+fecha1(len(lista))[x]+str(many5(i)))
    print("otro")
    rec3(lista,x+1)
 
def rec4(lista,x):
    if x> len(lista)-1:
          return
    for i in range(lista[x]):
        for b in range(1):
          print(fecha1(len(lista))[x]+"-"+many5(1)[b])
    print("otro")
    rec4(lista,x+1)    
 
def rec5(lista,x):
    if x> len(lista)-1:
          return
    for i in range(lista[x]):
        for b in range(1):
          print(fecha1(len(lista))[x]+" - "+many5(1)[b])
    print("END DAY")
    rec5(lista,x+1)
def fechaD1(dias,dia,mes,ano):
    for i in range(1):
        for b in range(dias):
            print(str(b+dia)+"/"+str(i+mes)+"/"+str(ano))
          
def fechaD(dias,dia,mes,ano):
    for i in range(1):
        s=[0]*dias
        for b in range(dias):
            
            s[b]=str(b+dia)+"/"+str(i+mes)+"/"+str(ano)
        return s
 
def fechaD2(dias,dia,mes,ano):
    for i in range(1):
        
        s=[0]*dias
        for b in range(dias):
            
                s[b]="0"+str(b+dia)+"/"+"0"+str(i+mes)+"/"+str(ano)
            
        return s        
def rec9(lista,x,dia,mes,ano):
    if x> len(lista)-1:
          return
    for i in range(lista[x]):
          print(str(fechaD(len(lista),dia,mes,ano)[x])+" - "+str(many5(1)[0]))
    print("END DAY")
    rec9(lista,x+1,dia,mes,ano)
 
def rec10(lista,x,dia,mes,ano):
    if x> len(lista)-1:
          return
    for i in range(lista[x]):
          print(str(fechaD(len(lista),dia,mes,ano)[x])+" - "+str(matrixLis3(1)[0][0]))
    print("END DAY")
    rec10(lista,x+1,dia,mes,ano)
 
 
def rec11(lista,x,dia,mes,ano):
    if x> len(lista)-1:
          return
    for i in range(lista[x]):
          a=random.randint(3,10)+random.random()
          b=random.randint(10,90)+random.random()
          z=random.randint(0,101)
          if z<90:
              uno=matrix3[0][int(random.random()*len(matrix3[0]))]
              print(str(fechaD(len(lista),dia,mes,ano)[x])+"-"+ uno+"-"+"%.2f"%a)
          if z>90:
              dos= matrix3[1][int(random.random()*len(matrix3[1]))] 
              print(str(fechaD(len(lista),dia,mes,ano)[x])+"-"+ dos+"-"+"%.2f"%b)
          if z==90:
              print("coca cola")
    print("END DAY")
    rec11(lista,x+1,dia,mes,ano)
 

def rec12(lista,x,dia,mes,ano,med,max):
    if x> len(lista)-1:
          return
    for i in range(lista[x]):
          a=random.randint(3,med)+random.random()
          b=random.randint(med,max)+random.random()
          z=random.randint(0,101)
          if z<90:
              num=int(random.random()*len(matrix3[0]))
              if num>=3:  
                 uno=matrix3[0][num]
              
                 print(
"""<tr style="border: 1px solid #EEE;background: white;">
    <td class="px-text-center" title="Confirmado"><img src="/assets/prex/img/movimientos/check.svg">
    <!--<span class='glyphicon glyphicon-ok-sign iconC'></span>--></td>
    <td>"""+str(fechaD(len(lista),dia,mes,ano)[x])+"""</td>
    <td class="hidden-xs" style="text-align: left">"""+uno+"""</td>
    <td class="black px-text-left" style="font-weight: 600;">-&nbsp;U$S&nbsp;"""+"%.2f"%a+"""</td>
    <td class="px-no-padding">
    <button class="btn btn-link btn-sm btn-info-movimiento" type="button" style="float: left" 
    data-estado="Confirmado" data-fecha="25/06/2020" data-descripcion="MS* BASEAUCKLAND" 
    data-origen="NZD -5,00" data-importe="U$S 4,01" data-colorimporte="black">VER</button>
   </td>""")
          if z>90:
              dos= matrix3[1][int(random.random()*len(matrix3[1]))] 
              print(
"""<tr style="border: 1px solid #EEE;background: white;">
    <td class="px-text-center" title="Confirmado"><img src="/assets/prex/img/movimientos/check.svg">
    <!--<span class='glyphicon glyphicon-ok-sign iconC'></span>--></td>
    <td>"""+str(fechaD(len(lista),dia,mes,ano)[x])+"""</td>
    <td class="hidden-xs" style="text-align: left">"""+dos+"""</td>
    <td class="black px-text-left" style="font-weight: 600;">-&nbsp;U$S&nbsp;"""+"%.2f"%b+"""</td>
    <td class="px-no-padding">
    <button class="btn btn-link btn-sm btn-info-movimiento" type="button" style="float: left" 
    data-estado="Confirmado" data-fecha="25/06/2020" data-descripcion="MS* BASEAUCKLAND" 
    data-origen="NZD -5,00" data-importe="U$S 4,01" data-colorimporte="black">VER</button>
   </td>""")
          if z==90 or z<3:
              print(
"""<tr style="border: 1px solid #EEE;background: white;">
    <td class="px-text-center" title="Confirmado"><img src="/assets/prex/img/movimientos/check.svg">
    <!--<span class='glyphicon glyphicon-ok-sign iconC'></span>--></td>
    <td>"""+str(fechaD(len(lista),dia,mes,ano)[x])+"""</td>
    <td class="hidden-xs" style="text-align: left">"""+"COCA COLA VENDING AUCKLAND"+"""</td>
    <td class="black px-text-left" style="font-weight: 600;">-&nbsp;U$S&nbsp;"""+"2.46"+"""</td>
    <td class="px-no-padding">
    <button class="btn btn-link btn-sm btn-info-movimiento" type="button" style="float: left" 
    data-estado="Confirmado" data-fecha="25/06/2020" data-descripcion="MS* BASEAUCKLAND" 
    data-origen="NZD -5,00" data-importe="U$S 4,01" data-colorimporte="black">VER</button>
   </td>""")
    
    rec12(lista,x+1,dia,mes,ano,med,max)
 
def fechaD3(dias,dia,mes,ano,x):
    for i in range(1):
        
        s=[0]*dias
        for b in range(dias):
            
            
            if x<=8:
                s[b]="0"+str(b+dia)+"/"+"0"+str(i+mes)+"/"+str(ano)
            if x>8:    
                s[b]=str(b+dia)+"/"+"0"+str(i+mes)+"/"+str(ano)
            
        return s
 
 
 
def fechaD4(dias,dia,mes,ano,x):
    for i in range(1):
        #x=0
        s=[0]*dias
        for b in range(dias):
            
            
            if x<=8 and mes<9:
                s[b]="0"+str(b+dia)+"/"+"0"+str(i+mes)+"/"+str(ano)
            if x>8 and mes<9:    
                s[b]=str(b+dia)+"/"+"0"+str(i+mes)+"/"+str(ano)
            if x<=8 and mes>9:
                s[b]="0"+str(b+dia)+"/"+str(i+mes)+"/"+str(ano)
            if x>8 and mes>9:    
                s[b]=str(b+dia)+"/"+str(i+mes)+"/"+str(ano)    
            
        return s
 
def rec14(lista,x,dia,mes,ano,med,max,nivel):
    if x> len(lista)-1:
          return
    for i in range(lista[x]):
          a=random.randint(3,med)+random.random()
          b=random.randint(med,max)+random.random()
          z=random.randint(0,101)
          if z<90:
              num=int(random.random()*len(nivel[0]))
              if num>=3:  
                 uno=nivel[0][num]
              
                 print(
"""<tr style="border: 1px solid #EEE;background: white;">
    <td class="px-text-center" title="Confirmado"><img src="/assets/prex/img/movimientos/check.svg">
    <!--<span class='glyphicon glyphicon-ok-sign iconC'></span>--></td>
    <td>"""+str(fechaD4(len(lista),dia,mes,ano,x)[x])+"""</td>
    <td class="hidden-xs" style="text-align: left">"""+uno+"""</td>
    <td class="black px-text-left" style="font-weight: 600;">-&nbsp;U$S&nbsp;"""+"%.2f"%a+"""</td>
    <td class="px-no-padding">
    <button class="btn btn-link btn-sm btn-info-movimiento" type="button" style="float: left" 
    data-estado="Confirmado" data-fecha="25/06/2020" data-descripcion="MS* BASEAUCKLAND" 
    data-origen="NZD -5,00" data-importe="U$S 4,01" data-colorimporte="black">VER</button>
    </td>
</tr>
   """)
          if z>90:
              dos= nivel[1][int(random.random()*len(nivel[1]))] 
              print(
"""<tr style="border: 1px solid #EEE;background: white;">
    <td class="px-text-center" title="Confirmado"><img src="/assets/prex/img/movimientos/check.svg">
    <!--<span class='glyphicon glyphicon-ok-sign iconC'></span>--></td>
    <td>"""+str(fechaD4(len(lista),dia,mes,ano,x)[x])+"""</td>
    <td class="hidden-xs" style="text-align: left">"""+dos+"""</td>
    <td class="black px-text-left" style="font-weight: 600;">-&nbsp;U$S&nbsp;"""+"%.2f"%b+"""</td>
    <td class="px-no-padding">
    <button class="btn btn-link btn-sm btn-info-movimiento" type="button" style="float: left" 
    data-estado="Confirmado" data-fecha="25/06/2020" data-descripcion="MS* BASEAUCKLAND" 
    data-origen="NZD -5,00" data-importe="U$S 4,01" data-colorimporte="black">VER</button>
    </td>
</tr>
   """)
          if z==90 or z<3:
              print(
"""<tr style="border: 1px solid #EEE;background: white;">
    <td class="px-text-center" title="Confirmado"><img src="/assets/prex/img/movimientos/check.svg">
    <!--<span class='glyphicon glyphicon-ok-sign iconC'></span>--></td>
    <td>"""+str(fechaD4(len(lista),dia,mes,ano,x)[x])+"""</td>
    <td class="hidden-xs" style="text-align: left">"""+"COCA COLA VENDING AUCKLAND"+"""</td>
    <td class="black px-text-left" style="font-weight: 600;">-&nbsp;U$S&nbsp;"""+"2.46"+"""</td>
    <td class="px-no-padding">
    <button class="btn btn-link btn-sm btn-info-movimiento" type="button" style="float: left" 
    data-estado="Confirmado" data-fecha="25/06/2020" data-descripcion="MS* BASEAUCKLAND" 
    data-origen="NZD -5,00" data-importe="U$S 4,01" data-colorimporte="black">VER</button>
    </td>
</tr>
   """)
    
    rec14(lista,x+1,dia,mes,ano,med,max,nivel)
 
 
 
 
def rec13(lista,x,dia,mes,ano,med,max,nivel):
    if x> len(lista)-1:
          return
    for i in range(lista[x]):
          a=random.randint(3,med)+random.random()
          b=random.randint(med,max)+random.random()
          z=random.randint(0,101)
          if z<90:
              num=int(random.random()*len(nivel[0]))
              if num>=3:  
                 uno=nivel[0][num]
              
                 print(
"""<tr style="border: 1px solid #EEE;background: white;">
    <td class="px-text-center" title="Confirmado"><img src="/assets/prex/img/movimientos/check.svg">
    <!--<span class='glyphicon glyphicon-ok-sign iconC'></span>--></td>
    <td>"""+str(fechaD3(len(lista),dia,mes,ano,x)[x])+"""</td>
    <td class="hidden-xs" style="text-align: left">"""+uno+"""</td>
    <td class="black px-text-left" style="font-weight: 600;">-&nbsp;U$S&nbsp;"""+"%.2f"%a+"""</td>
    <td class="px-no-padding">
    <button class="btn btn-link btn-sm btn-info-movimiento" type="button" style="float: left" 
    data-estado="Confirmado" data-fecha="25/06/2020" data-descripcion="MS* BASEAUCKLAND" 
    data-origen="NZD -5,00" data-importe="U$S 4,01" data-colorimporte="black">VER</button>
    </td>
</tr>
   """)
          if z>90:
              dos= nivel[1][int(random.random()*len(nivel[1]))] 
              print(
"""<tr style="border: 1px solid #EEE;background: white;">
    <td class="px-text-center" title="Confirmado"><img src="/assets/prex/img/movimientos/check.svg">
    <!--<span class='glyphicon glyphicon-ok-sign iconC'></span>--></td>
    <td>"""+str(fechaD3(len(lista),dia,mes,ano,x)[x])+"""</td>
    <td class="hidden-xs" style="text-align: left">"""+dos+"""</td>
    <td class="black px-text-left" style="font-weight: 600;">-&nbsp;U$S&nbsp;"""+"%.2f"%b+"""</td>
    <td class="px-no-padding">
    <button class="btn btn-link btn-sm btn-info-movimiento" type="button" style="float: left" 
    data-estado="Confirmado" data-fecha="25/06/2020" data-descripcion="MS* BASEAUCKLAND" 
    data-origen="NZD -5,00" data-importe="U$S 4,01" data-colorimporte="black">VER</button>
    </td>
</tr>
   """)
          if z==90 or z<3:
              print(
"""<tr style="border: 1px solid #EEE;background: white;">
    <td class="px-text-center" title="Confirmado"><img src="/assets/prex/img/movimientos/check.svg">
    <!--<span class='glyphicon glyphicon-ok-sign iconC'></span>--></td>
    <td>"""+str(fechaD3(len(lista),dia,mes,ano,x)[x])+"""</td>
    <td class="hidden-xs" style="text-align: left">"""+"COCA COLA VENDING AUCKLAND"+"""</td>
    <td class="black px-text-left" style="font-weight: 600;">-&nbsp;U$S&nbsp;"""+"2.46"+"""</td>
    <td class="px-no-padding">
    <button class="btn btn-link btn-sm btn-info-movimiento" type="button" style="float: left" 
    data-estado="Confirmado" data-fecha="25/06/2020" data-descripcion="MS* BASEAUCKLAND" 
    data-origen="NZD -5,00" data-importe="U$S 4,01" data-colorimporte="black">VER</button>
    </td>
</tr>
   """)
    
    rec13(lista,x+1,dia,mes,ano,med,max,nivel)    
 

 
def rec7(lista,x):
    if x> len(lista)-1:
          return
    for i in range(lista[x]):
          print(str(fecha1(len(lista))[x])+" - "+str(many5(1)[0]))
    print("END DAY")
    rec7(lista,x+1)
 
def rec81(lista,x):
    if x> len(lista)-1:
          return
    for i in range(lista[x]):
          print(str(fecha1(len(lista))[x])+" - "+str(many5(1)[0]))
    print("END DAY")
    rec81(lista,x+1)    
 
def rec6(lista,x):
    if x> len(lista)-1:
          return
    for i in range(lista[x]):
        for b in range(1):
          
          print("""<tr style="border: 1px solid #EEE;background: white;">
                <td class="px-text-center" title="Confirmado"><img src="/assets/prex/img/movimientos/check.svg"><!--<span class='glyphicon glyphicon-ok-sign iconC'></span>--></td>
                <td>"""+str(fecha1(len(lista)-1)[x])+"""</td>
                <td class="hidden-xs" style="text-align: left">+"""+str(many5(1)[b])+"""+</td>
                <td class="black px-text-left" style="font-weight: 600;">-&nbsp;U$S&nbsp;4,01</td>
                <td class="px-no-padding">
                    <button class="btn btn-link btn-sm btn-info-movimiento" type="button" style="float: left" data-estado="Confirmado" data-fecha="25/06/2020" data-descripcion="MS* BASEAUCKLAND" data-origen="NZD -5,00" data-importe="U$S 4,01" data-colorimporte="black">VER</button>
                </td>""")
    print("END DAY")
    rec6(lista,x+1)
 
def matrixLis2(frec):
    m=[]
    n=[]
    t=[m,n]
    
    for i in range(frec):
       z=random.randint(0,101)
       if z<90:
          
          uno= matrix3[0][int(random.random()*len(matrix3[0]))]
          m.append(uno)
         
 
       if z>90:   
          dos= matrix3[1][int(random.random()*len(matrix3[1]))] 
          n.append(dos)
          
    
    return t

 
def matrixLis3(frec):
    m=[]
    n=[]
    t=[m,n]
    
    for i in range(frec):
       z=random.randint(0,101)
       if z<90:
          
          uno= matrix3[0][int(random.random()*len(matrix3[0]))]
          m.append(uno)
         
 
       if z>90:   
          dos= matrix3[1][int(random.random()*len(matrix3[1]))] 
          n.append(dos)
    if len(m)==0:
          m.append("PAKANSIVE N SAVE R")
    if len(n)==0:
          n.append("NEW WORLD METRO")
 
    
    return t
def elec1(uno):
    for i in range(uno):
        print(matrixLis3(1)[0][0])

        
 
def rec8(lista,x):
    if x> len(lista)-1:
          return
    for i in range(lista[x]):
        for b in range(1):
          
          print(
"""<tr style="border: 1px solid #EEE;background: white;">
    <td class="px-text-center" title="Confirmado"><img src="/assets/prex/img/movimientos/check.svg">
    <!--<span class='glyphicon glyphicon-ok-sign iconC'></span>--></td>
    <td>""" + fecha1(len(lista))[x]+ """</td>
    <td class="hidden-xs" style="text-align: left">"""+many5(1)[0]+"""</td>
    <td class="black px-text-left" style="font-weight: 600;">-&nbsp;U$S&nbsp;4,01</td>
    <td class="px-no-padding">
    <button class="btn btn-link btn-sm btn-info-movimiento" type="button" 
    style="float: left" data-estado="Confirmado" data-fecha="25/06/2020" 
    data-descripcion="MS* BASEAUCKLAND" data-origen="NZD -5,00" data-importe="U$S 4,01" data-colorimporte="black">VER</button>
   </td>""")
    print("FIN DÍA")
    rec8(lista,x+1)  

def prueba2():
    print("""<tr style="border: 1px solid #EEE;background: white;">
                <td class="px-text-center" title="Confirmado"><img src="/assets/prex/img/movimientos/check.svg"><!--<span class='glyphicon glyphicon-ok-sign iconC'></span>--></td>
                <td>"""+str(5)+"""</td>
                <td class="hidden-xs" style="text-align: left">"""+str(6)+"""</td>
                <td class="black px-text-left" style="font-weight: 600;">-&nbsp;U$S&nbsp;4,01</td>
                <td class="px-no-padding">
                    <button class="btn btn-link btn-sm btn-info-movimiento" type="button" style="float: left" data-estado="Confirmado" data-fecha="25/06/2020" data-descripcion="MS* BASEAUCKLAND" data-origen="NZD -5,00" data-importe="U$S 4,01" data-colorimporte="black">VER</button>
                </td>""")
def suma():
     s=0
     for i in range(28):
          s=s+random.random()*3
     print ("%.2f"%s)
                         
 
def suma2():
    s=0
    for i in range(28):
        s=s+random.randint(1,100)+random.random()
    print ("%.2f"%s)
 

                          
tiendas=["a","a","a","b","b","c"]
def many():
    for i in range(28):
       x=int(random.random()*6)
       z=random.randint(5,150)+random.random()
       if 5<z<45 and x<5:
            print (tiendas[x]+" "+"%.2f"%z)
            

                          
def suma():
     x=0
     for i in range(28):
          x=x+random.randint(1,100)+random.random()
     print("%.2f"%x)

def diaEspecifico(inicio, dias):
    x=inicio
    for i in range(dias):
        print(x)
        x=x+1
def prueba(): 
    for i in range(1):
      for z in range(1):
        print(a)
        a=a+1

inta=["THE WAREHOUSE","PAK N SAVE R","PAK N SAVE R","PAK N SAVE R","PAK N SAVE R"
,"PAK N SAVE R","PAK N SAVE R","PAK N SAVE R","PAK N SAVE R","PAK N SAVE R"]
inta2=["THE WAREHOUSE","PAK N SAVE R"]
def many2():
    for i in range(28):
       x=int(random.random()*10)
       z=random.randint(5,150)+random.random()
       if 30<z<80 and x<10:
           print (inta[x]+"-"+"%.2f"%z)  
 
 
 
def many3():
    for i in range(28):
       x=int(random.random()*2)
       z=random.randint(5,150)+random.random()
       if 30<z<80 and x<2:
           print (inta2[x]+"-"+"%.2f"%z)  
                                
 
n2=[]
n3=[]
n4=[]
 
  
matrix2=[["the wer","the wer", "the wer", "the wer", "the wer", "the wer", "the wer", "the wer", "the wer", "the wer", "the wer", "the wer", "the wer", "the wer", "the wer", "pak","pak", "pak", "pak", "pak", "pak", "pak", "pak", "pak", "pak", "pak", "pak", "pak", "pak", "pak", "fort street","fort street", "famili","famili", "famili", "new world","new world", "new world", "new world", "new world", "new world", "new world", "new world", "new world", "new world", "new world", "new world", "new world", "new world", "new world", "transport","transport", "transport", "transport", "transport", "base","base", "liquor","liquor", "liquor", "liquor", "liquor", "queen street","queen street", "pointer","pointer", "pointer","proveedor", "proveedor",  "proveedor",  "nomad","nomad","nomad" ],["pakansive", "pakansive", "pakansive", "pakansive", "pakansive", "pakansive", "pakansive", "pakansive", "pakansive", "pakansive", "pakansive", "pakansive", "pakansive", "pakansive", "pakansive", "mac", "mac","mac","mac","mac", "sumo sushi", "sumo sushi","sumo sushi","sumo sushi","sumo sushi", "new world", "new world","new world","new world","new world","new world","new world","new world","new world","new world","new world","new world","new world","new world","new world","new world","new world","new world","new world","trans","trans", "trans", "trans", "trans", "trans", "trans", "trans", "trans", "trans", "dominos","dominos", "dominos", "dominos", "dominos", "dominos", "kfc","kfc", "kfc", "kfc", "kfc", "kfc", "kfc", "kfc", "kfc", "kfc", "dominos otro","dominos otro", "dominos otro", "dominos otro", "dominos otro", "dominos otro", "liquor", "liquor","liquor","liquor","liquor","liquor","liquor","liquor","liquor","liquor"]]
 
def many4(dias):
   for i in range(dias):
       
       a=random.randint(3,30)+random.random()
       b=random.randint(30,150)+random.random()
       
       z=random.randint(1,100)
       if z<80:
           
           uno= matrix2[0][int(random.random()*len(matrix2[0]))]
           print(uno+"-"+"%.2f"%a)
       if z>80:
           
           dos= matrix2[1][int(random.random()*len(matrix2[1]))]                     
           print(dos+"-"+"%.2f"%b)
                       
 #parameters                         
#1.-number of days
#2.-amount of purchases on those days
#3.-0 constant is not modified
#4.-the number of the day on which the count begins
#5.-the month of the year
#6.-year 
#7.-average amount of money between a minimum of 3
#8.-maximum amount of money 
# LEVELS
# nivel1 = nivel1, replace nivel1 with the level.
rec14(fin3(20,60),0,1,10,2021,30,90,nivel1)