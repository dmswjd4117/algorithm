// https://gmlwjd9405.github.io/2018/09/06/java-comparable-and-comparator.html
package tree;

import java.util.*;

class Edge {
    int to, cost;
    Edge(int to, int cost){
        this.to = to;
        this.cost = cost;
    }
}

class EdgeComp implements Comparator<Edge> {
    public int compare(Edge one, Edge two){
        return Integer.compare(one.cost, two.cost);
    }
}

public class Main_1922 {
    static Scanner kb = new Scanner(System.in);
    static int N,M;
    static ArrayList<Edge>[]  edges;
    public static void main(String[] args) {
        N = kb.nextInt();
        M = kb.nextInt();
        edges = new ArrayList[N+1];
        for(int i=1; i<N+1; i++){
            edges[i] = new ArrayList<>();
        }
        for(int i=0; i<M; i++){
            int a, b, c;
            a = kb.nextInt();
            b = kb.nextInt();
            c = kb.nextInt();
            edges[a].add(new Edge(b, c));
            edges[b].add(new Edge(a, c));
        }

        int ans = prim(1);
        System.out.println(ans);
    }

    public static int prim(int start){
        int ans = 0;
        boolean[] vis = new boolean[N+1];
        PriorityQueue<Edge> q = new PriorityQueue<Edge>(1, new EdgeComp());
        vis[start] = true;
        for(Edge edge:  edges[start]){
            q.add(edge);
        }
        while(!q.isEmpty()){
            Edge e = q.poll();
            if(vis[e.to] == true) continue;
            vis[e.to] = true;
            ans += e.cost;
            for(Edge next_edge : edges[e.to]){
                q.add(next_edge);
            }
        }
        return ans;
    }
}
