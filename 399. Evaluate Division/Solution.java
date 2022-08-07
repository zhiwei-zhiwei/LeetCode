import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        int equationsSize = equations.size();

        UnionFind unionFind = new UnionFind(2 * equationsSize);
        // 预处理，将变量的值与id进行映射，是并查集的底层使用数组实现
        Map<String, Integer> hashMap = new HashMap<>(2 * equationsSize);
        int id = 0;
        for(int i = 0; i < equationsSize; i++){
            List<String> equation = equations.get(i);
            String var1 = equation.get(0); // first string
            String var2 = equation.get(1); // second string

            if(!hashMap.containsKey(var1)){
                hashMap.put(var1,id);
                id++;
            }
            if(!hashMap.containsKey(var2)){
                hashMap.put(var2,id);
                id++;
            }
            unionFind.union(hashMap.get(var1), hashMap.get(var2), values[i]);
        } 
        // do seaching
        int queriesSize = queries.size();
        double[] res = new double[queriesSize];
        for(int i = 0; i < queriesSize; i++){
            String var1 = queries.get(i).get(0);
            String var2 = queries.get(i).get(1);

            Integer id1 = hashMap.get(var1);
            Integer id2 = hashMap.get(var2);

            if (id1 == null || id2 == null){
                res[i] = -1.0d; // when there is no such a string in equations
            }else{
                res[i] = unionFind.isConnected(id1,id2);
            }
        }
        return res;
    }

    private class UnionFind{
        private int[] parent;
        private double[] weight;

        public UnionFind(int n){
            this.parent = new int[n];
            this.weight = new double[n];
            for (int i = 0; i < n; i++){
                parent[i] = i;
                weight[i] = 1.0d;
            }
        }

        public void union(int x, int y, double value){
            int rootX = find(x);
            int rootY = find(y);
            if (rootX == rootY){
                // the root is same, so they do not need to do disjoi
                return;
            }
            parent[rootX] = rootY;
            weight[rootX] = weight[y] * value / weight[x]; // update the weight to the root
        }

        // comprese the root
        // return root id
        public int find(int x){
            if (x != parent[x]){
                // when x is not root node
                int origin = parent[x];
                parent[x] = find(parent[x]); // look up, recursive
                weight[x] *= weight[origin];
            }
            return parent[x];
        }
        public double isConnected(int x, int y){
            int rootX = find(x);
            int rootY = find(y);
            if (rootX == rootY){
                // when the root node is same, already did the disjoiunt action
                return weight[x]/weight[y];
            }else{
                return -1.0d;
            }
        }
    }
}
