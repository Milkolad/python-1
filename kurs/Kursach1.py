import os 
import numpy as np
import collections 

def scan(s,v):
    symb=""
    for ch in s:
        if((ch!='+')&(ch!="/")&(ch!=s[-1])): symb+=ch
        elif((symb=="")&(ch==s[-1])): v.append(ch)
        elif(symb!=""): v.append(symb); symb="" 

def printf(v):
    count=0
    for i in range(len(v)//2):
        if(v[i]!=v[-1]): print(v[count]+"/"+v[count+1], end=''); count+=2
        if(i!=(len(v)//2)-1): print("+", end='')
    print()

def mult(x,y):
    arrnonzero = []
    #ar = np.zeros((40))
   # for i in range(3):
    ar = []
    ar1 = []
    ar1pr= []
    armin = []
    max_value = []
    for i in range(len(x)//2):
        ar.append(np.add(x[i+i+1],y[1::2]))
        ar1pr = np.hstack((ar1pr,ar[i]))
        ar1.append(np.fmin(x[i+i],y[0::2]))
        armin = np.hstack((armin, ar1[i]))
    arrr = np.vstack((ar1pr,armin))
    print(arrr)
    counter = collections.Counter(ar1pr).most_common()
    print(counter)
    counter1 = list(counter)
    counter1 = list(map(list,counter1))
    print(counter1)
    for i in range(len(counter1)):
        counter2 = list(map(str,counter1[i]))
        coun = int(counter2[1])
        if (coun >1) : 
            print(coun)
            arrnonzero.append(counter2[0])
        #print(counter2[1])
    print("non",arrnonzero)
    if len(arrnonzero)!=0:
        print("yclovie")
        #for j in range(len(arrnonzero[i]))
        for i in range(len(arrnonzero)):
            index = np.where(arrr[0,]==float(arrnonzero[i]))
            print("index = ",index[0])
            max_value = float(0.0)
            for i in range(len(index[0])):
                print("last")
                max_value = np.maximum(arrr[1][index[0][i]],max_value)
            index_delete = np.where(arrr[1,]!=max_value)
            print("max_value = ",max_value)
            print("index_delete = ",index_delete[0])
            index1 = list(set(index[0]) & set(index_delete[0]))
            for i in range(len(set(index1).symmetric_difference(set(index[0])))-1):
                index1.append(index[0][i])
            print("delete this",index1)
            arrr = np.delete(arrr , index1 , axis=1)
            print(arrr)
        arrr[0] , arrr[1] = list(arrr[1]) , list(arrr[0])
        arrr = np.reshape(arrr,len(arrr)*len(arrr[0]), order="f")
        return arrr
        


def main():
    A=[]
    B=[]
    C = []
    print("Введите A")
    string="0.2/2+0.3/1+0.6/3+0.2/4"
    scan(string, A)
    printf(A)
    print("Введите B")
    string="0.1/5+1/1+0.5/2+0.6/4"
    scan(string, B)
    printf(B)
    A = list(map(float,A))
    B = list(map(float,B))
    print(A)
    print(B)
    C = mult(A,B)
    C = list(map(str,C))
    printf(C)


if __name__ == '__main__':
   main()