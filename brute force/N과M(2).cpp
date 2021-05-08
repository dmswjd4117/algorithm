#include <iostream>
using namespace std;
// i을 배열에 포함시켰는지 아닌지
// 포함되었으면 true 포함안되었으면 false
bool c[10];
// a배열에 수열들을 담는당
int a[10]; 

void go(int index, int n, int m) {
    if (index == m) {
        for(int i=0 ; i<m ; i++){
            cout << a[i] << " ";
        }
        cout << "\n";
        return;
    }
    
    for(int i=1 ; i<= n ;i++){
        if(c[i]) continue;
        if(index != 0 && a[index-1] > i) continue; 
        a[index] = i;
        c[i] = true; 
        go(index+1, n, m);
        c[i] = false;
    }
}

int main() {
    int n, m;
    cin >> n >> m;
    go(0,n,m);
    return 0;
}