# Expand around centre pattern.

def expand(s):
    
        if s == s[::-1]:
            return s
        else:
            max_len=1
            s_index=0
            for i in range(len(s)):
                for j in range(len(s)):
                    if i-j>=0 and i+j<len(s) :
                        if s[i-j]==s[i+j]: # odd sort
                            cur_len=2 * j  +1
                            if cur_len > max_len:
                                max_len=cur_len
                                s_index=i-j
                        else:
                            break
                for j in range(len(s)):
                    if i-j>=0 and i+j+1<len(s) : #even sort
                        if s[i-j]==s[i+1+j]:
                            cur_len=2 * j  +2
                            if cur_len > max_len:
                                max_len=cur_len
                                s_index=i-j
                        else:
                            break
                        
        return s[s_index:max_len+s_index]


print(expand(s = "abacdfgdcaba"))


        