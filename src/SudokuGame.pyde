# class NumInBox:
#     def __init__(self,text,x,y):
#         self.text= text
#         self.color= 0
#         self.x=x
#         self.y=y


#     def display(self):
#         fill(self.color)
#         textAlign(CENTER)
#         print(text(self.text, self.x+10, self.y+18))
    


        

#Variables
from gamebuttons import*
from numberbuttons import *
from freespace import*
play = False
fixednum = False
select = False
easylevel = Gamebuttons("Easy",400,400)
hardlevel = Gamebuttons("Hard",400,440)
#set up grid for sudoku
grid = [ ['', '','',6,'','','','',3],
    [2,3,'','','',8,'','',''],
    ['',9,8,'','','',2,7,''],
    ['','',9,'','',2,'','',''],
    ['','','',4,'',7,'',1,2],
    [4,'','',8,'','',3,6,''],
    [1,2,'','',8,4,6,5,7],
    [9,4,6,'',3,5,'',2,8],
    ['','',7,'',1,6,'','',''], ]
gridhard = [['','','',4,'','','','',''],
            [7,2,3,'','',9,4,'',''],
            ['','',1,'','','',9,'',''],
            [2,'','',8,'',3,'',5,4],
            ['','','',2,6,'','','',''],
            ['','','','',5,'','','',9],
            [3,'','','','','','','',''],
            [8,7,'','','',6,'','',''],
            [5,'','',3,'',8,'',7,2]]
boxeshard = list()
for j in range(9):
    for i in range(9):
        boxeshard.append(Freespace(gridhard[i][j],162+(22*i),162+(22*j)))
boxes = list()
for j in range(9):
    for i in range(9):
        boxes.append(Freespace(grid[i][j],162+(22*i),162+(22*j))) 
workboxes = list()
for j in range(9):
    for i in range(9):
        workboxes.append(Freespace(grid[i][j],162+(22*i),162+(22*j))) 
numbut = list()
for i in range(9):
    numbut.append(NumberButtons(i+1,25+(42*i),400))
undo = Gamebuttons("Undo", 320,440)
clearnum = NumberButtons("Check", 238,440)
hardfixednumber = list()
easyfixednumber = list()
fixednumber = [0]

for j in range(9):
    for i in range(9):
        if gridhard[i][j] == '':
            hardfixednumber.append(gridhard[i][j])
for j in range(9):
    for i in range(9):
        if grid[i][j] == '':
            easyfixednumber.append(grid[i][j])
print(easyfixednumber)
    
#commad do-things
def mouseClicked():
    if (mouseX>easylevel.x and mouseY>easylevel.y and mouseX<easylevel.x+70 and mouseY<easylevel.y+30):
        for k in range(81):
            workboxes.insert(k,boxes[k]) 
        for i in range(len(easyfixednumber)):
            fixednumber.insert(i,easyfixednumber[i])
        print(fixednumber)    
    if (mouseX>hardlevel.x and mouseY>hardlevel.y and mouseX<hardlevel.x+70 and mouseY<hardlevel.y+30):
        for k in range(81):
            workboxes.insert(k,boxeshard[k])
        for j in range(len(hardfixednumber)):
            fixednumber.insert(j,hardfixednumber[j])
        print(fixednumber)      
    return;
def setup():
    size(500,500)
    background("#FAF8E1")
    
def draw():
    select = False
    startscreen()
  
    for i in range(9):
        if mouseX>numbut[i].x and mouseY>numbut[i].y and mouseX<numbut[i].x+22 and mouseY<numbut[i].y+22:
            select = True
        if select == True:
            numbut[i].color = 0

def keyTyped():
    for i in range(81):
        if mouseX>workboxes[i].x and mouseY>workboxes[i].y and mouseX<workboxes[i].x+22 and mouseY<workboxes[i].y+22: 
                for k in range(len(fixednumber)):
                    if fixednumber[k] == workboxes[i].number:
                        workboxes[i].number=key
                        print (workboxes[i].number)
    return;
def startscreen():
    if not play:
        fill(0)
        textAlign(CENTER)
        textSize(40)
        text("SUDOKU", 250,50)
        textSize(16)
        text("To begin, please select a level difficulty below.", 250, 75)
        text("By Alice Leppert", 80, 465)
        text("May 2021", 80,485)
        fill(0)
        easylevel.display()
        easylevel.changecolor()
        hardlevel.display()
        hardlevel.changecolor()
        undo.display()
        undo.changecolor()
        clearnum.display()
        clearnum.changecolor()
        for i in range(81):
            workboxes[i].display()
            workboxes[i].changecolor()
    return;
# def gameplayeasy():      
#     play = True
#     for i in range(81):
#         boxes[i].display()
#         boxes[i].changecolor()

# def gameplayhard():      
#     play = True
#     for i in range(81):
#         boxeshard[i].display()
#         boxeshard[i].changecolor()
# def enternumber():
#  #   if (mouseX>test.x and mouseY>test.y and mouseX<test.x+70 and mouseY<test.y+30):
#  #       test.changecolor() 
#     return;
# def clearbutton():
#     return;
# def check():
#     return;
