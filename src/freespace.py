class Freespace:
    def __init__(self,number,x,y):
        self.number=number
        self.x=x
        self.y=y
        self.dist = 22
        self.color = "#AF9057"
        hover = False
        return;

    def display(self):
        strokeWeight(1)
        fill(self.color)
        rect(self.x,self.y,self.dist,self.dist)
        strokeWeight(2.5)
        line(228,162,228,360)
        line(294,162,294,360)
        line(162,228,360,228)
        line(162,294,360,294)
        strokeWeight(1)
        textSize(18)
        fill(0)
        textAlign(CENTER)
        text(self.number,self.x+10,self.y+18)
        return;
    def changecolor(self):
        if (mouseX>self.x and mouseY>self.y and mouseX<self.x+22 and mouseY<self.y+22):
            self.color = "#BFA679"
        else:
            self.color = "#AF9057"
        hover = True
        return;
    def hover():
        hover = (mouseX>self.x and mouseY>self.y and mouseX<self.x+22 and mouseY<self.y+22)
        self.color = "#BFA679"
        return;
    # def newnumber():
