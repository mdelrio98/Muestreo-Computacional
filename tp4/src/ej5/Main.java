package ej5;

public class Main {
    public static int cant_rep(String[] arr_caracteres,  int i){
        int count  = 0;
        String s = arr_caracteres[i];
        while(arr_caracteres[i]==s){
            count++;
            i++;
        }
        return count;
    }
    public static String[] rlc(String[] arr_caracteres,int n){
        int i=0, j=0;
        String[] arr_rlc= new String[200];
        while(i<n){
            arr_rlc[j] = arr_caracteres[i];
            j++;
            arr_rlc[j] = String.valueOf(cant_rep(arr_caracteres,i));
            j++;
        }
        return arr_rlc;
    }
    public static void decode(String[] arr_rlc,String[] salida,int m){
        int k=0,l=0;
        while(k<m){
            for(int i=0;i<Integer.parseInt(arr_rlc[k+1]);i++){
                salida[l] =arr_rlc[k];
                l++;
            }
            k+=2;
        }
    }
    public static void main(String[] args){
        int n=40,m=54;
        String[] arr_caracteres = new String[]{"5","5","4","5","5","3","3","3","5","5","4","4","10","9","5","5","4","5","9","10","9",
                "10","10","10","2","2","3","14","13","14","13","13","2","2","5","13","14","14","4","5"};

        String[] salida = new String[n];
        String[] arr_rlc = rlc(arr_caracteres,n);
        decode(arr_rlc,salida,m);
        System.out.println("arr_caracteres: t= "+arr_caracteres.length);
        System.out.println("arr_rlc: t= "+arr_rlc.length);
        System.out.println("salida: t= "+salida.length);
        for(int i=0; i< arr_caracteres.length; i++){
            System.out.println("codificacion= "+arr_rlc[i]);
        }
    }

}
