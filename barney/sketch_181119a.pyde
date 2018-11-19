

def setup():

    size(1000, 600)

    background(100,170,255)

    noStroke()

    noLoop()

    

def draw():

    drawcloud(200, 150)

    drawcloud( 800, 300)

def drawcloud(xloc, yloc):
 
            
    for i in range(3):

        ellipse(xloc, yloc+i*50, 100+i*20, 90+i*20)
        ellipse(xloc-i*20, yloc+i*70, 100+i*40, 90+i*30)
        ellipse(xloc+i*40, yloc+i*90, 100+i*60, 90+i*40)
    
   
    
