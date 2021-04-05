#include <iostream>
#include <vector>

using namespace std;

int N, M;
int vis[30];
int ans[22][22];
int moving[4][2] = {
    {-1, 0}, {0,1}, {1,0}, {0,-1}
};

int go(vector<vector<int>> &arr, int x, int y) {
    vis[arr[x][y]] = 1;

    for(int i=0 ; i<4; i++){
        int tx = x + moving[i][0];
        int ty = y + moving[i][1];
        if(tx<0||ty<0||tx>=N||ty>=M) continue;
        if(vis[arr[x][y]]) continue;
    }

    vis[arr[x][y]] = 0;
    return 0;
}

int main() {

  cin >> N >> M;
  vector<vector<int>> arr (N+1);
  
  int A = (int)'A';
  for(int i=0; i<N;i++){
      string str ;
      cin >> str;
      for(int j=0; j<str.size();j++){
        int ch = (int)str[j]-A;
        arr[i].push_back(ch);
      }
  }

  go(arr, 0, 0);


  return 0;
}


//   for(int i=0; i<N;i++){
//       for(int j=0; j<M;j++){
//         cout << arr[i][j] << " ";
//       }
//       cout << endl;
//   }