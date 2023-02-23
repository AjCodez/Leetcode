class Solution {
    public String largestWordCount(String[] messages, String[] senders) {
        HashMap<String, Integer> hm = new HashMap<>();
        int m = 0;
        for(int i = 0 ;i<messages.length;i++){
            hm.put(senders[i],hm.getOrDefault(senders[i],0)+messages[i].split(" ").length);
            m = Math.max(m, hm.get(senders[i]));
        }
        ArrayList<String> ar = new ArrayList<>();
        for(String s : hm.keySet()){
            if(hm.get(s)==m) ar.add(s);
        }
        Collections.sort(ar);
        return ar.get(ar.size()-1); 
    }
}