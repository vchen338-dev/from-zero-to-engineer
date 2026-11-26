import java.util.ArrayList;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        // 1. Single-dimensional array (fixed length)
        int[] numbers = new int[4];              // [0, 0, 0, 0]
        int[] initialized = {10, 20, 30, 40};
        int[] explicitNew = new int[]{1, 2, 3};
        String[] names = {"Ana", "Ben", "Cara"};

        // 2. Multidimensional array (array of arrays; rows can vary in length)
        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6}
        };

        int[][] jagged = new int[2][];
        jagged[0] = new int[]{10, 20};
        jagged[1] = new int[]{30, 40, 50};

        // 3. Resizable alternative (ArrayList)
        ArrayList<Integer> dynamicList = new ArrayList<>(Arrays.asList(5, 6));
        dynamicList.add(7);

        System.out.println(initialized[0]);      // 10
        System.out.println(names[1]);            // Ben
        System.out.println(matrix[1][2]);        // 6
        System.out.println(jagged[1][2]);        // 50
        System.out.println(dynamicList.size());  // 3
    }
}