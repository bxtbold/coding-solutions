class Solution {
public:
    /**
     * RUNTIME: 171 ms (5.1%)
     * MEMORY: 10.8 MB (46.8%)
    */
    int firstUniqChar(string s) {
        unordered_map<char, int> hashmap;
        for (char each : s) {
            if (hashmap.find(each) != hashmap.end()) {
                hashmap[each] = hashmap[each] + 1;
            }
            else {
                hashmap[each] = 1;
            }
        }
        for (int i = 0; i < s.size(); i++) {
            if (hashmap[s[i]] == 1) {
                return i;
            }
        }
        return -1;
    }
};
