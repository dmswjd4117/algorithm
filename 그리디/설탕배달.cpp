#include <iostream>
#include <algorithm>

using namespace std;



int main() {
  int N ;
  cin >> N;

  int five_cnt = N / 5;
  while(five_cnt != -1){
      int na = N - 5 * five_cnt;

      if(na % 3 == 0){
          int three_cnt = na / 3;
          cout << five_cnt + three_cnt << "\n";
          break; 
      }

      five_cnt --;
  }

  if(five_cnt == -1){
      cout << -1;
  }
}