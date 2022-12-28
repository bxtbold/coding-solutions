class Solution {
public:
    /**
     * RUNTIME: 210 ms (81.98%)
     * MEMORY: 84.7 MB (79.56%)
    */
    int maximumBags(vector<int>& capacity, vector<int>& rocks, int additionalRocks) {
        for (int i = 0; i < capacity.size(); i++) {
            capacity[i] -= rocks[i];
        }
        sort(capacity.begin(), capacity.end());
        int cnt = 0;
        int result = count(capacity.begin(), capacity.end(), 0);
        for (int i = result; i < capacity.size(); i++) {
            cnt += capacity[i];
            if (cnt <= additionalRocks) { result += 1; }
            else { break; }
        }
        return result;
    }
};
