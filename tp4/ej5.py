#no ejecutar por la ram

n=40
m=54
def cant_rep(arr_caracteres,i):
    count  = 0
    s = arr_caracteres[i]
    while(arr_caracteres[i]==s && i<n):
        count=count+1
        i=i+1
    return count

def rlc(arr_caracteres):
    i=0
    j=0
    arr_rlc = [n];
    while(i<n):
        arr_rlc.append(str(arr_caracteres[i]))
        j=j+1
        i= cant_rep(arr_caracteres,i)
        arr_rlc.append(str(i))
        j=j+1    
    return arr_rlc;

def decode(arr_rlc,salida,m):
    k=0
    l=0
    while(k<m and l<m):
        for i in range(arr_rlc):
            salida[l] = arr_rlc[k]
            l=l+1  
    k=k+2
    
def main():
    
    arr_caracteres = ["5","5","4","5","5","3","3","3","5","5","4","4","10","9","5","5","4","5","9","10","9",
                "10","10","10","2","2","3","14","13","14","13","13","2","2","5","13","14","14","4","5"]
    salida = []
    arr_rlc = rlc(arr_caracteres)
    decode(arr_rlc,salida)
    for i in range(arr_rlc):
        print("|"+arr_rlc[i])

main()