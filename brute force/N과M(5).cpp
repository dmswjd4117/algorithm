#include <iostream>
#include <algorithm>

using namespace std;
int nums[10];
int ans[10];
bool c[10];

int find(int index, int n, int m){
    if (index == m) {
        for (int i=0; i<m; i++) {
            cout << ans[i];
            if (i != m-1) cout << ' ';
        }
        cout << '\n';
        return 0;
    }
    for(int i=0 ; i < n ; i++ ){
        if(c[i]) continue;
        ans[index] = nums[i];
        c[i] = true;
        find(index +1 , n, m);
        c[i] = false;
    }
    return 0;
}

int main() {
    int n, m;
    cin >> n >> m;
    for(int i=0 ; i< n; i++){
        cin >> nums[i];
    }

    sort(nums, nums+n);
    find(0, n, m);
    return 0;
}
