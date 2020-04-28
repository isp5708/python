from tkinter import *
from tkinter import messagebox
import random
import time
import sys


class makeBridge:
    def __init__(self,peopleCount):
        self.peopleCount=peopleCount #사람수
        self.bridgeCount=peopleCount*2 #다리갯수
        self.arrayRow=peopleCount*2+2
        self.arrayColumn=peopleCount+2  #Matrix = [[0 for x in range(w)] for y in range(h)]  컬럼 , 열 순서
        self.bridge=[[0 for x in range(self.arrayColumn)]for y in range(self.arrayRow)]  #배열에 사다리 위치를 그림
        self.location=[[0 for x in range(self.arrayColumn)]for y in range(self.arrayRow)] #y좌표값을 저장해놈 사다리를 그리기위해서
        self.indexTrace = [[0 for x in range(self.arrayColumn)] for y in range(self.arrayRow)] # 인덱스 자취
        self.locationArrayOneHeight=540/(self.peopleCount*2)
        for i in range(0,self.arrayRow-1,1):
            for j in range(1,self.arrayColumn-1,1):
                self.location[i+1][j]=80+self.locationArrayOneHeight/2+self.locationArrayOneHeight*i

        print(self.location)


    def randomBridgeMake(self):  # 다리랜덤하게 생성
        i=0
        while i<self.peopleCount*2:#random.randint(1, 10) 1~10까지 정수난수발생
            x=random.randint(1,self.peopleCount*2) #행
            y=random.randint(1,self.peopleCount-1)#열
            if self.bridge[x][y]==0 and self.bridge[x][y+1]==0:
                self.bridge[x][y]=i+1
                self.bridge[x][y+1] = i + 1
            else:
                i=i-1
            i=i+1






class mainLadder: #처음 인원수와  각위치에 내용을 넣을 클래스
    def __init__(self):
        self.window=Tk()
        Label(self.window, text="사람 수:").grid(row=0)
        self.e1 = Entry(self.window)
        self.etUser=[]
        self.etItem=[]
        self.resultLabel=[]
        self.arraySize=80
        self.e1.grid(row=0,column=1)
        self.ballArray=[] #공을만들어주는 배열
        self.mi = Button(self.window, text='시작', command=self.makeItem)
        self.mi.grid(row=1, column=0, sticky=W)
        self.window.mainloop()

    def makeItem(self):

        try:
            self.count = int(self.e1.get())
            if self.count>1 and self.count<= 10:  #사다리타기 10명까지만으로 사람제한
                for i in range(self.count):
                    Label(self.window, text=str(i+1) + ".").grid(row=2 + i)
                    self.etUser.append( Entry(self.window))
                    self.etUser[i].grid(row=2+i,column=1)

                Label(self.window, text="당첨 항목: ").grid(row=2 + self.count)

                for i in range(self.count):
                    Label(self.window, text=str(i+1)).grid(row=3 + self.count + i)
                    self.etItem.append(Entry(self.window))
                    self.etItem[i].grid(row=3+self.count+i,column=1)
                self.mi.configure(state='disabled')  # 버튼의 상태변경
                self.btnStart=Button(self.window,text='사다리타기 시작~',command=self.newCanvos)
                self.btnStart.grid(row=4+self.count*2)
            else:
                messagebox.showinfo(title="오류", message="2명이상 10명이하로해주세요")
        except ValueError:
            messagebox.showinfo(title="오류", message="숫자로 입력하여주세요.")
    def newCanvos(self): #정보를 다입력하고 버튼을 누를시 새로운 창이뜨게해주는 함수.
        t=Toplevel(self.window)
        c=Canvas(t,width=(self.count+2)*80,height=700) # 가로크기는 사람수에 비례하여 늘어나고 세로는 700으로 고정시켜둠
        c.pack()
        self.makeLadderFrame(c)
        self.labelprint(t)

        mb=makeBridge(self.count)
        mb.randomBridgeMake()
        print(mb.bridge)
        self.drawBridge(mb,c) # 사다리다리를 만듬
        self.ballMake(c) #이동시킬 공을만듬
        self.ballMove(c,mb,t)


    def ballMake(self,c):#공만드는함수
        for i in range(self.count):
            id=c.create_oval(self.arraySize*i+95,20,self.arraySize*i+130,60,fill="red")
            self.ballArray.append(id)
    def ballMoveDown(self,i,c,t):  #공을 아래로이동
        for j in range(self.arrayHeight):
            c.move(self.ballArray[i], 0, 1)
            t.update()
            time.sleep(0.001)
    def ballMoveLeft(self,i,c,t): #공을 왼쪽으로이동
        for j in range(80):
            c.move(self.ballArray[i], -1, 0)
            t.update()
            time.sleep(0.001)
    def ballMoveRight(self,i,c,t): #공을 오른쪽으로이동
        for j in range(80):
            c.move(self.ballArray[i], 1, 0)
            t.update()
            time.sleep(0.001)
    def ballMoveDownEception(self,i,c,t):# 공이 맨마지막으로내려올때 내가지정해놓은 처음배열사이즈와달라 예외처리를해주어야한다. 아니면 조금짧게도착하거나 길게도착한다.
        for j in range(int(self.arrayHeight/2+40)):
            c.move(self.ballArray[i], 0, 1)
            t.update()
            time.sleep(0.001)

    def ballMove(self,c,mb,t): #인덱스 시작위치 , 캔버스, 다리좌표값찍힌 배열들, 공의 id값
        for i in range (self.count): #인원수의 공만큼 움직임
            self.arrayHeight=int(540/(self.count*2))
            x = 1
            y = 1+i
            n = 0
            for l in range(40+int(self.arrayHeight/2)): #일단 배열아래로 내려가야하기때문에 아래로 이동시켜준다.
                c.move(self.ballArray[i], 0, 1)
                t.update()
                time.sleep(0.001)
            while n<self.count*2: #아래로 사용자수*2-1 만큼 이동하면 끝이나야한다.
                if mb.bridge[x][y]==0:  #현재위치의 값이 0이면 무조건 아래로내려간다.
                    if n == self.count * 2 - 1:
                        self.ballMoveDownEception(i, c, t)
                    else:
                        self.ballMoveDown(i, c, t)
                    x=x+1
                elif mb.bridge[x][y]==mb.bridge[x][y-1] and mb.bridge[x][y]!=0: #현재위치의왼쪽과 현재위치의 값이같고 0이아닐시 왼쪽으로이동하고 아래로내려간다.
                    self.ballMoveLeft(i,c,t)
                    if n==self.count*2-1:
                        self.ballMoveDownEception(i,c,t)
                    else:
                        self.ballMoveDown(i,c,t)
                    x=x+1
                    y=y-1
                elif mb.bridge[x][y]==mb.bridge[x][y+1]and mb.bridge[x][y]!=0: #현재위치의 오른쪽과 현재위치의 값이같고 0이아닐시 오른쪽으로이동하고 아래로내려간다.
                    self.ballMoveRight(i,c,t)
                    if n==self.count*2-1:
                        self.ballMoveDownEception(i,c,t)
                    else:
                        self.ballMoveDown(i,c,t)
                    x=x+1
                    y=y+1
                n=n+1
            #etUser[] etItem[]
            self.resultLabel[i].config(text=self.etItem[y-1].get()+"의 주인공은"+self.etUser[i].get())
            print("%d %d" % (x, y))

    def labelprint(self,t): #Toplevel에 라벨을표시해주는함수
        for i in range (len(self.etItem)):
            la=Label(t,text=str(i+1)+".")
            la.pack()
            self.resultLabel.append(la)


    def makeLadderFrame(self,c):  #비율을 고정시켜놔 기본틀을 그리게함
        for i in range(self.count):
            c.create_rectangle(self.arraySize*i+95,20,self.arraySize*i+130,60) # 35 35  사이즈의 버튼
            c.create_rectangle(self.arraySize*i+95,640,self.arraySize*i+130,680)
            c.create_line(115+i*self.arraySize,60,115+i*self.arraySize,640)
    def drawBridge(selfs, makeBridge,c):
        for i in range(1,len(makeBridge.bridge)-1):
            for j in range(1,len(makeBridge.bridge[0])-2): #열 수
                if makeBridge.bridge[i][j] !=0 and makeBridge.bridge[i][j+1]!=0and makeBridge.bridge[i][j]==makeBridge.bridge[i][j+1]:
                    c.create_line(36+j*80,makeBridge.location[i][j],36+(j+1)*80,makeBridge.location[i][j])




mi=mainLadder()
