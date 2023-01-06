class Solution {
public:
    /**
     * RUNTIME: 223 ms (91.63%)
     * MEMORY: 103.7 MB (45.14%)
    */
    int minimumRounds(vector<int>& tasks) {
        unordered_map<int, int> hashmap;
        for (int i : tasks) {
            ++hashmap[i];
        }
        int answer = 0;
        for (auto pair : hashmap) {
            if (pair.second == 1) {
                return -1;
            }
            else if (pair.second == 2 || pair.second == 3) {
                answer++;
            }
            else if (pair.second % 3 == 0) {
                answer += pair.second / 3;
            }
            else {
                answer += pair.second / 3 + 1;
            }
        }
        return answer;
    }
};