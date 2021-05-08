#include <iostream>
#include <algorithm>
int nums[10];
int ans[10];
using namespace std;

int find(int index, int n, int m){
    if(index == m){
        for(int i=0 ; i < m ;i++){
            cout << ans[i] << " ";
        }
        cout << "\n";
        return 0;
    }

    for(int i=0 ; i<n ; i++){
        if(index != 0 && ans[index-1] >= nums[i]) continue;
        ans[index] = nums[i];
        find(index + 1 , n, m);
    }
    return 0 ;
}

int main() {
    
    int N, M;
    cin >> N >> M;

    for(int i=0; i<N; i++){
        cin >> nums[i];
    }

    sort(nums, nums+N);
    find(0, N, M);
    
    return 0;
}

