def cant_rep(arr_caracteres,i):
    count  = 0
    arr_caracteres=[i]
    while(arr_caracteres[i]==s):
        count=count+1
        i=i+1
    return count

def rlc(arr_caracteres,n):
    i=0
    j=0
    arr_rlc= [];
    while(i<n):
        arr_rlc[j] = arr_caracteres[i]
        j=j+1
        arr_rlc[j] = cant_rep(arr_caracteres,i)
        j=j+1    
    return arr_rlc;

def decode(arr_rlc,salida,m):
    k=0
    l=0
    while(k<m):
        for i in range(arr_rlc):
            salida[l] = arr_rlc[k]
            l=l+1  
    k=k+2
    
def main():
    n=40
    m=54
    arr_caracteres = ["5","5","4","5","5","3","3","3","5","5","4","4","10","9","5","5","4","5","9","10","9",
                "10","10","10","2","2","3","14","13","14","13","13","2","2","5","13","14","14","4","5"]
    salida = []
    arr_rlc = rlc(arr_caracteres,n)
    decode(arr_rlc,salida,m)

main()