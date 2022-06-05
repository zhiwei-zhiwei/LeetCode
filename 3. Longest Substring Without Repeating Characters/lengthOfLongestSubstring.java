class Solution {
    public int lengthOfLongestSubstring(String s) {
        int len = 0; // use to record the max length
        int point = 0; // use to update the point of character that is same
        HashMap<Character, Integer> map = new HashMap<>(); // hashmap here could help to update the point of new character and reassign the point to count the new character that is same with porevisou one
        for(int i = 0; i < s.length(); i++){
            if(map.containsKey(s.charAt(i))){
                point = Math.max(point, map.get(s.charAt(i)) + 1);
                //  if one letter is same with the one in the map, update the point 
                // a b c a e r t y u i  like the second "a" and the map only have add to <c, 2>
                // 0 1 2 3 4 5 6 7 8 9  in order to update the point, we should add 1 position
                // when the algorifght enter this if statement, which means there is a repeated char
                // in this example, update the pointer from 0 to 1, b/c char 'a' is realpeted, so the
                // start pointer should be from index 1 which is b which ensure there is no duplicated ones
                // and also ensure that the algo can count the longest substring
            }
            map.put(s.charAt(i),i); // no matter what is happened, we  alwasy add new element to the map
            len = Math.max(len,i - point + 1); // then alwasy check the max length and do caulation between the max position and the point we assigned before
        }
        return len;
    }
}