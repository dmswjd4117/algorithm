#include <iostream>
#include <vector>
#include <queue>
using namespace std;

#define MAX 100002
int check[MAX];
int ans[MAX];
queue<int> que;

int main() {

    vector<int>node[MAX];
    int answer [MAX];

    int N;
    cin >> N;

    for(int i=0 ; i < N-1; i++) {
        int a,b ;
        cin >> a >> b;
        node[a].push_back(b);
        node[b].push_back(a);
    }

    que.push(1);
    check[1] = true;
    
    while(!que.empty()) {
        int root = que.front();
        que.pop();

        for(int child : node[root]){
            if(check[child] == true) continue;
            que.push(child);
            check[child] = true;
            ans[child] = root;
        }
    }

    for(int i=2 ; i<= N; i++){
        cout << ans[i] << '\n';
    }
    
    return 0;
}