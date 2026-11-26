#include <array>
#include <iostream>
#include <vector>

int main() {
    // 1. Basic C-style array (fixed size)
    int numbers[4] = {10, 20, 30, 40};
    int zeros[5] = {}; // all 0

    // 2. Modern fixed-size array
    std::array<int, 3> fixed_arr = {1, 2, 3};

    // 3. Resizable array (vector)
    std::vector<int> dyn_arr = {5, 6};
    dyn_arr.push_back(7);

    // 4. 2D array (rows and columns)
    int grid[2][3] = {
        {1, 2, 3},
        {4, 5, 6}
    };

    std::cout << numbers[0] << "\n";    // 10
    std::cout << zeros[0] << "\n";      // 0
    std::cout << fixed_arr[1] << "\n";  // 2
    std::cout << dyn_arr[2] << "\n";    // 7
    std::cout << grid[1][2] << "\n";    // 6

    return 0;
}