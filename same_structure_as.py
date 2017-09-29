def same_structure_as(original,other):

    object1=str(original)
    object2=str(other)
    structA="".join(map(str,object1))
    structB="".join(map(str,object2))

    if(len(structA)!=len(structB)):
        return False

    compare_structA=""
    compare_structB=""
    solution=True
    digitA=0
    digitB=0

    for i in structA:
        if(i=="[" or i=="]"):
            compare_structA+="X"

        elif(i==" "):
            continue

        elif(i.isdigit()==True):
            compare_structA+="N"
            digitA=i


        elif(i.isdigit()!=True):
            compare_structA+=i

    for i in structB:
        if(i=="[" or i=="]"):
            compare_structB+="X"

        elif(i==" "):
            continue

        elif(i.isdigit()==True):
            compare_structB+="N"
            digitB=i

        elif(i.isdigit()!=True):
            compare_structB+=i

    sizeStructA=len(compare_structA)
    
    for i in range(sizeStructA):
        if(compare_structA[i]!=compare_structB[i]):
            solution=False
            break

    if(digitA==digitB):
        for i in range(sizeStructA):
           if(compare_structA[i]!=compare_structB[sizeStructA-i-1]):
               return False
               
        solution=True
    return solution