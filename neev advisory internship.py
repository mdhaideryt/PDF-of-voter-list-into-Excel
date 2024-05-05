with open("Neev english edited.txt",'r+') as file:
    t1=file.read().lower()
    t=list(t1)
    if ":" in t:
        t.remove(":")
    else:
        pass
t=[i for i in t if i!=":"]
text=''.join(t)
# print(t)
# print(text)
with open("Neev english edited.txt",'w') as file:
    file.write(text)
with open("Neev english.txt", 'r') as file:
    t1=file.read().split()
    t=list(t1)
    print(len(t))
    print(t)
    name_of_elector=[]
    father_or_husband=[]
    house_no=[]
    age=[]
    EPIC_number=[]
    for i in range(len(t)-5):
        if (len(t[i])==10 and t[i].isalnum()) or (len(t[i])==16):
            #print(t[i],end=" ")
            EPIC_number.append(t[i])
        if t[i]=='name' and t[i+1]=='of' and (t[i+2]=='voter' or t[i+2]=='elector'):
            if (t[i+4] in ["name","husband's","father's","photo","house","age","gender",t[i+4].isalnum(),t[i+4].isnumeric()]) and (len(t[i+4])!=16):
                name_of_elector.append(t[i+3])
            elif (t[i+4] not in ["name","husband's","father's","photo","house","age","gender",t[i+4].isalnum(),t[i+4].isnumeric()]) and (t[i+5] in ["name","husband's","father's","photo","house","age","gender",t[i+5].isalnum(),t[i+5].isnumeric()]) and (len(t[i+4])!=16):
                full_name=' '.join([t[i+3],t[i+4]])
                name_of_elector.append(full_name)
            elif ((t[i+4] and t[i+5]) not in ["name","husband's","father's","photo","house","age","gender",t[i+4].isalnum(),t[i+4].isnumeric(),t[i+5].isalnum(),t[i+5].isnumeric()]) and (t[i+6] in ["name","husband's","father's","photo","house","age","gender",t[i+5].isalnum(),t[i+5].isnumeric()]):
                full_name = ' '.join([t[i + 3], t[i + 4],t[i+5]])
                name_of_elector.append(full_name)
        if (t[i]=="father's" or t[i]=="husband's") and t[i+1]=='name':
            if t[i+3] in ["name","husband's","father's","photo","house","age","gender",t[i+3].isalnum(),t[i+3].isnumeric()]:
                father_or_husband.append(t[i+2])
            elif (t[i+3] not in ["name","husband's","father's","photo","house","age","gender",t[i+3].isalnum(),t[i+3].isnumeric()]) and (t[i + 4] in ["name","husband's","father's","photo","house","age","gender",t[i+4].isalnum(),t[i+3].isnumeric()]) and (len(t[i+3])!=16):
                full_name=' '.join([t[i+2],t[i+3]])
                father_or_husband.append(full_name)
            elif ((t[i+3] and t[i+4]) not in ["name","husband's","father's","photo","house","age","gender",t[i+4].isalnum(),t[i+4].isnumeric(),t[i+3].isalnum(),t[i+3].isnumeric()]) and (len(t[i+4])!=16):
                full_name = ' '.join([t[i + 2], t[i + 3],t[i+4]])
                father_or_husband.append(full_name)
        if t[i]=='house' and t[i+1]=='number' and t[i+2].isnumeric():
            house_no.append(t[i+2])
        if t[i]=='age' and t[i+1].isnumeric():
            age.append(t[i+1])
# print(name_of_elector,end=' ')
# print(father_or_husband, end=' ')
# print(house_no,end=' ')
# print(age,end=" ")
# print(EPIC_number, end=" ")
import pandas as pd
df=pd.DataFrame(list(zip(name_of_elector,father_or_husband,house_no,age,EPIC_number)), columns=['Name_of_Voter',"Father/Husband's name","House_No.","Age","EPIC_Number"])
df.to_excel("neev_Md Rumman Haider.xlsx",index=False)