#include <iostream>
#include <vector>
#include <cmath>
#include <queue>

using namespace std;

int check[100002];
int dist[100002];
int MAX = 100000;

int main() {
    int N, K;
    cin >> N >> K;
    queue<int> que;
    que.push(N);
    check[N] = 1;

    while (!que.empty()) {
        int top = que.front();
        que.pop();
        int a = top - 1;
        if (a >= 0 && check[a] != 1) {
            check[a] = 1;
            dist[a] = dist[top] + 1;
            que.push(a);
            if (a == K) {
                cout << dist[K];
                return 0;
            }
        }

        int b = top + 1;
        if (b <= MAX && check[b] != 1) {
            check[b] = 1;
            dist[b] = dist[top] + 1;
            que.push(b);
            if (b == K) {
                cout << dist[K];
                return 0;
            }
        }

        int c = top * 2;
        if (c <= MAX && check[c] != 1) {
            check[c] = 1;
            dist[c] = dist[top] + 1;
            que.push(c);
            if (c == K) {
                cout << dist[K];
                return 0;
            }
        }
    }

    cout << dist[K];
}