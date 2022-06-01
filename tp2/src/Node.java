import java.util.Objects;

public class Node {
        private Integer simbolo;
        private float prob;
        private String codigo;
        Node left;
        Node right;

        public Node (){}

        public Node(Integer simbolo) {
            this.left= null;
            this.right=null;
            this.simbolo = simbolo;
            this.prob = 1;
            this.codigo="";
        }
        public Node(Float p) {
            this.prob=p;
            this.left= null;
            this.right=null;
            this.codigo="";
        }

        public int getSimbolo() {
            return simbolo;
        }

        public void setSimbolo(Integer simbolo) {
            this.simbolo = simbolo;
        }

        public void sumarcodigo(String s) {this.codigo = this.codigo+ s;}

        public void setProb(float prob) {
            this.prob = prob;
        }

        public float getProb() {
            return prob;
        }
        public String getCodigo(){return this.codigo;}

        public void sumar_aparicion(){this.prob = this.prob +1;}


        @Override
        public boolean equals(Object o) {

            Node node = (Node) o;
            return simbolo.equals(node.simbolo);
        }
        public int longCodigo(){
            return this.getCodigo().length();
        }

        
}

