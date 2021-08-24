import java.util.*;

class Solution {
    String arr[] = new String[3];
    boolean vis[] = new boolean[3];
    String oper[] = {
        "+", "-", "*"
    };
    long answer = 0;
    List<String> operList = new ArrayList<>();
    List<Long> numList = new ArrayList<>();
    
    public long solution(String expression) {
        String num = "";
        for(int i=0; i<expression.length(); i++){
            char e = expression.charAt(i);
            if(e == '-' || e == '*' || e == '+'){
                numList.add(Long.parseLong(num));
                num = "";
                operList.add(e+"");
            }else{
                num += e;
            }
        }
        numList.add(Long.parseLong(num));
        
        perm(0, 3);
        
        return answer;
    }
    
    public void solve(){
        List<String> opers = new ArrayList<>();
        opers.addAll(operList);
        List<Long> nums = new ArrayList<>();
        nums.addAll(numList);
        
        for(int i=0; i<3; i++){
            String cur_op = arr[i];
            int index = 0;
            while(index < opers.size()){
                String operator = opers.get(index);
                if(operator.equals(cur_op)){
                    Long res = calcul(nums.get(index), nums.get(index+1), cur_op);
                    nums.add(index, res);
                    nums.remove(index+1);
                    nums.remove(index+1);                
                    opers.remove(index);
                }else{
                    index += 1;
                }
            }
        }
        
        Long res = nums.get(0);
        answer = Math.max(answer , Math.abs(res));
        
    }
    
    public Long calcul(Long a, Long b, String op){
        if(op.equals("+")){
            return a+b;
        }
        if(op.equals("-")){
            return a-b;
        }
        if(op.equals("*")){
            return a*b;
        }
        return 1L;
    }
    
    public void perm(int index, int length){
        if(index == length){
            solve();
            return;
        }
        
        for(int i=0; i<length; i++){
            if(vis[i]){
                continue;
            }
            vis[i] = true;
            arr[index] = oper[i];
            perm(index+1, length);
            vis[i] = false;
        }
    }
}