class Solution {
public:
    /**
     * RUNTIME: 301 ms (75.35%)
     * MEMORY: 97.3 MB (9.17%)
    */
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        if (nums.empty()) { return false; }
        unordered_map <int, vector<int>> hashmap;
        for (int i = 0; i < nums.size(); i++) {
            if (hashmap.find(nums[i]) == hashmap.end()) {
                hashmap[nums[i]] = vector<int>();
            }
            hashmap[nums[i]].push_back(i);
            if (hashmap[nums[i]].size() > 1) {
                if (hashmap[nums[i]][1] - hashmap[nums[i]][0] <= k) {
                    return true;
                }
                hashmap[nums[i]].erase(hashmap[nums[i]].begin());
            }
        }
        return false;
    }
};
