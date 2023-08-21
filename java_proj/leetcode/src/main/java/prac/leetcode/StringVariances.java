package prac.leetcode;
/*
'A' -> "1"
'B' -> "2"
…
'J' -> “10”
'K' -> “11”
'Z' -> "26"

Example:
# 1      ->    1 (A)
# 12    ->    2 (AB,     L)
# 123  ->    3 (ABC , LC, AW )

input: 0-9 string
output: a number
 */
public class StringVariances {
    static public int parseNum(String input) {
        int n = input.length();
        if (n <= 1) {
            if (input.equals("0")) {
                return 0;
            }
            return 1;
        }
        int pos_num = 0;
        boolean findInvalid = false;
        for (int i=1; i < n+1; ++i) {
            int ind = Integer.parseInt(input.substring(0, i));
            if (ind > 0 && ind <=26) {
                int r = parseNum(input.substring(i, n));
                pos_num += r;
            } else {
                findInvalid = true;
                break;
            }
        }
        if (findInvalid && pos_num == 0) {
            return 0;
        }

        return pos_num;
    }
}
