#!/usr/bin/env python3

"""tile:cover a wall with bricks

__author__ = "Li Yichen"
__pkuid__  = "1800011849"
__email__  = "1800011849@pku.edu.cn"
"""

a=int(input('瓷砖长:'))
b=int(input('瓷砖宽:'))
m=int(input('墙长:'))
n=int(input('墙宽:'))
import sys  #扩大递归深度 
sys.setrecursionlimit(10000000)     
def cover(q,a,b,p):
    '''
    用axb的砖块从第q块铺名字为p的墙
    '''
    l=()
    for i in range(b):
        for j in range(q,q+a):
            p[j]=1
            l=l+(j,)
        q+=m
    return l
def judge(q,a,b,p):
    '''
    判断是否可以在第q块铺axb的砖块
    '''
    true=True
    w=(q//m+1)*m
    for i in range(b):
        if q+(a-1)>=min(w,len(p)) :
            return False
        for j in range(q,q+a):
            if p[j]==1:
                true=False
        q+=m
        w+=m
    return true
way=[[]]
total=0
last=[]
def kaishipu(m,n,a,b):
    '''
    开始铺设
    '''
    for ways in way:
        if len(ways)==m*n/a/b:
            last.append(ways)
            way.remove(ways)
            kaishipu(m,n,a,b)
        else:
            for a,b in[(a,b),(b,a)]:
                lstt=[0]*m*n
                for q in ways:
                    for w in q:
                        lstt[w]=1
                for h in range(len(lstt)):
                    if lstt[h]==0:
                        break
                if judge(h,a,b,lstt):
                    x=cover(h,a,b,lstt)
                    wayss=ways+[x]
                    way.append(wayss)        
            way.remove(ways)
            kaishipu(m,n,a,b)


def visual():
    '''
    将获得的组数加以处理，并以乌龟作图的形式表现出来
    '''
    if a==b:
        x=len(last)
        for i in range(1,x):
            del last[-1]                
    g=0
    sol={}
    for i in range(len(last)):
        
        g+=1
        sol['第'+str(g)+'组：']=last[i]
    for i in sol:
        print(i,sol[i])
    if g==0:
        print('铺不了，重新输')
    else:
        
        import turtle
        p=int(turtle.numinput('输入','想可视化的组数',1,minval=1,maxval=(len(last))))
        t=sol['第'+str(p)+'组：']
        cdg=turtle.Turtle()
        cdg.color('blue')
        cdg.pensize(1)
        cdg.speed(0)
        cdg.hideturtle()
        for i in range(n):
            for j in range (m):
                x1=30*(j-m/2)
                x2=30*(j+1-m/2)
                y1=30*(i-n/2)
                y2=30*(i+1-n/2)
                cdg.penup()
                cdg.goto(x1,y1)
                cdg.pendown()
                cdg.goto(x2,y1)
                cdg.goto(x2,y2)
                cdg.goto(x1,y2)
                cdg.goto(x1,y1)
                cdg.penup()
                cdg.goto((2*x1+x2)/3,y1)
                cdg.write(str(i*m+j))
        yhf=turtle.Turtle()
        yhf.pencolor('black')
        yhf.pensize(2)
        yhf.hideturtle()
        for i in t:
            o1=i[0]
            o2=i[-1]
            km1=o1%m
            km2=o2%m
            kn1=o1//m
            kn2=o2//m
            x1=30*(km1-m/2)
            x2=30*(km2+1-m/2)
            y1=30*(kn1-n/2)
            y2=30*(kn2+1-n/2)
            yhf.penup()
            yhf.goto(x1,y1)
            yhf.pendown()
            yhf.goto(x2,y1)
            yhf.goto(x2,y2)
            yhf.goto(x1,y2)
            yhf.goto(x1,y1)
def main():
    kaishipu(m,n,a,b)
    visual()
if __name__=='__main__':
    main()

