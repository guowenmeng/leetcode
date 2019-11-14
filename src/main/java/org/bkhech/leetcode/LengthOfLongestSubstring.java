package org.bkhech.leetcode;

import java.util.*;

/**
 * @author guowm
 * @date 2019/11/8
 * @description 无重复字符的最长子串
 */
public class LengthOfLongestSubstring {

    public static void main(String[] args) {
        int len = lengthOfLongestSubstring("asd2ui7dfjk");
        System.out.println("len = " + len);
    }

    public static int lengthOfLongestSubstring(String s) {
        if (s == null) {
            return 0;
        }

        char[] chars = s.toCharArray();
        int[] nums = new int[]{0};
        Map<Character, Integer> containers = new HashMap<>();
        loop(0, chars, containers, nums);
        return nums[0];

    }

    private static void loop(int index, char[] chars, Map<Character, Integer> containers, int[] nums) {
        if (chars.length - index < nums[0]) {
            return;
        }

        containers.clear();
        int repeatIndex = 0;

        for (int i = index; i < chars.length; i++) {
            if (containers.containsKey(chars[i])) {
                if (nums[0] < containers.size()) {
                    nums[0] = containers.size();
                }
                repeatIndex = containers.get(chars[i]);
                break;
            }
            containers.put(chars[i], i);
            if (i == chars.length - 1) {
                nums[0] = containers.size();
                return;
            }
        }

        loop(repeatIndex+1, chars, containers, nums);
    }

}
