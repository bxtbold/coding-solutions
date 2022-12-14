class Solution {
public:
    /**
     * RUNTIME: 13 ms (96.78%)
     * MEMORY: 13.9 MB (19.15%)
    */
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map <int, int> mp;
        map <int, vector<int>> repetance;
        vector <int> result, keys;
        for (int i : nums) {
            ++mp[i];
        }
        for (auto i : mp) {
            if (repetance.find(i.second) == repetance.end()) {
                repetance[i.second] = vector<int>();
                keys.push_back(i.second);
            }
            repetance[i.second].push_back(i.first);
        }
        sort(keys.begin(), keys.end(), std::greater<int>());
        for (int i : keys) {
            for (int j : repetance[i]) {
                result.push_back(j);
            }
            if (result.size() >= k) {
                break;
            }
        }
        sort(result.begin(), result.end());
        return result;
    }
};
