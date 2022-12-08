class Solution {
public:
    /**
     * RUNTIME: 7 ms (85.48%)
     * MEMORY: 17.79 MB (10.8%)
    */

    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> hashset1;
        unordered_map<int, int> hashset2;
        vector<int> unique;
        for (int i : nums1) { hashset1[i] = 1; }
        for (int i : nums2) { hashset2[i] = 1; }
        for (auto i : hashset1) {
            if (hashset2.find(i.first) != hashset2.end() ) {
                unique.push_back(i.first);
            }
        }
        return unique;
    }
};