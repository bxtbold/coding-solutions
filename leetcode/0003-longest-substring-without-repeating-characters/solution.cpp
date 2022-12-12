class Solution {
public:
    /**
     * RUNTIME: 11 ms (90.89%)
     * MEMORY: 8.3 MB (61.28%)
    */
    int lengthOfLongestSubstring(string s) {
        unordered_map <char, int> mp;
        int ans = 0;
        int i = 0;
        for (int j=0; j < s.size(); j++) {
            if (mp.find(s[j]) != mp.end()) {
                i = max(i, mp[s[j]]);
            }
            ans = max(ans, j - i + 1);
            mp[s[j]] = j + 1;
        }
        return ans;
    }
};
