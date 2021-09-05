import java.util.*;

class Solution {
    public String solution(String p) {
        String answer = go(p);
        return answer;
    }
    
    public String go(String string){
        if(string.equals("")){
            return "";
        }
        
        int index = balanced_index(string);
        String left = string.substring(0, index+1);
        String right = string.substring(index+1);
        
        if(isRight(left)){
            String res = left + go(right);
            return res;
        }
        
        String res =   "(" + go(right) + ")";
        for(int i=1; i<left.length()-1; i++){
            char c = left.charAt(i);
            if(c == '('){
                res += ")";
            }else{
                res += "(";
            }
        }
        return res;
    }
    
    public boolean isRight(String string){
        int cnt = 0;
        for(int i=0; i<string.length(); i++){
            if(cnt == -1){
                return false;
            }
            char c = string.charAt(i);
            if(c == '('){
                cnt += 1;
            }else{
                cnt -= 1;
            }
        }
        return true;
    }
    
    public int balanced_index(String string){
        int left = 0;
        int right = 0;
        for(int i=0; i<string.length(); i++){
            char c = string.charAt(i);
            if(c == '('){
                left += 1;
            }else{
                right += 1;
            }
            if(left == right){
                return i;
            }
        }
        return string.length()-1;
    }
}