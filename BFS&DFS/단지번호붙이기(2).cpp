#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>
#include <cstring>

using namespace std;

// 세로 가로 개수
int n;
// 원래 그래프
int graph[30][30];
// 방문한뒤 그래프
int after[30][30];
// 움직이는 방향
int moving[4][4] = { {-1, 0}, {0, 1}, {1, 0}, {0, -1}};

void dfs(int x, int y, int cnt){

    after[x][y] = cnt;
    for(int i=0; i<4 ; i++){
        int nx = x + moving[i][0];
        int ny = y + moving[i][1];
        if( 0 <= nx && nx < n && 0 <= ny && ny < n){
            if( graph[nx][ny] == 1 && after[nx][ny] == 0) {
                dfs(nx, ny, cnt);
            }
        }
    }
}

int main() {

    scanf("%d",&n);
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            scanf("%1d",&graph[i][j]);
        }
    }

    int cnt = 0;
    for(int i=0; i<n ; i++){
        for(int j=0 ; j<n ; j++){
            if(graph[i][j] && after[i][j] == 0){
                dfs(i, j, ++cnt);
            }
        }
    }

    cout << cnt << endl;

    int answers[30*30];
    memset(answers, 0, sizeof(answers));
    for(int i=0 ; i<n ; i++){
        for(int j=0 ; j<n ; j++){
            int t = after[i][j];
            if(t) answers[t] += 1;
        }
    }

    sort(answers, answers+cnt+1);

    for(int i=1 ; i <= cnt ; i++){
        cout << answers[i] << "\n";
    }

    return 0;
}
