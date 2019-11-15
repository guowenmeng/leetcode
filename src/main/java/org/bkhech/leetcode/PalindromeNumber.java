package org.bkhech.leetcode;

/**
 * @author guowm
 * @date 2019/11/14
 * @description 回文数
 *
 * 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
 *
 * 示例 1:
 *
 * 输入: 121
 * 输出: true
 * 示例 2:
 *
 * 输入: -121
 * 输出: false
 * 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
 * 示例 3:
 *
 * 输入: 10
 * 输出: false
 * 解释: 从右向左读, 为 01 。因此它不是一个回文数。
 * 进阶:
 *
 * 你能不将整数转为字符串来解决这个问题吗？
 *
 * 注：反转时整数溢出问题
 *
 * 来源：力扣（LeetCode）
 * 链接：https://leetcode-cn.com/problems/palindrome-number
 * 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 */
public class PalindromeNumber {

    public static void main(String[] args) {
        int x = -2332;
        System.out.println("isPalindrome(x) = " + isPalindrome_V2(x));
    }

    public static boolean isPalindrome(int x) {
        if (x < 0) return false;

        char[] chars = String.valueOf(x).toCharArray();
        if (chars.length == 1) return true;

        boolean isOdd;
        isOdd = chars.length % 2 != 0 ? true : false;
        int halfLen = chars.length / 2;

        int tempCursor = 0;
        if (isOdd) {
            tempCursor = 1;
        }

        for (int i = halfLen - 1; i >= 0; i--) {
            if (chars[i] != chars[halfLen + tempCursor]) {
                return false;
            }
            tempCursor++;
        }
        return true;
    }

    public static boolean isPalindrome_V2(int x) {
        if (x < 0) return false;
        int t = x, ret = 0, max = 0x7fffffff;
        long temp = 0;
        while (x > 0) {
            temp = temp*10 + x%10;
            x = x/10;
        }

        //如果是回文数，一定不会溢出
//        if (temp > max) {
//            return false;
//        }

        return t == temp;
    }

}
