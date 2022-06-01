import java.util.Comparator;

public class NodeComparator implements Comparator<Node> {
    public int compare(Node x, Node y)
    {

        return Float.compare(x.getProb(),y.getProb());
    }
}
