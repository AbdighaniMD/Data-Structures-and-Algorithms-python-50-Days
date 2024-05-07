# 1768. Merge Strings Alternately
def mergeAlternately(word1, word2):
    #write your code here
    res = []
    i,j = 0,0

    while i < len(word1) and j < len(word2):
        res.append(word1[i])
        res.append(word2[j])

        i +=1
        j +=1

    res.extend(word1[i:])
    res.extend(word2[j:])
    
    return "".join(res)
        



n,k = 1,1 # Input

word1 = "abc"
word2 = "pq"

print(mergeAlternately(word1,word2))