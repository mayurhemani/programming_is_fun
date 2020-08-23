def isPalindrome(s):
    i = 0
    j = len(s) - 1
    while i <= j:
        if s[i] == " ":
            i = i + 1
            continue
        if s[j] == " ":
            j = j - 1
            continue
        if s[i] != s[j]:
            return False
        i = i + 1
        j = j - 1
    return True

print(isPalindrome("n   it  in "))
print(isPalindrome("niti  ni   "))

