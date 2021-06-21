using namespace std;
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> counter;
        int i;
        int n = nums.size();
        
        while (i < n) {
            cout << i << counter[i] << endl;
            if (counter.find(nums[i]) == counter.end()) {
                counter[nums[i]] = 1;
            }
            else {
                cout << 5 << endl;
                if (counter[nums[i]] > n/2) {
                    
                    return nums[i];
                }
                else {
                    counter[nums[i]] += 1;
                }
            }
            i += 1;
        }
        return 0;
    }
};

vector<int> x = {5,3,5,5,5};
majorityElement(vector<int>& x);