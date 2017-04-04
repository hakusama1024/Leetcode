def firstindexofanagram(s, t):
    if len(s) == 0 and len(t) == 0 : return 0
    if len(s) == 0: return -1
    if len(t) == 0 : return 0 
    if len(s) < len(t) : return -1
    dic = {'a':2, 'b':3, 'c':5, 'd':7, 'e':11, 'f':13, 'g':17, 'h':19, 'i':23, 'j':29, 'k':31, 'l':37, 'm':41, 'n':43, 'o':47, 'p':53, 'q':59, 'r':61, 's':67, 't':71, 'u':73, 'v':79, 'w':83, 'x':89, 'y':97, 'z':101}

    sut = 1
    win = 1

    for i in range(len(t)):
        sut *= dic[t[i]]

    for i in range(len(t)):
        win *= dic[s[i]]

    for i in range(len(t), len(s)):
        if sut == win : return i-3
        win *= dic[s[i]]
        win /= dic[s[i-3]]



s = "teacher"
t = "ech"
print firstindexofanagram(s, t)



