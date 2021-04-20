// dfs
#include <iostream>
#include <cstring>
#define PATH 0
#define WALL 1
#define VISITED 1
#define NOT_VISITED 0

void showPath();
int find(int x, int y, int count);

using namespace std;
int N;
int K;
int arr[100][100];
// 방문체크
int check[100][100];
// 답
int res = 0;

int moving[4][2] = {
    {1, 0}, {0, 1} , {-1, 0}, {0, -1} };


int main(void)
{
    int temp[10][10] = {
        {0,0,0,0,0},
        {0,0,0,1,0},
        {0,1,0,0,0},
        {0,0,0,0,0},
        {0,0,1,0,0}
    };

    N = 5;
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            arr[i][j] = temp[i][j];
        }
    }
    K = 10;


    find(0, 0, 0);
    cout << res << endl;


    // 초기화
    res = 0;
    memset(check, 0, sizeof(check));

    return 0;
}

int find(int x, int y, int count) {
    // 범위초과 ?
    if (count > K || x < 0 || y < 0 || x >= N || y >= N) {
        return 0;
    }
    // 길이 아니거나 방문했다면 리턴
    if (arr[x][y] != PATH || check[x][y] == VISITED) {
        return 0;
    }
    // 출구까지 길이가 K보다 길면 리턴
    if (count > K) {
        return 0;
    }

    if (x == N - 1 && y == N - 1) {
        res += 1;
        showPath();
        return 0;
    }

    check[x][y] = VISITED;
    find(x + 1, y, count + 1);
    find(x, y + 1, count + 1);
    find(x - 1, y, count + 1);
    find(x, y - 1, count + 1);
    check[x][y] = NOT_VISITED;

    return 0;
}

void showPath()
{
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cout << check[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;
}
