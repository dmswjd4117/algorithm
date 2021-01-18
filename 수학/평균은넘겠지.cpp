#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int T;
    cin >> T;

    cout << fixed;
    cout.precision(3);
    for(int i=0 ; i< T ; i++){
        int n;
        cin >> n;

        int s[1001];
        int sum = 0;
        for(int i=0 ; i<n ;i++){
            cin >> s[i];
            sum += s[i];
        }

        double avg = sum/ (double)n;
        int count = 0;
        for(int i=0 ; i<n ; i++){
            if(s[i] > avg) count += 1;
        }

        double ratio = ((double)count / n) * 100 ;
        cout << ratio << "%\n"; 
    }
    return 0;
}
