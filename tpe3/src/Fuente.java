import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;
public class Fuente {
    private  ArrayList<Node>  listNode;
    public Fuente(){
        this.listNode = new ArrayList<>();
    }

    public ArrayList<Node> generar_Lista_proba() throws FileNotFoundException{
        Scanner s = new Scanner(new File("Lgante.txt"));
        int Simbolos_totales = 0;
        while (lector.hasNext()) {
            Node nodo_Nuevo= new Node(Integer.parseInt(lector.next()));
            boolean encontro =false;
            int i=0;
            while((!encontro ==true) &&(i < listNode.size())) {
                if( listNode.get(i).getSimbolo()== nodo_Nuevo.getSimbolo()){
                    listNode.get(i).sumar_aparicion();
                    encontro = true;
                }
                i++;
            }
            if(encontro==false){
                listNode.add(nodo_Nuevo);}
            Simbolos_totales++;
        }
        for (Node nodo : listNode) {
            nodo.setProb(nodo.getProb() / Simbolos_totales);
        }
        lector.close();
        return listNode;
    }

    public double CalcularEntropia (){
        double entropia = 0;
        for (Node n : listNode) {
            double logpi = -(Math.log(n.getProb())/ Math.log(2));
            entropia += logpi * n.getProb();
        }
        return entropia;
    }
}