class Solution {
public:
    /**
     * RUNTIME: 259 ms (35.90%)
     * MEMORY: 45.9 MB (5.25%)
    */
    vector<string> findRestaurant(vector<string>& list1, vector<string>& list2) {
        int least = list1.size() + list2.size();
        unordered_map<string, int> list_dict1, list_dict2;
        unordered_map<int, vector<string>> least_dict;
        if (list1.size() > list2.size()) {
            vector<string> tmp;
            tmp = list1;
            list1 = list2;
            list2 = tmp;
        }
        for (int i=0; i < list2.size(); i++) {
            list_dict2[list2[i]] = i;
        }
        for (int i=0; i < list1.size(); i++) {
            if (list_dict2.find(list1[i]) != list_dict2.end()) {
                list_dict1[list1[i]] = i;
            }
        }
        for (auto i : list_dict1) {
            string str = i.first;
            if (list_dict2.find(str) != list_dict2.end()) {
                int min_sum = list_dict1[str] + list_dict2[str];
                if (least > min_sum) {
                    least_dict.clear();
                    vector<string> tmp;
                    tmp.push_back(str);
                    least_dict[min_sum] = tmp;
                    least = min_sum;
                }
                else if (least == min_sum) {
                    least_dict[min_sum].push_back(str);
                }
            }
        }
        return least_dict[least];
    }
};
