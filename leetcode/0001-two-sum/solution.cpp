class Solution {
public:
    /**
     * RUNTIME: 21 ms (77.4%)
     * MEMORY: 11.8 MB (12.93%)
    */
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, vector<int>> hashmap;
        vector<int> result;
        for (int i=0; i<nums.size(); i++) {
            if (hashmap.find(nums[i]) == hashmap.end()) {
                hashmap[nums[i]] = vector<int>();
            }
            hashmap[nums[i]].push_back(i);
            int find = target - nums[i];
            if (hashmap.count(find) > 0) {
                if (nums[i] == find && hashmap[find].size() > 1) {
                    result.push_back(hashmap[find][0]);
                    result.push_back(hashmap[find][1]);
                    break;
                }
                else if (nums[i] != find) {
                    result.push_back(hashmap[find][0]);
                    result.push_back(hashmap[nums[i]][0]);
                    break;
                }
            }
        }
        return result;
    }
};
