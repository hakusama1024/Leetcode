def LicenseKeyFormatting(s, k):
    size = len(s)
    if size == 0 : return s

    res = ""
    count = 0
    for i in range(size-1, -1, -1):
        if s[i] != '-':
            res = s[i] + res
            count += 1
        if count == k:
            res = '-' + res
            count = 0

    print res.upper()

s = "2-4A0r7-4k"
k = 3


LicenseKeyFormatting(s, k)



