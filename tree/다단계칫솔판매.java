import java.util.*;
import java.util.Map.Entry;

class Solution {
    HashMap<String, String> parents = new HashMap<>();
    HashMap<String, Integer> money_map = new HashMap<>();
    
    public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {
        int[] answer = new int[enroll.length];
        
        for(int i=0; i< enroll.length; i++){
            String en = enroll[i];
            parents.put(en, referral[i]);
            money_map.put(en, 0);
        }
        
        for(int i=0; i< seller.length; i++){
            int temp = amount[i] * 100;
            go(seller[i], temp);
        }
        
        for(int i=0; i< enroll.length; i++){
            String en = enroll[i];
            answer[i] = money_map.get(en);
        }
        
        return answer;
    }
    
    
    
    public void go(String user, int money){
        String parent = parents.get(user);
        if(user.equals("-")){
            return;
        }
        
        int temp = money / 10;
        money_map.put(user, money_map.get(user)+money-temp);
        if(temp == 0){
            return;
        }
        go(parent, temp);
    }
    
}