class RandomizedSet {
public:
    /**
     * RUNTIME: 322 ms (75.23%)
     * MEMORY: 97 MB (80.67%)
    */
    RandomizedSet() {
    }

    bool insert(int val) {
        if (hashset.find(val) == hashset.end()) {
            hashset[val] = 0;
            return true;
        }
        else {
            return false;
        }
    }

    bool remove(int val) {
        if (hashset.find(val) != hashset.end()) {
            hashset.erase(val);
            return true;
        }
        else {
            return false;
        }
    }

    int getRandom() {
        int random = rand() % hashset.size() + 1;
        int result, cnt = 0;
        for (auto i : hashset) {
            if (++cnt == random) {
                result = i.first;
                break;
            }
        }
        return result;
    }
private:
    unordered_map <int, int> hashset;
};