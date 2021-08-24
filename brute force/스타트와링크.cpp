// BOJ https://www.acmicpc.net/problem/14889

#include <cmath>
#include <iostream>          
#include <algorithm>
#include <vector>
#include <deque>
#include <fstream>
#include <unordered_set>
#include <tuple>
#include <queue>
#include<string.h>
#include <cmath>

using namespace std;

long long INF = 1e9;
int n;
int arr[100][100];
int res = INF;
 
int main() {
    std::ifstream cin("data.txt");

    cin >> n;
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cin >> arr[i][j];
        }
    }
 
    vector<int> v;
    for(int i=0; i<n/2; i++){
        v.push_back(0);
    }
    for(int j=0; j<n/2; j++){
        v.push_back(1);
    }

    do{
        vector<int> ateam;
        vector<int> bteam;
        int a = 0;
        int b = 0;
        for(int i=0; i<n; i++){
            if(v[i] == 0){
                ateam.push_back(i);
            }
            else{
                bteam.push_back(i);
            }
        }
        for(int i=0; i<n/2 ; i++){
            for(int j=i+1; j<n/2; j++){
                int index1 = ateam[i];
                int index2 = ateam[j];
                a += arr[index1][index2];
                a += arr[index2][index1];

                index1 = bteam[i];
                index2 = bteam[j];
                b += arr[index1][index2];
                b += arr[index2][index1];
            }
        }

        res = min(res, abs(a-b));
    }while(next_permutation(v.begin(), v.end()));

    cout << res;
    return 0;
}


// 비트마스크
//https://velog.io/@skyepodium/%EB%B0%B1%EC%A4%80-14889-%EC%8A%A4%ED%83%80%ED%8A%B8%EC%99%80-%EB%A7%81%ED%81%AC