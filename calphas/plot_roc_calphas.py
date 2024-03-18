import numpy as np
import matplotlib.pyplot as plt

xs1_family=[]
xs1_superfamily=[]
xs1_fold=[]
with open("foldseek_original.rocx", 'r') as fs:
    for line in fs:
        l=line.split("\t")
        #print(l)
        xs1_family.append(l[2])
        xs1_superfamily.append(l[3])
        xs1_fold.append(l[4])
        
# print(xs1_superfamily[:100])
# print(xs1_family[:100])
xs1_family=xs1_family[1:]
xs1_family.sort()
xs1_superfamily=xs1_superfamily[1:]
xs1_superfamily.sort()
xs1_fold=xs1_fold[1:]
xs1_fold.sort()



xs2_family=[]
xs2_superfamily=[]
xs2_fold=[]
with open("foldseek_original_ca.rocx", 'r') as fs:
    for line in fs:
        l=line.split("\t")
        #print(l)
        xs2_family.append(l[2])
        xs2_superfamily.append(l[3])
        xs2_fold.append(l[4])
xs2_family=xs2_family[1:]
xs2_family.sort()
xs2_superfamily=xs2_superfamily[1:]
xs2_superfamily.sort()
xs2_fold=xs2_fold[1:]
xs2_fold.sort()

xs3_family=[]
xs3_superfamily=[]
xs3_fold=[]
with open("foldseek.rocx", 'r') as fs:
    for line in fs:
        l=line.split("\t")
        #print(l)
        xs3_family.append(l[2])
        xs3_superfamily.append(l[3])
        xs3_fold.append(l[4])
xs3_family=xs3_family[1:]
xs3_family.sort()
xs3_superfamily=xs3_superfamily[1:]
xs3_superfamily.sort()
xs3_fold=xs3_fold[1:]
xs3_fold.sort()

xs4_family=[]
xs4_superfamily=[]
xs4_fold=[]
with open("foldseek_ca.rocx", 'r') as fs:
    for line in fs:
        l=line.split("\t")
        #print(l)
        xs4_family.append(l[2])
        xs4_superfamily.append(l[3])
        xs4_fold.append(l[4])
xs4_family=xs4_family[1:]
xs4_family.sort()
xs4_superfamily=xs4_superfamily[1:]
xs4_superfamily.sort()
xs4_fold=xs4_fold[1:]
xs4_fold.sort()

ys=[]
x1_family=[]
x1_superfamily=[]
x1_fold=[]
x2_family=[]
x2_superfamily=[]
x2_fold=[]
x3_family=[]
x3_superfamily=[]
x3_fold=[]
x4_family=[]
x4_superfamily=[]
x4_fold=[]
cnt1_family=0
cnt1_superfamily=0
cnt1_fold=0
cnt2_family=0
cnt2_superfamily=0
cnt2_fold=0
cnt3_family=0
cnt3_superfamily=0
cnt3_fold=0
cnt4_family=0
cnt4_superfamily=0
cnt4_fold=0
for i in range(100):
    curr=0.01*i
    ys.append(curr)
    while(float(xs1_family[cnt1_family])<curr and cnt1_family<len(xs1_family)-1):
        cnt1_family+=1
    while(float(xs2_family[cnt2_family])<curr and cnt2_family<len(xs2_family)-1):
        cnt2_family+=1
    while(float(xs3_family[cnt3_family])<curr and cnt3_family<len(xs3_family)-1):
        cnt3_family+=1
    while(float(xs4_family[cnt4_family])<curr and cnt4_family<len(xs4_family)-1):
        cnt4_family+=1
    x1_family.append(1-(cnt1_family/len(xs1_family)))
    x2_family.append(1-(cnt2_family/len(xs2_family)))
    x3_family.append(1-(cnt3_family/len(xs3_family)))
    x4_family.append(1-(cnt4_family/len(xs4_family)))
    while(float(xs1_superfamily[cnt1_superfamily])<curr and cnt1_superfamily<len(xs1_superfamily)-1):
        cnt1_superfamily+=1
    while(float(xs2_superfamily[cnt2_superfamily])<curr and cnt2_superfamily<len(xs2_superfamily)-1):
        cnt2_superfamily+=1
    while(float(xs3_superfamily[cnt3_superfamily])<curr and cnt3_superfamily<len(xs3_superfamily)-1):
        cnt3_superfamily+=1
    while(float(xs4_superfamily[cnt4_superfamily])<curr and cnt4_superfamily<len(xs4_superfamily)-1):
        cnt4_superfamily+=1
    x1_superfamily.append(1-(cnt1_superfamily/len(xs1_superfamily)))
    x2_superfamily.append(1-(cnt2_superfamily/len(xs2_superfamily)))
    x3_superfamily.append(1-(cnt3_superfamily/len(xs3_superfamily)))
    x4_superfamily.append(1-(cnt4_superfamily/len(xs4_superfamily)))
    while(float(xs1_fold[cnt1_fold])<curr and cnt1_fold<len(xs1_fold)-1):
        cnt1_fold+=1
    while(float(xs2_fold[cnt2_fold])<curr and cnt2_fold<len(xs2_fold)-1):
        cnt2_fold+=1
    while(float(xs3_fold[cnt3_fold])<curr and cnt3_fold<len(xs3_fold)-1):
        cnt3_fold+=1
    while(float(xs4_fold[cnt4_fold])<curr and cnt4_fold<len(xs4_fold)-1):
        cnt4_fold+=1
    x1_fold.append(1-(cnt1_fold/len(xs1_fold)))
    x2_fold.append(1-(cnt2_fold/len(xs2_fold)))
    x3_fold.append(1-(cnt3_fold/len(xs3_fold)))
    x4_fold.append(1-(cnt4_fold/len(xs4_fold)))
ys.reverse()
x1_family.reverse()
x2_family.reverse()
x3_family.reverse()
x4_family.reverse()
x1_superfamily.reverse()
x2_superfamily.reverse()
x3_superfamily.reverse()
x4_superfamily.reverse()
x1_fold.reverse()
x2_fold.reverse()
x3_fold.reverse()
x4_fold.reverse()

#print(x4_fold)
import seaborn as sns
sns.set_style('whitegrid')
#plt.rcParams.update({'font.size': 16})
fig,axs=plt.subplots(1,3, figsize=(22.5,5))
axs[0].set_xlim(right=1.0)
axs[0].plot(x1_family[:-1],ys[:-1], label = "Foldseek with PDB", color='black')
axs[0].plot(x1_family[:-1][::10],ys[:-1][::10], marker='o', linestyle='None', color='black', markersize=5, markerfacecolor='none')
axs[0].plot(x3_family[:-1],ys[:-1], label = "Foldseek with ProstT5", color='red')
axs[0].plot(x3_family[:-1][::10],ys[:-1][::10], marker='v', linestyle='None', color='red', markersize=5, markerfacecolor='none')
axs[0].plot(x2_family[:-1],ys[:-1], label = "Foldseek with PDB + C-alphas")
axs[0].plot(x2_family[:-1][::10],ys[:-1][::10], marker='D', linestyle='None', color='steelblue', markersize=5, markerfacecolor='none')
axs[0].plot(x4_family[:-1],ys[:-1], label = "Foldseek with ProstT5 + C-alphas")
axs[0].plot(x4_family[:-1][::10],ys[:-1][::10], marker='s', linestyle='None', color='darkorange', markersize=5, markerfacecolor='none')
axs[0].set_ylabel("ROC1")
axs[0].set_xlabel("Query coverage")
#axs[0].legend(fontsize='small')
axs[0].set_title("Family")

axs[1].set_xlim(right=1.0)
axs[1].plot(x1_superfamily[:-1],ys[:-1], label = "Foldseek with PDB", color='black')
axs[1].plot(x1_superfamily[:-1][::10],ys[:-1][::10], marker='o', linestyle='None', color='black', markersize=5, markerfacecolor='none')
axs[1].plot(x3_superfamily[:-1],ys[:-1], label = "Foldseek with ProstT5", color='red')
axs[1].plot(x3_superfamily[:-1][::10],ys[:-1][::10], marker='v', linestyle='None', color='red', markersize=5, markerfacecolor='none')
axs[1].plot(x2_superfamily[:-1],ys[:-1], label = "Foldseek with PDB + C-alphas")
axs[1].plot(x2_superfamily[:-1][::10],ys[:-1][::10], marker='D', linestyle='None', color='steelblue', markersize=5, markerfacecolor='none')
axs[1].plot(x4_superfamily[:-1],ys[:-1], label = "Foldseek with ProstT5 + C-alphas")
axs[1].plot(x4_superfamily[:-1][::10],ys[:-1][::10], marker='s', linestyle='None', color='darkorange', markersize=5, markerfacecolor='none')
axs[1].set_ylabel("ROC1")
axs[1].set_xlabel("Query coverage")
#axs[1].legend(fontsize='small')
axs[1].set_title("Superfamily")

axs[2].set_xlim(right=1.0)
axs[2].plot(x1_fold[:-1],ys[:-1], color='black')
axs[2].plot(x1_fold[20:-1][::10],ys[20:-1][::10], marker='o', linestyle='None', color='black', markersize=5, markerfacecolor='none', label = "Foldseek with PDB")
axs[2].plot(x3_fold[:-1],ys[:-1], color='red')
axs[2].plot(x3_fold[20:-1][::10],ys[20:-1][::10], marker='v', linestyle='None', color='red', markersize=5, markerfacecolor='none', label = "Foldseek with ProstT5")
axs[2].plot(x2_fold[:-1],ys[:-1])
axs[2].plot(x2_fold[20:-1][::10],ys[20:-1][::10], marker='D', linestyle='None', color='steelblue', markersize=5, markerfacecolor='none', label = "Foldseek with PDB + C-alphas")
axs[2].plot(x4_fold[:-1],ys[:-1])
axs[2].plot(x4_fold[20:-1][::10],ys[20:-1][::10], marker='s', linestyle='None', color='darkorange', markersize=5, markerfacecolor='none', label = "Foldseek with ProstT5 + C-alphas")
axs[2].set_ylabel("ROC1")
axs[2].set_xlabel("Query coverage")
axs[2].legend()
axs[2].set_title("Fold")


fig.savefig("joined_graph.pdf", bbox_inches='tight', pad_inches=0.3, dpi=500)       