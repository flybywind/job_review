package PerplexProblem;

public class PerplexFunc {
    public int m(int f, int g) {
        try {
            int[] far = new int[f];
            far[g] = 1;
            return f;
        } catch(NegativeArraySizeException e) {
            f = -f;
            g = -g;
            return (-m(f, g) == -f) ? -g : -f;
        } catch(IndexOutOfBoundsException e) {
            return (m(g, 0) == 0) ? f : g;
        }
    }

    public static void main(String[] args) {
        PerplexFunc f = new PerplexFunc();
        System.out.printf("m(1,2) = %d\n", f.m(1,2));
        System.out.printf("m(-1,2) = %d\n", f.m(-1,2));
        System.out.printf("m(1,-2) = %d\n", f.m(1,-2));
        System.out.printf("m(5,2) = %d\n", f.m(5,2));
        System.out.printf("m(-5,2) = %d\n", f.m(-5,2));
        System.out.printf("m(5,-2) = %d\n", f.m(5,-2));
        System.out.printf("m(-5,-2) = %d\n", f.m(-5,-2));
    }
}
