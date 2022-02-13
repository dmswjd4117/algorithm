import java.util.*;

class Solution {
    public boolean solution(String[] book) {
        boolean answer = true;

        HashSet<String> hashSet = new HashSet<>();

        for(int i=0; i<book.length; i++){
            hashSet.add(book[i]);
        }


        for(String num: book){
            for(int i=0; i<num.length()-1; i++){
                String compNum = num.substring(0, i+1);
                if(hashSet.contains(compNum)){
                    return false;
                }
            }
        }

        return answer;
    }
}


// 테스트 1 〉	통과 (2.74ms, 74.9MB)
// 테스트 2 〉	통과 (3.38ms, 57.9MB)
// 테스트 3 〉	통과 (282.36ms, 245MB)
// 테스트 4 〉	통과 (212.25ms, 130MB)


import java.util.*;

class Solution {
    public boolean solution(String[] book) {
        boolean answer = true;
        
        HashSet<String>[] setArr = new HashSet[30];
        
        for(int i=0; i<30; i++){
            setArr[i] = new HashSet<>();
        }
        
        for(String num: book){
            int size = num.length();
            setArr[size].add(num);
        } 
        
        
        for(String num: book){
            int size = num.length();
            for(int i=0; i<size-1; i++){
                String compNum = num.substring(0, i+1);
                if(setArr[i+1].contains(compNum)){
                    return false;
                }
            }
        }
        
        return answer;
    }
}


// 효율성  테스트
// 테스트 1 〉	통과 (6.67ms, 59MB)
// 테스트 2 〉	통과 (3.07ms, 56.5MB)
// 테스트 3 〉	통과 (294.79ms, 247MB)
// 테스트 4 〉	통과 (174.61ms, 135MB)