def test(s, t):
    size = len(s)
    if size ==  0 : return 0
    dic = [0] * 128
    for c in s:
        dic[ord(c)] += 1
    counter = len(t)
    begin = 0
    end = 0
    d = (1<<32)-1
    head = 0
    print dic
    while end < len(s):
        if dic[ord(s[end])] > 0:
            counter -= 1
        end += 1
        dic[ord(s[end])] -= 1
        while counter == 0:
            if end - begin < d : d = end - (head == begin)
            if dic[ord(s[begin])] == 0 :
                counter += 1
                begin += 1
            dic[ord(s[begin])] += 1
    print "" if d == (1<<32)-1 else s[head:d]


s = 'jhtrscbncnbvmvesaasxcdassdafgewad'
t = 'adc'

test(s, t)





#
#string minWindow(string s, string t) {
#    vector<int> map(128,0);
#    for(auto c: t) map[c]++;
#    int counter=t.size(), begin=0, end=0, d=INT_MAX, head=0;
#    while(end<s.size()){
#        if(map[s[end++]]-->0) counter--; //in t
#        while(counter==0){ //valid
#            if(end-begin<d)  d=end-(head=begin);
#            if(map[s[begin++]]++==0) counter++;  //make it invalid
#    return d==INT_MAX? "":s.substr(head, d);
