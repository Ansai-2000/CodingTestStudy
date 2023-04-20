import jdk.jshell.EvalException;

import java.lang.reflect.Array;
import java.util.*;
import java.io.*;
public class Main {
    static int V,E,K;
    static ArrayList<Edge>[] A;
    static boolean[] visited;
    static int[] distance;
    static PriorityQueue<Edge> q = new PriorityQueue<>();
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(br.readLine());

        A = new ArrayList[V+1];
        visited = new boolean[V+1];
        distance = new int[V+1];
        for(int i=1;i<=V;i++){
            A[i] = new ArrayList<>();
        }
        for(int i=1;i<=V;i++){
            distance[i] = Integer.MAX_VALUE;
        }
        for(int i=0;i<E;i++){
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            A[u].add(new Edge(v,w));
        }
        q.add(new Edge(K,0));
        distance[K] = 0;
        while(!q.isEmpty()){
            Edge now = q.poll();
            int now_v = now.vertex;
            if(visited[now_v]) continue;
            visited[now_v] = true;
            for(Edge tmp:A[now_v]){
                
                int next = tmp.vertex;
                int value = tmp.value;
                if(distance[next] > distance[now_v] + value){
                    distance[next] = distance[now_v] + value;
                    q.add(new Edge(next,distance[next]));
                }
            }
        }
        for(int i=1;i<=V;i++){
            if(visited[i]){
                System.out.println(distance[i]);
            }
            else System.out.println("INF");
        }
    }
    static class Edge implements Comparable<Edge>{
        int vertex, value;
        Edge(int vertex,int value){
            this.vertex = vertex;
            this.value = value;
        }
        @Override
        public int compareTo(Edge e) {
            if(this.value>e.value){
                return 1;
            }
            else return -1;
        }
    }
}


