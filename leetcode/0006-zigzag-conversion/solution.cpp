class Solution {
public:
    /**
     * RUNTIME: 17 ms (58.81%)
     * MEMORY: 14.9 MB (22.45%)
    */
    string convert(string s, int numRows) {
        if (numRows == 1) { return s; }
        vector<string> each;
        for (size_t i=0; i<numRows; i++) {
            each.push_back("");
        }
        int n = (numRows - 1) * 2;
        for (size_t i=0; i<s.size(); i++) {
            int index = i % n;
            if (index >= numRows) {
                each[2 * (numRows - 1) - index] += s[i];
            }
            else {
                each[index] += s[i];
            }
        }
        string answer = "";
        for (string& str : each) {
            answer += str;
        }
        return answer;
    }
};
