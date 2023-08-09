'''
Write a function solution that, given two integers A and B, returns a string containing exactly A letters 'a' and exactly B letters 'b' with no three consecutive letters being the same (in other words, neither "aaa" nor "bbb" may occur in the returned string).

Examples:

1. Given A = 5 and B = 3, your function may return "aabaabab". Note that "abaabbaa" would also be a correct answer. Your function may return any correct answer.

2. Given A = 3 and B = 3, your function should return "ababab", "aababb", "abaabb" or any of several other strings.

3. Given A = 1 and B = 4, your function should return "bbabb", which is the only correct answer in this case.

Assume that:

A and B are integers within the range [0..100];
at least one solution exists for the given A and B.
In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
'''

def solution(A, B):
    # Implement your solution here
    res = []
    if A > B:
        res = ["a", "a"]
        A -= 2
    else:
        res = ["b", "b"]
        B -= 2

    while A > 0 and B > 0:
        if A/B >= 2:
            if res[-1] != "a":
                res += ["a", "a"]
            else:
                res += ["b", "a", "a"]
                B -= 1

            A -= 2
            continue
        elif B/A >= 2:
            if res[-1] != "b":
                res += ["b", "b"]
            else:
                res += ["a", "b", "b"]
                A -= 1
            B -= 2
            continue
        else:
            if res[-1] == "a":
                res += ["b", "a"]
            else:
                res += ["a", "b"]
            A-= 1
            B-= 1

    if A > 0:
        return ''.join(res + ['a']*A)
    if B > 0:
        return ''.join(res + ['b']*B)
    return ''.join(res)


if __name__ == "__main__":
    A, B = 3, 3
    print(f"solution of {A},{B} = {solution(A, B)}")
    
    A, B = 2, 0
    print(f"solution of {A},{B} = {solution(A, B)}")

    A, B = 3, 5
    print(f"solution of {A},{B} = {solution(A, B)}")

    A, B = 3, 8
    print(f"solution of {A},{B} = {solution(A, B)}")
    
    A, B = 1, 4
    print(f"solution of {A},{B} = {solution(A, B)}")