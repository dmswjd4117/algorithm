#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef pair<int,int> P;
vector<P> arr;

bool comp(P a,P b) {
    if(a.second < b.second) {
        return true;
    }
    if(a.second == b.second) {
        return a.first < b.first;
    }
    return false;
}

int main() {

    int N;
    cin >> N;

    for(int i=0 ; i<N ; i++){
        int a , b;
        cin >> a >> b;
        arr.push_back({a, b});
    }

    sort(arr.begin(), arr.end(), comp);

    
    int temp = arr[0].second;
    int count = 1;

    for(int i=1 ; i<N ; i++){
        if(temp <= arr[i].first){
            count += 1;
            temp = arr[i].second;
        }
    }

    cout << count << '\n';

    return 0;
}