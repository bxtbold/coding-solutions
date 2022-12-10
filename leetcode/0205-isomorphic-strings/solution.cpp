class Solution {
public:
    /**
     * RUNTIME: 6 ms (91.3%)
     * MEMORY: 7 MB (75.6%)
    */
    bool isIsomorphic(string s, string t) {
        if (s.size() != t.size()) { return false; }
        unordered_map<int, int> hashmap;
        vector<int> values;
        for (int i=0; i < s.size(); i++) {
            if (hashmap.find(s[i]) == hashmap.end()) {
                if ( std::find(values.begin(), values.end(), t[i])  != values.end() ) {
                    return false;
                }
                hashmap[s[i]] = t[i];
                values.push_back(t[i]);
            }
            else {
                if (hashmap[s[i]] != t[i]) {
                    return false;
                }
            }
        }
        return true;
    }
};
