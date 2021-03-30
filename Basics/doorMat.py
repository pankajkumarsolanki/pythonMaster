n,m = map(int, input().split())


L=[]
for i in range(1,n,2):
    L.append((".|."*i).center(m,"-"))
print("\n".join(L + ["Welcome".center(m,"-")] + L[::-1]))

