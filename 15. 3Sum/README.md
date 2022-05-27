# 15. 3Sum

[LeetCode](https://leetcode.cn/problems/3sum)

**This question cares about two pointers, the the pointers to find the solution. Be careful when you try to move the pointer\
Remember to deal with the situdation, [0,0,0,0,0], to prevent the same solution**

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.\
Notice that the solution set must not contain duplicate triplets.

Example 1:\
Input: nums = [-1,0,1,2,-1,-4]\
Output: [[-1,-1,2],[-1,0,1]]

Example 2:\
Input: nums = []\
Output: []

Example 3:\
Input: nums = [0]\
Output: []

Constraints:\
0 <= nums.length <= 3000\
-105 <= nums[i] <= 105

