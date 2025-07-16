// Last updated: 7/16/2025, 9:42:15 AM
class Solution {
    public int[] runningSum(int[] nums) {
        for (int i = 1; i < nums.length; i++){
            nums[i]= nums[i-1]+nums[i];
        }
        return nums;
    }
}