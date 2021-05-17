#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>
#include <cstring>

using namespace std;
// 1은 땅 0은 바다 !!
// x = H (높이),  y = W (너비)

int W = 1, H = 1 ;
int graph[51][51];
bool check[51][51];

int find(int x, int y){
    if(x<0 || y <0 || x>= H || y >= W) return false;
    if(!graph[x][y] || check[x][y]) return false;
    
    check[x][y] = true;
    find(x+1, y);
    find(x, y+1);
    find(x-1, y);
    find(x, y-1);

    find(x-1, y-1);
    find(x-1, y+1);
    find(x+1, y-1);
    find(x+1, y+1);

    return true;
}

int main() {

    while(1){
        int island_count = 0;

        cin >> W >> H;
        if(W == 0 && H == 0) return 0;

        for(int i=0 ; i<H ; i++){
            for(int j=0 ; j< W ; j++){
                cin >> graph[i][j];
            }
        }

        for(int i=0 ; i<H ; i++){
            for(int j=0 ; j< W ; j++){
                int t = find(i, j);
                if(t){
                    island_count += 1;
                }
            }
        }

        cout << island_count << "\n";
        memset(check, false, sizeof(check));
    }
     
    return 0;
}
