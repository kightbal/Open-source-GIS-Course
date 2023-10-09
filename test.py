import re;
'''[.]表示.这个字符，而不加括号的单独.表示任意一个字符，除了/n即回车'''
mode1=re.compile("[经精]度[:：][0-9]+.[0-9]+")
mode2=re.compile("[纬维]度[:：][0-9]+.[0-9]+")
with open("作业提交//学生报道.md","rt",encoding='utf-8') as f:
    K=f.read();
f.close();
print(K)
data1= re.findall(mode1,K)
print(data1)
data1_str=''.join(data1)
data2=re.findall(mode2,K)
data2_str=''.join(data2)
mode3=re.compile("[0-9]+.[0-9]+")
longitude=re.findall(mode3,data1_str)
latitude=re.findall(mode3,data2_str)
mode4=re.compile("°")
data_long=list()
data_lati=list()
for i in range(len(longitude)):
     longitude[i]= eval(re.sub(mode4,".",longitude[i]))
     latitude[i]=eval(re.sub(mode4,".",latitude[i]))
T= {"东北":0,"东南":0,"西北":0,"西南":0}
for i in range(len(longitude)):
    if(longitude[i]-102.851>0):
        if(latitude[i]-24.841>0):
            T["东北"]=T["东北"]+1
        else:
            T["东南"]=T["东南"]+1
    else:
        if(latitude[i]-24.841>0):
            T["西北"]=T["西北"]+1
        else:
            T["西南"]=T["西南"]+1
scale1=T["东北"]/float(len(longitude))
scale2=T["东南"]/float(len(longitude))
scale3=T["西北"]/float(len(longitude))
scale4=T["西南"]/float(len(longitude))
print("东北:"+str(scale1)+"东南:"+str(scale2)+"西北:"+str(scale3)+"西南:"+str(scale4));