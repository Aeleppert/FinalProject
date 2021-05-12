class NumberButtons:
    def __init__(self,text,x,y):
        self.text= text
        self.color= "#AF9057"
        self.x=x
        self.y=y
        return;

    def display(self):
        fill(self.color)
        ellipseMode(LEFT)
        textAlign(CENTER)
        rect(self.x, self.y,30,30)
        fill(250)
        text(self.text, self.x+15, self.y+20)
        return;
    def changecolor(self):
        if (mouseX>self.x and mouseY>self.y and mouseX<self.x+30 and mouseY<self.y+30):
            self.color = "#BFA679"
        else:
            self.color = "#AF9057"
        return;
    def hover():
        hover = (mouseX>self.x and mouseY>self.y and mouseX<self.x+22 and mouseY<self.y+22)
        self.color = "#BFA679"
        return;
