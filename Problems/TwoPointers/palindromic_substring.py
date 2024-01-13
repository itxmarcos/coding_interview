def subcadenas(s):
    n = len(s)
    print(f"n: {n}")
    for length in range(1, n+1):
        print(f"length: {length}")
        for i in range(n - length + 1):
            print(f"i: {i}")
            yield s[i:i+length]

class Solution:
    def countSubstrings(self, s: str) -> int:
        counter_palindromic = 0
        for subcadena in subcadenas(s):
            left, right = 0, len(subcadena) - 1
            is_palindromic = True
            while left < right:
                if subcadena[left] != subcadena[right]:
                    is_palindromic = False
                    break
                left += 1
                right -= 1

            if is_palindromic:
                counter_palindromic += 1

        return counter_palindromic

cadena = "abcd"
sol = Solution()
print(sol.countSubstrings(cadena))
