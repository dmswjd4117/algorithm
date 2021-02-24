#include <iostream>
#include <vector>
#include <deque>
 
using namespace std;
 
int main(){
    int N;
    cin >> N;
    vector<int>nums(N);
    vector<int>answer(N, -1);
    for(int i=0 ; i<N; i++){
        cin >> nums[i];
    }

    deque<int> indexs;
    for(int index=0 ; index<N; index++){
        while(!indexs.empty()){
            int top_index = indexs.back();
            int top = nums[top_index];
            if(top < nums[index]){
                indexs.pop_back();
                answer[top_index] = nums[index];
            }else{
                break;
            }
        }
        indexs.push_back(index);
    }

    for(int i=0;i<N; i++){
        cout << answer.at(i) << " ";
    }
}

