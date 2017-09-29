def longest_consec(strarr, k):
    if (strarr==[] or k==0 or k<0 or k>len(strarr)):
        return ""
    characters=[]
    solution=[]
    index=0
    longest_string=list(0 for i in range(len(strarr)))

    for i in strarr:
        characters.append(len(i))

    while(index<=len(longest_string)-k):
        for j in range(index,index+k):
            longest_string[index]+=characters[j]
        index+=1

    max_value=longest_string.index(max(longest_string))


    for i in range(max_value,max_value+k):
        solution.append(strarr[i])
    return "".join(solution)
