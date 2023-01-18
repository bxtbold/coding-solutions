class Solution {
public:
    /**
     * RUNTIME: 10 ms (97.88%)
     * MEMORY: 17.1 MB (45.20%)
    */
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> answer;
        for(auto &&i : intervals){
            if(i[1] < newInterval[0]) {
                answer.push_back(i);
            }
            else if(newInterval[1] < i[0]){
                answer.push_back(newInterval);
                newInterval = i;
            }
            else{
                newInterval[0]=min(newInterval[0],i[0]);
                newInterval[1]=max(newInterval[1],i[1]);
            }
        }
        answer.push_back(newInterval);
        return answer;
    }
};
