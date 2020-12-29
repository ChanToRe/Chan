#수렵채집사회 주거지의 영역범위와 농경사회 주거지의 영역범위가 서로 상충할 경우 수렵채집사회의 스트레스 +1

class Residence():
    def __init__(self, x, y, v=2.5):
        self.x = x
        self.y = y
        self.status = 'hunting'
        self.stress = 0
        self.v = v
        
    def display(self):
        if self.status == 'hunting':
            shapeMode(CENTER)
            fill(0, 255, 0)
            triangle(self.x, self.y - 3, self.x - 3, self.y + 3, self.x + 3, self.y + 3)
            ellipseMode(CENTER)
            noFill()
            ellipse(self.x, self.y, 60, 60)
            
        elif self.status == 'farming':
            shapeMode(CENTER)
            fill(255, 0, 0)
            triangle(self.x, self.y - 3, self.x - 3, self.y + 3, self.x + 3, self.y + 3)
            ellipseMode(CENTER)
            noFill()
            ellipse(self.x, self.y, 60, 60)
            
    def change(self):
        for Residence in residences:
            
            distence = sqrt((self.x - Residence.x)**2 + (self.y - Residence.y)**2)
            
            if Residence.status == 'hunting':
                if distence <= 60:
                    Residence.stress += 1
                    
                    if Residence.stress >= 1000 :
                        if self.status == 'farming' and Residence.status == 'hunting':
                            Residence.status = 'farming'
                            break
                        elif self.status == 'hunting' and Residence.status == 'farming':
                            Residence.status = 'farming'
                            break
            elif Residence.status == 'farming':
                continue
                        
    def move(self):
        for residence in residences:
            self.dst_x = random(-1500, 1500)
            self.dst_y = random(-1500, 1500)
    
            dist = sqrt((self.dst_x - self.x) ** 2 + (self.dst_y - self.y) ** 2)
    
        if self.status == 'hunting':

            dist_x = (self.dst_x - self.x) * self.v
            dist_y = (self.dst_y - self.y) * self.v
            
            self.x += dist_x / dist
            self.y += dist_y / dist
            
#main
RESIDENCE = 200

residences = []

W, H = 500, 500
for i in range(RESIDENCE):
    residences.append(Residence(x=random(0, 500), y=random(0, 500)))
    
residences[0].status = 'farming'
residences[1].status = 'farming'

def setup():
    frameRate(60)
    size(W, H)
    
def draw():
    background(127)

    for residence in residences:
        residence.change()
        residence.display()
        residence.move()
