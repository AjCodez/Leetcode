class Solution {
    public int[][] diagonalSort(int[][] mat) {
        int l = mat.length - 1;
        int r = 0;
        int tl = 0;
        int tr = mat.length - 1;
        while (l!=0 || tl!=mat[0].length-1 || r!=mat[0].length-1){
            ArrayList<Integer> list = new ArrayList<>();
            int t1=l;
            int t2=tl;
            while (t1<=tr+1 && t2<=r){
                list.add(mat[t1][t2]);
                t1++;
                t2++;
            }
            int t=0;
            t1=l;
            t2=tl;
            Collections.sort(list);
            while (t1<=tr+1 && t2<=r){
                mat[t1][t2]=list.get(t);
                t++;
                t1++;
                t2++;
            }
            if (l!=0) l--;
            else tl++;
            if (r!=mat[0].length-1) r++;
            else tr--;
        }
        return mat;
    }
}