min = int(input("Ingrese el rango minimo: "))
max = int(input("Ingrese el rango maximo: "))

def isPar(n):
    if n%2 == 0:
        return True
    else:
        return False
    
n=min
i=min

while i <= max:
    n=i
    result = "para n = " + str(n)+": "
    while n != 1:
        if isPar(n):
            n = n/2
            result += "-> "+str(int(n))
            continue
        else: 
            n= 3*n+1  
            result += "-> "+str(int(n))
            continue
    print(result)
    i+=1
