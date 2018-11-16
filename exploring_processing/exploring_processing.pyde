x = 0

y = 20

p = 600

q = 600

g = 10

text_size = 30

rotation = 0

rotation_speed = 0

text_size_speed = 1

animate = False


def setup(): 
    size(1200, 600)
    global img1
    global img2
    img1 = loadImage("qsc.jpg")
    img2 = loadImage("qscc.jpg")
    
def draw():
    global x
    global p
    global q
    global text_size
    global rotation
    global rotation_speed
    global text_size_speed
    global g
                    
    x += g
    if x >= 1200:
        g = -50
    if x <= 0:
        g = 50
    background(img1)
    
    noStroke()
    
    triangle(p,2*p, 200, 500, 400, 400)
    if keyPressed:
        if key == 'b' or key == 'B':
            p += 10
        if p >= 600:
            p = 0
    rect(y, 20, 150, 150, 80, 80, 20, 20)   
    
    ellipse(x, 200, 150, 150) 
    
    image(img2, q, 300, 300, 200)
    q += 20
    if q >= 1200:
        q = 0
    
    if animate:
        rotation_speed += 0.01
        text_size_speed += 0.3
        text_size += text_size_speed
        rotation += rotation_speed
                                    
    textAlign(CENTER, CENTER)

    translate(width/2, height/2)

    rotate(rotation)

    textSize(text_size)

    fill(255, 110, 0, 255-text_size/2)

    text("Hello", 0, 0)                                    
                                                            
def mouseClicked(): 
   
    global y
    
    y += 100
    if y >= 1200:
        y = 0
        
def keyPressed():
    if keyPressed:
        if key == 'v' or key == 'V':
            global animate
            animate = not animate        
        
            

    
