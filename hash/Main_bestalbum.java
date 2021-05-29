package hash;

// https://programmers.co.kr/learn/courses/30/lessons/42579?language=java

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        int[] answer = {};
        ArrayList<Integer> tempA = new ArrayList<Integer>();
        HashMap<String, Integer> hash = new HashMap<>();
        for(int i=0; i<genres.length; i++){
            hash.put(genres[i], hash.getOrDefault(genres[i], 0)+plays[i]);
        }
        List<String> keySet = new ArrayList<>(hash.keySet());
        Collections.sort(keySet, new Comparator<String>(){
            public int compare(String s1, String s2){
                if(hash.get(s1) < hash.get(s2)){
                    return 1;
                }
                if(hash.get(s1) > hash.get(s2)){
                    return -1;
                }
                return 1;
            }
        });
        
        // System.out.println(keySet);

        for(String key: keySet){
            HashMap<Integer, Integer> playHash = new HashMap<>();
            for(int i=0; i<genres.length; i++){
                if(genres[i].equals(key)){
                    playHash.put(i, plays[i]);
                }
            }
            List<Integer> keySetList = new ArrayList<Integer>(playHash.keySet());
            Collections.sort(keySetList, (o1, o2)->(playHash.get(o2).compareTo(playHash.get(o1))));
            
            for(int i=0; (i<keySetList.size())&&(i<2) ; i++){
                tempA.add(keySetList.get(i));
            }
        }

        answer = new int[tempA.size()];
        for(int i=0; i<tempA.size(); i++){
            answer[i] = tempA.get(i);
        }

        return answer;
    }
}

class Main_bestalbum {
    public static void main(String[] args) {
        Solution s = new Solution();
        String[] str = {"classic", "pop", "classic", "classic", "pop"};
        int[] plays = {500, 600, 150, 800, 2500};
        int ans[] = s.solution(str, plays);
        for(Integer a:ans){
            System.out.println(a);
        }
    }
}

/*
put(키, value) -> 키, value 저장
get('키') -> value 가져오기
map.keySet() -> 키들 확인 가능

Arrays.sort -> Dual-Pivot Quicksort (unstable)
Collections.sort -> timsort (stable)
*/