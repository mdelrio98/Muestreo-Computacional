import java.io.FileNotFoundException;
import java.util.*;

public class Main {
    // recursive function to print the
    // huffman-code through the tree traversal.
    // Here s is the huffman - code generated.
    public static void printCode(Node root, String s)
    {
        if (root.left == null && root.right == null) {

            // c is the character in the node
            System.out.println("S: "+ root.getSimbolo()+ " |C: " + s +" |P: " + root.getProb());

            return;
        }
        printCode(root.left, s + "0");
        printCode(root.right, s + "1");
    }

    // main function
    public static void main(String[] args)throws FileNotFoundException {


        Fuente fuente1 = new Fuente();
        ArrayList<Node> lnodos = fuente1.generar_Lista_proba();// generamos nuestra fuente en una lista de nodos
        // creating a priority queue q.
        // makes a min-priority queue(min-heap).
        for (int i=0; i <lnodos.size();i++){System.out.println("sim: "+ lnodos.get(i).getSimbolo() + " prob:" + lnodos.get(i).getProb()) ;}
        PriorityQueue<Node> q = new PriorityQueue<Node>(lnodos.size(), new NodeComparator());

        q.addAll(lnodos);
/*
       while(!q.isEmpty()){
            System.out.println("Simbolo: "+ q.peek().getSimbolo()+ " proba: " +q.peek().getProb());
            q.poll();
        }*/
        // create a root node
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

        printCode(root, "");
    }

}
