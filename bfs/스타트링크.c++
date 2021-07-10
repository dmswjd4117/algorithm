// BOJ https://www.acmicpc.net/problem/5014
// 1 

#include <iostream>          
#include <algorithm>
#include <vector>
#include <deque>
#include <fstream>
#include <unordered_set>
#include <tuple>
#include <queue>

using namespace std;
int INF = 1e9;
int f,s,g,u,d;
bool isin(int x){
    if(1 <= x && x <= f){
        return true;
    }
    return false;
}
bool vis[1000002];

int main(){
    std::ifstream cin("data.txt");

    cin >> f >> s >> g >> u >> d;

    deque<pair<int, int>> q;
    q.push_back(make_pair(0, s));

    while(!q.empty()){
        int cnt = q.front().first;
        int x = q.front().second;
        q.pop_front();
        if(x == g){
            cout << cnt;
            return 0;
        }
 

        int tx = x + u;
    
        if(isin(tx) && !vis[tx]){
            q.push_back(make_pair(cnt+1, tx));
            vis[tx] = true;
        }

        tx = x - d;
        if(isin(tx) && !vis[tx]){
            q.push_back(make_pair(cnt+1, tx));
            vis[tx] = true;
        }
    }
    
    cout << "use the stairs";
    return 0;
}


// 2

#include <iostream>          
#include <algorithm>
#include <vector>
#include <deque>
#include <fstream>
#include <unordered_set>
#include <tuple>
#include <queue>
#include<string.h>

using namespace std;
int INF = 1e9;
int f,s,g,u,d;
bool isin(int x){
    if(1 <= x && x <= f){
        return true;
    }
    return false;
}
bool vis[1000002];
int dist[1000002];

int main(){
    std::ifstream cin("data.txt");
    cin >> f >> s >> g >> u >> d;

    priority_queue<pair<int, int>> hq;
    hq.push(make_pair(0, s));

    for(int i=0; i<=f; i++){
        dist[i] = INF;
    }

 
    
    while(!hq.empty()){
        int cnt = hq.top().first;
        int x = hq.top().second;
        hq.pop();

        if(x == g){
            cout << cnt;
            return 0;
        }
 

        int tx = x + u;
 
        if(isin(tx) && dist[tx] > cnt+1){
            dist[tx] = cnt + 1;
            hq.push(make_pair(cnt+1, tx));
        }

        tx = x - d;
        if(isin(tx) && dist[tx] > cnt+1){
            dist[tx] = cnt + 1;
            hq.push(make_pair(cnt+1, tx));
        }
    }
    
    cout << "use the stairs";
    return 0;
}
