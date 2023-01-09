class Solution {
public:
    /**
     * RUNTIME: 55 ms (71.19%)
     * MEMORY: 18.2 MB (32.47%)
    */
    int maxPoints(vector<vector<int>>& points) {
        int ans = 0;
        float slope;
        for (int i=0; i<points.size(); ++i) {
            unordered_map<float, int> hashmap;
            int localMax = 0;
            for (int j=0; j<i; ++j) {
                slope = getSlope(points[i], points[j]);
                hashmap[slope]++;
                ans = max(ans, hashmap[slope]);
            }
        }
        return ans + 1;
    }

    float getSlope(vector<int> p1, vector<int> p2) {
        if (p1[0] - p2[0] == 0) {
            return std::numeric_limits<float>::max();
        }
        return static_cast<float>(p1[1] - p2[1]) / static_cast<float>(p1[0] - p2[0]);
    }
};
