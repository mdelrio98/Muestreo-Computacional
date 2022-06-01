import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.*;
public class Main {
    public static void almacenarArchivo(List<Node>data){
        PrintWriter printWriter = null;

        try {
                printWriter = new PrintWriter("archivoCod.txt");
        } catch (FileNotFoundException e) {
                System.out.println("Unable to locate the fileName: " + e.getMessage());
        }
        for (Node nodos : data) {
            Objects.requireNonNull(printWriter).println(nodos.getSimbolo()+"|"+nodos.getProb()+"|"+nodos.getCodigo());
        }
        printWriter.close();
    }
    public static void printCode(Node root, String s, List<Node>data)
    {
        if (root.left == null && root.right == null) {

            System.out.println("S: "+ root.getSimbolo()+ " |C: " + s +" |P: " + root.getProb());
            root.sumarcodigo(s);
            data.add(root);

            return;
        }
        printCode(root.left, s + "0");
        printCode(root.right, s + "1");
    }

    // main function
    public static void main(String[] args)throws FileNotFoundException {


        Fuente fuente1 = new Fuente();
        ArrayList<Node> lnodos = fuente1.generar_Lista_proba();// generamos nuestra fuente en una lista de nodos
        PriorityQueue<Node> q = new PriorityQueue<Node>(lnodos.size(), new NodeComparator());

        q.addAll(lnodos);

        Node root = null;
        while (q.size() > 1) {

            // first min extract.
            Node x = q.peek();
            q.poll();

            // second min extract.
            Node y = q.peek();
            q.poll();

            //generamos el nodo intermedio con la suma de las probs de los simbolos mas pequeños
            // no lleva simbolo
            Node f = new Node();

            f.setProb(x.getProb() + y.getProb());
            // to the sum of the frequency of the two nodes
            // assigning values to the f node.

            // first extracted node as left child.
            f.left = x;

            // second extracted node as the right child.
            f.right = y;

            // marking the f node as the root node.
            root = f;

            // add this node to the priority-queue.
            q.add(f);
        }

        // print the codes by traversing the tree
        List<Node>data = new ArrayList<>();
        printCode(root, "",data);
        almacenarArchivo(data);
        double longM = 0.0;
        for(Node nodo: data){
             longM += nodo.longCodigo() * nodo.getProb();
            System.out.println("Long media: "+ longM);
        }
        double entropia = fuente1.CalcularEntropia();
        System.out.println("Entropia: "+ entropia);
        double r = Main.calcularRendimiento(entropia,longM);
        System.out.println("Rendimiento: "+ r);
    }

    private static double calcularRendimiento(double h, double l) {
        return h/l;
    }

}
