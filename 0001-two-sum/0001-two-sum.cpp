#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;  // Map to store each number and its index
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (map.find(complement) != map.end()) {
                return {map[complement], i};  // Return the indices if complement is found
            }
            map[nums[i]] = i;  // Store the current number's index in the map
        }
        return {};  // Return an empty vector if no solution is found (not needed due to constraints)
    }
};