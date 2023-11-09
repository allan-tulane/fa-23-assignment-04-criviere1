import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T), MED(S[1:], T[1:])))


def fast_MED(S, T, MED={}):
    # fill MED[i][j] with 0s
    MED = [[0 for i in range(len(T)+1)] for j in range(len(S)+1)]
    
    for i in range(len(S) + 1):
        for j in range(len(T) + 1):
            if i == 0: #base case
                MED [i][j] = j
            elif j == 0: #base ccase
                MED[i][j] = i 
            
            elif S[i-1] == T[j-1]: # if first letters are the same
                MED[i][j] = MED[i-1][j-1]
            else:
                MED[i][j] = 1 + min(MED[i][j-1], MED[i-1][j], MED[i-1][j-1])
    
    return MED


def fast_align_MED(S, T, MED={}):
    # TODO - keep track of alignment
    MED = fast_MED(S,T)
    s = []
    t = []

    i = len(S)
    j = len(T)

    while (i!=0 and j!=0):
        insert = MED[i][j-1]
        remove = MED[i-1][j]
        sub = MED[i-1][j-1]
        m = min(insert,remove,sub)

        if (sub == m):
            s = [S[i-1]] + s
            t = [T[j-1]] + t
            i -= 1
            j -= 1

        elif (insert == m):
            s = ['-'] + s
            t = [T[j-1]] + t
            j -= 1

        elif (remove == m):
            s = [S[i-1]] + s
            t = ['-'] + t
            i -= 1

    s_str = "".join(s)
    t_str = "".join(t)

    return s_str, t_str

def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T)[-1][-1] == MED(S, T)
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])
