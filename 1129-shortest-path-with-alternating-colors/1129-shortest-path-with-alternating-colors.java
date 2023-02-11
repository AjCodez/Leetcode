class Solution {
    private int[] h, e, ne, v;
    private int idx;
    public int[] shortestAlternatingPaths(int n, int[][] redEdges, int[][] blueEdges) {
        this.h = new int[n];
        Arrays.fill(h, -1);
        int m = redEdges.length + blueEdges.length;
        this.e = new int[m];
        this.ne = new int[m];
        this.v = new int[m];
        this.idx = 0;
        for (int[] e : redEdges) add(e[0], e[1], 0);
        for (int[] e : blueEdges) add(e[0], e[1], 1);
        Queue<int[]> q = new ArrayDeque<>();
        int[][] vis = new int[n][2];
        int[] rst = new int[n];
        Arrays.fill(rst, -1);
        rst[0] = 0;
        vis[0][0] = 1;
        vis[0][1] = 1;
        for (int i = h[0]; i != -1; i = ne[i]) {
            int j = e[i];
            if (vis[j][v[i]] == 1) continue;
            q.offer(new int[]{j, v[i]});
            vis[j][v[i]] = 1;
        }
        int step = 1;
        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                int[] tmp = q.poll();
                if (rst[tmp[0]] == -1) rst[tmp[0]] = step;
                for (int j = h[tmp[0]]; j != -1; j = ne[j]) {
                    int k = e[j];
                    if (vis[k][v[j]] == 1) continue;
                    if (v[j] == tmp[1]) continue;
                    q.offer(new int[]{k, v[j]});
                    vis[k][v[j]] = 1;
                }
            }
            step++;
        }
        return rst;
    }

    private void add(int a, int b, int c) {
        e[idx] = b;
        ne[idx] = h[a];
        v[idx] = c;
        h[a] = idx++;
    }
}