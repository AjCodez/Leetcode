class Solution {
    public String reverseWords(String s) {
        char[] str = s.toCharArray();
        char[] out = new char[s.length()];
        int size = 0;
        int r = str.length;
        for (int l = r - 1; l >= 0; l--) {
            if (str[l] == ' ') {
                for (int i = l + 1; i < r; i++) {
                    out[size++] = str[i];
                }
                if (l + 1 < r) out[size++] = ' ';
                r = l;
            }
        }
        for (int i = 0; i < r; i++) {
            out[size++] = str[i];
        }
        if (size > 0 && out[size - 1] == ' ') size--;
        return String.valueOf(out, 0, size);
    }
}