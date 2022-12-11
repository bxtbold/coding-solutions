class Solution {
public:
    /**
     * RUNTIME: 6 ms (85.10%)
     * MEMORY: 10.8 MB (21.13%)
    */
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> hashmap1, hashmap2;
        vector<int> intersected;

        if (nums1.size() > nums2.size()) {
            vector<int> tmp = nums2;
            nums2 = nums1;
            nums1 = tmp;
        }
        for (int i : nums1) {
            ++hashmap1[i];
        }
        for (int i : nums2) {
            if (hashmap1.find(i) != hashmap1.end()) {
                ++hashmap2[i];
            }
        }

        for (auto i : hashmap2) {
            int tmp = i.first;
            int repeat = hashmap1[tmp] > hashmap2[tmp] ? hashmap2[tmp] : hashmap1[tmp]; 
            for (int j = 0; j < repeat; j++) {
                intersected.push_back(i.first);
            }
        }
        return intersected;
    }
};
