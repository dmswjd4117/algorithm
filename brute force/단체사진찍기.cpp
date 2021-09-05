// https://programmers.co.kr/learn/courses/30/lessons/1835?language=cpp

#include <string>
#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;

bool diff_check(char c, int diff, int num){
    if(c == '='){
        return diff == num;
    }else if(c == '>'){
        return diff > num;
    }else if(c == '<'){
        return diff < num;
    }
    return false;
}

int solution(int n, vector<string> data) {
    int answer = 0;
    
    string friends = "ACFJMNRT";
    do{
        bool flag = true;
        for(string order: data){
            char a = order[0];
            char b = order[2];
            char op = order[3];
            int num = order[4]-'0';
            int diff = abs(int(friends.find(a)-friends.find(b)))-1;
            if(!diff_check(op, diff, num)){
                flag = false;
                break;
            }
        }
        if(flag){
            answer += 1;
        }
    }while(next_permutation(friends.begin(), friends.end()));
    return answer;
}