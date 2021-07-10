// BOJ https://www.acmicpc.net/problem/16936

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

using namespace std;
long long INF = 1e9;
long long n;
unordered_set<long long> us;
unordered_set<long long> check;
long long ans[102];

bool isin(long long x) {
    return us.count(x) == 1;
}

bool go(int index, long long x) {
    ans[index] = x;
    if (index == n) {
        return true;
    }

    long long tx = x * 2;
    if (isin(tx) && check.count(tx) == 0) {
        check.insert(tx);
        if (go(index + 1, tx)) {
            return true;
        }
        check.erase(tx);
    }

    if (x % 3 == 0) {
        long long tx = x / 3;
        if (isin(tx) && check.count(tx) == 0) {
            check.insert(tx);

            if (go(index + 1, tx)) {
                return true;
            }

            check.erase(tx);
        }
    }

    return false;
}

int main() {
    std::ifstream cin("data.txt");

    cin >> n;
    vector<long long>nums;
    for (int i = 0; i < n; i++) {
        long long a;
        cin >> a;
        us.insert(a);
    }


    for(long long  num : us){
        if (go(1, num)) {
            for (int j = 1; j <= n; j++) {
                cout << ans[j] << " ";
            }
            return 0;
        }
    }

    return 0;
}

// https://velog.io/@hschoi1104/BOJ-16936-%EB%82%983%EA%B3%B12
// https://kimcodingvv.github.io/BOJ-16936/