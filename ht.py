# -*- coding: cp936 -*-
import linecache
o=open('Ӣ��������.txt')#�ļ�·��
o.seek(0)
r=o.readlines()
s1=str(input('����Ҫ��λ����Ϣ:'))
for i in r: #����ֵ��ϲ���
    if i.find(s1)>=0:       
        print(i)#��ʾ��λ��
print ('Total:%d'%count)
