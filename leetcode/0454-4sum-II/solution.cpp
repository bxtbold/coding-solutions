class Solution {
public:
    /**
     * RUNTIME: 276 ms (90.38%)
     * MEMORY: 27.5 MB (15.64%)
    */
    int fourSumCount(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3, vector<int>& nums4) {
        unordered_map <int, int> sum1, sum2;
        int total = 0;
        for (int i=0; i < nums1.size(); i++ ) {
            for (int j=0; j < nums1.size(); j++ ) {
                int tmp1 = nums1[i] + nums2[j];
                int tmp2 = nums3[i] + nums4[j];
                ++sum1[tmp1];
                ++sum2[tmp2];
            }
        }
        for (auto i : sum1) {
            if (sum2.find(-i.first) != sum2.end()) {
                total += i.second * sum2[-i.first];
            }
        }
        return total;
    }
};
