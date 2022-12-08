class Solution {
public:
    /**
     * RUNTIME: 90 ms (97.85%)
     * MEMORY: 51.3 MB (70.17%)
    */

    bool containsDuplicate(vector<int>& nums) {
        if (nums.empty()) { return false; }
        unordered_map<int,int> hashset;
        for (int i : nums) {
            if (++hashset[i] > 1) {
                return true;
            }
        }
        return false;
    }
};
