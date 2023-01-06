class Solution {
public:
    /**
     * RUNTIME: 393 ms (37.65%)
     * MEMORY: 76.4 MB (76.68%)
    */
    int maxIceCream(vector<int>& costs, int coins) {
        sort(begin(costs), end(costs));
        for (int i = 0; i < costs.size(); ++i) {
            if (coins < costs[i]) { return i; }
            coins -= costs[i];
        }
        return costs.size();
    }
};