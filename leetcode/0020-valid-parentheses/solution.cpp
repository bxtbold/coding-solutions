class Solution {
public:
    /**
     * RUNTIME: 0 ms (100%)
     * MEMORY: 6.4 MB (52.7%)
    */
    bool isValid(string s) {
        if (s.length() % 2 == 1) {
            return false;
        }
        stack<char> st;
        for(char c : s){
            if(c == '('|| c == '{' || c == '[') {
                st.push(c);
            }
            else {
                if(st.empty()) return false;
                if(c == ')' && st.top() != '(') return false;
                if(c == '}' && st.top() != '{') return false;
                if(c == ']' && st.top() != '[') return false;
                st.pop();
            }
        }
        return st.empty();
    }
};
