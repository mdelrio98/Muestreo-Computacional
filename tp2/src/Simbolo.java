public class Simbolo implements Comparable<Simbolo>{
    private Integer simbolo;
    private float prob;

    public Simbolo(){
        this.simbolo = null;
        this.prob=0;
    }
    public Simbolo(Integer simbolo) {
        this.simbolo = simbolo;
        this.prob = 1;
    }

    public int getSimbolo() {
        return simbolo;
    }

    public void setSimbolo(Integer simbolo) {
        this.simbolo = simbolo;
    }

    public float getProb() {
        return prob;
    }

    public void setProb(float prob) {
        this.prob = prob;
    }

    public void sumar_aparicion(){
        this.prob = this.prob +1;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Simbolo simbolo1 = (Simbolo) o;
        return simbolo == simbolo1.simbolo && Float.compare(simbolo1.prob, prob) == 0;
    }



    @Override
    public int compareTo(Simbolo simbolo) {
        return Float.compare(this.prob,simbolo.prob);
    }
}
