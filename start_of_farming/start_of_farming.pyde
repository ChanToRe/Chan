class Patch(): #자원집중
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.status = 'nature'
    def display(self):
        if self.status == 'nature':
            shapeMode(CENTER)
            fill(0, 255, 0)
            triangle(self.x, self.y - 3, self.x - 3, self.y + 3, self.x + 3, self.y + 3)
        elif self.status == 'farming':
            shapeMode(CENTER)
            fill(255, 0, 0)
            triangle(self.x, self.y - 3, self.x - 3, self.y + 3, self.x + 3, self.y + 3)
            ellipseMode(CENTER)
            noFill()
            ellipse(self.x, self.y, 50, 50) 
            
class H_residence(): #수렵채집사회 주거지
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.status = 'hunting'
    def display(self):
        if self.status == 'hunting':
            fill(0, 0, 255)
            ellipseMode(CENTER)
            ellipse(self.x, self.y, 5, 5)
            ellipseMode(CENTER)
            noFill()
            ellipse(self.x, self.y, 100, 100)
        elif self.status == 'farming':
            shapeMode(CENTER)
            fill(255, 0, 0)
            triangle(self.x, self.y - 3, self.x - 3, self.y + 3, self.x + 3, self.y + 3)
            ellipseMode(CENTER)
            noFill()
            ellipse(self.x, self.y, 50, 50) 
        
class F_residence():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.status = 'farming'
    def display(self):
        shapeMode(CENTER)
        fill(255, 0, 0)
        triangle(self.x, self.y - 3, self.x - 3, self.y + 3, self.x + 3, self.y + 3)
        ellipseMode(CENTER)
        noFill()
        ellipse(self.x, self.y, 50, 50) 
        
        
#main
N_PATCH = 40
N_H_RESIDENCE = 30
N_F_RESIDENCE = 5

patchs = []
h_residences = []
f_residences = []

for i in range(N_PATCH):
    patchs.append(Patch(x=random(0, 470), y=random(0, 470)))
for i in range(N_H_RESIDENCE):
    h_residences.append(H_residence(x=random(0, 470), y=random(0, 470)))        
for i in range(N_F_RESIDENCE):
    f_residences.append(F_residence(x=random(0, 470), y=random(0, 470)))    
 
def setup():
    frameRate(60)
    size(470, 470)

def draw():
    background(127)
    
    for patch in patchs:
        patch.display()
    for h_residence in h_residences:
        h_residence.display()
    for f_residence in f_residences:
        f_residence.display()
