using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        // 1. Single-dimensional array (fixed length)
        int[] numbers = new int[4];              // [0, 0, 0, 0]
        int[] initialized = { 10, 20, 30, 40 };
        int[] explicitNew = new int[] { 1, 2, 3 };
        string[] names = ["Ana", "Ben", "Cara"]; // C# 12+ collection expression

        // 2. Multidimensional (rectangular) array [rows, columns]
        int[,] matrix = new int[2, 3]
        {
            { 1, 2, 3 },
            { 4, 5, 6 }
        };

        // 3. Jagged array (array of arrays; rows can have different lengths)
        int[][] jagged = new int[2][];
        jagged[0] = [10, 20];
        jagged[1] = [30, 40, 50];

        // 4. Resizable alternative (List<T>)
        List<int> dynamicList = [5, 6];
        dynamicList.Add(7);

        Console.WriteLine(initialized[0]);   // 10
        Console.WriteLine(names[1]);         // Ben
        Console.WriteLine(matrix[1, 2]);      // 6
        Console.WriteLine(jagged[1][2]);     // 50
        Console.WriteLine(dynamicList.Count); // 3
    }
}