class Solution {
public:
    /**
     * RUNTIME: 0 ms (100%)
     * MEMORY: 6.3 MB (49.75%)
    */
    int numJewelsInStones(string jewels, string stones) {
        unordered_map <char, int> hashmap;
        int cnt = 0;
        for (char i : stones) {
            if (jewels.find(i) != string::npos) {
                ++hashmap[i];
            }
        }
        for (char i : jewels) {
            if (hashmap.find(i) != hashmap.end()) {
                cnt += hashmap[i];
            }
        }
        return cnt;
    }
};
