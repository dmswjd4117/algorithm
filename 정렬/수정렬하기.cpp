#include <iostream>
#include <algorithm>

using namespace std;

int N;
int arr[1000001];
int merge(int start,int middle,int end);

void sorting(int start ,int end){
    if(end-start < 1)return;
    int middle = (start + end) / 2;

    sorting(start , middle);
    sorting(middle+1, end);

    merge(start , middle, end);
}


int merge(int start,int middle,int end){
    int left = start;
    int right = middle + 1;
    int index = 0;
    int dest[1000001];
    
    while(left <= middle && right <= end){
        if(arr[left] < arr[right]){
            dest[index] = arr[left];
            left++;
        }
        else{
            dest[index] = arr[right];
            right++;
        }
        index++;
    }

    if(left <= middle){
        for(int i=left ; i<=middle ; i++){
            dest[index] = arr[i];
            index++;
        }
    }
    else{
        for(int i=right ; i<=end ; i++){
            dest[index] = arr[i];
            index++;
        }
    }

    index = 0;
    for(int i=start ; i <= end ; i++){
        arr[i] = dest[index++];
    }
    return 0;
}


int main() {
  cin >> N;

  for(int i=0 ; i<N; i++){
      cin >> arr[i];
  }

  sorting(0, N-1);

  for(int i=0 ; i<N; i++){
      cout << arr[i] << "\n";
  }
}