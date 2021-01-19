#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;

int graph[30][30];
int check[30][30];
int n;
int home_count = 0;

int find(int x,int y){
    if(x < 0 || y < 0 || x >= n || y >= n) return false;

    if(!graph[x][y] || check[x][y]) return false;

    check[x][y] = 1;
    home_count += 1;
    find(x+1, y);
    find(x, y+1);
    find(x-1, y);
    find(x, y-1);
    return true;
}

int main() {
    cin >> n;
    
    for(int i=0; i<n; i++){
        string line;
        cin >> line;
        for(int j=0 ; j<n ; j++){
            graph[i][j] = line[j] - '0';
        }
    }

    int sum = 0;
    vector<int> answer;
    for(int i=0; i<n; i++){
        for(int j=0; j<n;j++) {
            int t = find(i, j);
            if(t){
                sum += 1;
                answer.push_back(home_count);
                home_count = 0 ;
            }
        }
    }

    cout << sum << "\n";
    sort(answer.begin(), answer.end());
    for(int i=0 ; i<answer.size() ; i++){
        cout << answer[i] <<  "\n";
    }
    return 0;
}