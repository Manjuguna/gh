cns1=int(input())
lit1=list(map(int,input().split()))
att=[1]*cns1
for daa in range(cns1):
    if(daa==0):
        if(lit1[daa]>li1[daa+1]):
            att[daa]=att[daa]+att[daa+1]
    elif(daa>0):
        if(lit1[daa]>lit1[daa-1]):
            att[daa]=att[daa]+att[daa-1]
print(sum(att))
