
#include <iostream>
#include <algorithm>
#include <cstring>
#include <cmath>

using namespace std;

int dir[5][2] = { {0,0}, {1,0}, {0,1}, {-1,0}, {0,-1} };

int arr[1000][1000];

int main() {

    int N ;
    cin >> N;
    int find;
    cin >> find;

    int col = N;
    int row = N - 1;

    int num = N * N;
    int x = -1;
    int y = 0;
    int dir = 1;

    while (num != 0) {
        for (int i = 0; i < col; i++) {
            x += dir;
            arr[x][y] = num;
            num -= 1;
        }
        col -= 1;

        for (int i = 0; i < row; i++) {
            y += dir;
            arr[x][y] = num;
            num -= 1;
        }
        row -= 1;

        dir *= -1;
    }

    int res_x = 0, res_y = 0; 
    for (int j = 0; j < N; j++) {
        for (int i = 0; i <  N; i++) {
            if (arr[i][j] == find) { 
                res_x = i+1; 
                res_y = j+1; 
            }
            cout << arr[j][i] << " ";
        }
        cout << "\n";
    }

    cout << res_x << " " << res_y;
    return 0;
}

