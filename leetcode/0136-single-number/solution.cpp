class Solution {
public:
    /**
     * RUNTIME: 71 ms (16.39%)
     * MEMORY: 20.1 MB (20.29%)
    */

    int singleNumber(vector<int>& nums) {
        unordered_map<int, int> hashset;
        for (int i : nums) {
            ++hashset[i];
        }
        for (auto each : hashset) {
            if (each.second == 1) {
                return each.first;
            }
        }
        return -1;
    }
};
