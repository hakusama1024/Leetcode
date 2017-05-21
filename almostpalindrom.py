def almostPal(s):
    if not s or len(s) == 1:
        return True
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return perfectPal(s[left+1:right+1]) or perfectPal(s[left:right])

s = "aaabaaaaaaa"
print almostPal(s)
