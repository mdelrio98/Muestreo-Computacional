import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.*;
public class Main {
    public static void almacenarArchivo(List<Node>nodosCodificados){
        PrintWriter printWriter = null;

        try {
                printWriter = new PrintWriter("archivoCodLgante.txt");
        } catch (FileNotFoundException e) {
                System.out.println("Unable to locate the fileName: " + e.getMessage());
        }
        for (Node nodos : nodosCodificados) {
            Objects.requireNonNull(printWriter).println(nodos.getSimbolo()+"|"+nodos.getProb()+"|"+nodos.getCodigo());
        }
        printWriter.close();
    }
    public static void listarCodigo(Node raiz, String s, List<Node>nodosCodificados)
    {

        if (raiz.left == null && raiz.right == null) {

            //System.out.println("S: "+ raiz.getSimbolo()+ " |C: " + s +" |P: " + raiz.getProb());
            raiz.sumarcodigo(s);
            nodosCodificados.add(raiz);
            return;
        }
        listarCodigo(raiz.left, s + "0",nodosCodificados);
        listarCodigo(raiz.right, s + "1",nodosCodificados);
    }

    public static void calculosTeoricos (List<Node>nodosCodificados, Fuente fuente1) {
        double longM = 0.0;
        double longTotal = 0.0;
        for (Node nodo : nodosCodificados) {
            longM += nodo.longCodigo() * nodo.getProb();
            longTotal += nodo.longCodigo() * nodo.getProb() * 1000;
        }
        System.out.println("Long media: " + longM);
        double entropia = fuente1.CalcularEntropia();
        System.out.println("Entropia: " + entropia);
        double rendimiento = entropia/longM;
        System.out.println("Rendimiento: " + rendimiento);
        System.out.println("Longitud total archivo: " + longTotal + " bits");
    }
    public static void main(String[] args)throws FileNotFoundException {
        Fuente fuente1 = new Fuente();
        ArrayList<Node> lnodos = fuente1.procesar_Archivo_entrada();// generamos nuestra fuente en una lista de nodos
        PriorityQueue<Node> q = new PriorityQueue<>(lnodos.size(), new NodeComparator()); //cola de prioridad para ordenar los nodos
        q.addAll(lnodos);
        Node raiz = null;
        
        while (q.size() > 1) {

            //extraigo el primer nodo con menor probabilidad
            Node x = q.peek();
            q.poll();
            //extraigo el segundo nodo con menor probabilidad
            Node y = q.peek();
            q.poll();
            //generamos el nodo intermedio con la suma de las probabilidades de los simbolos mas pequeños
            // no lleva simbolo
            Node f = new Node();
            f.setProb(x.getProb() + y.getProb());
            // el primer nodo mas chico como hijo izquierdo
            f.left = x;
            //  el segundo nodo mas chico como hijo derecho
            f.right = y;
            //generamos la raiz
            raiz = f;
            // se agrega la raiz a la cola de prioridad.
            q.add(f);
        }

        //Se generan los codigos para cada simbolo
        List<Node>nodosCodificados = new ArrayList<>();
        listarCodigo(raiz, "",nodosCodificados);
        //Almacenamos los codigos, simbolo y probabilidad en un archivo txt
        almacenarArchivo(nodosCodificados);
        //Calculamos entropia,longitud media, longitud total y rendimiento
        calculosTeoricos(nodosCodificados,fuente1);
    }
}