import numpy as np
import matplotlib.pyplot as plt


xs1=[]
with open("foldseek_original.rocx", 'r') as fs:
    for line in fs:
        l=line.split("\t")
        #print(l)
        xs1.append(l[3])
xs1=xs1[1:]
xs1.sort()

xs2=[]
with open("foldseek.rocx", 'r') as fs:
    for line in fs:
        l=line.split("\t")
        #print(l)
        xs2.append(l[3])
xs2=xs2[1:]
xs2.sort()

xs3=[]
with open("foldseek_pt5_pdb.rocx", 'r') as fs:
    for line in fs:
        l=line.split("\t")
        #print(l)
        xs3.append(l[3])
xs3=xs3[1:]
xs3.sort()

xs4=[]
with open("foldseek_pdb_pt5.rocx", 'r') as fs:
    for line in fs:
        l=line.split("\t")
        #print(l)
        xs4.append(l[3])
xs4=xs4[1:]
xs4.sort()

ys=[]
x1=[]
x2=[]
x3=[]
x4=[]
cnt1=0
cnt2=0
cnt3=0
cnt4=0
for i in range(100):
    curr=0.01*i
    ys.append(curr)
    while(float(xs1[cnt1])<curr and cnt1<len(xs1)-1):
        cnt1+=1
    while(float(xs2[cnt2])<curr and cnt2<len(xs2)-1):
        cnt2+=1
    while(float(xs3[cnt3])<curr and cnt3<len(xs3)-1):
        cnt3+=1
    while(float(xs4[cnt4])<curr and cnt4<len(xs4)-1):
        cnt4+=1
    x1.append(1-(cnt1/len(xs1)))
    x2.append(1-(cnt2/len(xs2)))
    x3.append(1-(cnt3/len(xs3)))
    x4.append(1-(cnt4/len(xs4)))
ys.reverse()
x1.reverse()
x2.reverse()
x3.reverse()
x4.reverse()

import seaborn as sns
sns.set_style('whitegrid')

fig,ax=plt.subplots()
ax.plot(x1[:-1],ys[:-1], color='black')
ax.plot(x2[:-1],ys[:-1], color='red')
ax.plot(x3[:-1],ys[:-1])
ax.plot(x4[:-1],ys[:-1])

ax.plot(x1[:-1][::10],ys[:-1][::10], label = "PDB query, PDB target (original Foldseek)", marker='o', linestyle='None', color='black', markersize=5, markerfacecolor='none')
ax.plot(x2[:-1][::10],ys[:-1][::10], label = "ProstT5 query, ProstT5 target", marker='v', linestyle='None', color='red', markersize=5, markerfacecolor='none')
ax.plot(x3[:-1][::10],ys[:-1][::10], label = "ProstT5 query, PDB target", marker='D', linestyle='None', color='steelblue', markersize=5, markerfacecolor='none')
ax.plot(x4[:-1][::10],ys[:-1][::10], label = "PDB query, ProstT5 target", marker='s', linestyle='None', color='darkorange', markersize=5, markerfacecolor='none')
ax.set_ylabel("ROC1")
ax.set_xlabel("Query coverage")
ax.legend(fontsize='small')
ax.set_title("Superfamily")
fig.savefig("QueryTarget_superfamily.pdf", bbox_inches='tight', dpi=500, pad_inches=0.3)        

fig, axs = plt.subplots(1, 3)