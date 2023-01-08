class Solution {
public:
    /**
     * RUNTIME: 89 ms (83.45%)
     * MEMORY: 69.5 MB (55.78%)
    */
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int total{0}, tank{0}, start{0};
        for (int i=0; i < gas.size(); ++i){
            tank = tank + gas[i] - cost[i];
            if (tank < 0) {
                start = i + 1;
                total += tank;
                tank = 0;
            }
        }
        return total + tank < 0 ? -1 : start;
    }
};
