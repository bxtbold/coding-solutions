class Solution {
public:
    /**
     * RUNTIME: 39 ms (91.77%)
     * MEMORY: 20.8 MB (40.23%)
    */
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map <string, vector<string>> hashmap;
        for (string i : strs) {
            string tmp = i;
            sort(tmp.begin(), tmp.end());
            if (hashmap.find(tmp) == hashmap.end()) {
                hashmap[tmp] = vector<string>();
            }
            hashmap[tmp].push_back(i);
        }
        vector<vector<string>> result;
        for (auto i : hashmap) {
            result.push_back(i.second);
        }
        return result;
    }
};
