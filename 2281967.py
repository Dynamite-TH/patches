from graphix import Window, Point, Circle,Rectangle, Text, Entry

def draw_circle(win, center, radius, colour,outsidecolour):
    circle = Circle(center, radius)
    circle.fill_colour = colour
    circle.outline_colour = outsidecolour
    circle.draw(win)

def draw_rectangle(win, point1, point2, colour):
    rect = Rectangle(point1, point2)
    rect.fill_colour = colour
    rect.outline_colour = colour
    rect.draw(win)

def patch_1(win,colour,tl_corner):
    br_corner = Point(tl_corner.x + 100,tl_corner.y + 100)
    draw_rectangle(win, tl_corner, br_corner, colour)
    
def Patch_2(win,X,Y,colour):
    row = 5

    for y in range(Y, 100+Y, 20):
        for x in range(X, 100+X, 20):

            if row % 2 == 0:
                center = Point(x + 10, y + 10)
                draw_circle(win, center, 10, "white",colour)
            else:            
                center = Point(x + 10, y + 10)
                draw_circle(win, center, 10, colour,colour)
        row -=1

def patch_3(win,X,Y,colour):
    flag = True
    for y in range(Y, Y + 100, 20):
        for x in range(X, X + 100, 20):
                # Inverse Rectangles going left to right
                if flag == True and (x+y)==((X)+(Y+40)) or  (x+y)==((X+40)+(Y+80)):
                    draw_rectangle(win, Point(x,y+5), Point(x+20,y+10), colour)
                    draw_rectangle(win, Point(x, y+15), Point(20+x,20+y), colour)
                # Rectangles going left to right
                elif flag == True and (x + y) == (X +Y) or (x+y) == ((X+80)+(Y+80)) or x+y==((X+20)+(Y+60)) :
                    draw_rectangle(win, Point(x,y), Point(x+20,y+5), colour)
                    draw_rectangle(win, Point(x, y+10), Point(20+x,15+y), colour)
                # Rectangles going Top Down
                elif flag == False and x+y == ((X)+(Y+20)) or (x+y)== ((X+40)+(Y+60)):
                    draw_rectangle(win, Point(x,y), Point(x+5,y+20), colour)
                    draw_rectangle(win, Point(x+10, y), Point(x+15,20+y), colour) 
                # Inverse Rectangles going Top Down
                elif flag == False and (x+y)==((X+20)+(Y+40)) or (x+y)==((X+60)+(Y+80)):
                    draw_rectangle(win, Point(x+5,y), Point(x+10,y+20), colour)
                    draw_rectangle(win, Point(x+15, y), Point(x+20,20+y), colour) 

                flag = not flag

def grid(win,sc_size,colour_1,colour_2,colour_3):
    count = 1

    # patch_1 going down right side
    for i in range(sc_size):
        patch_1(win,colour_1,Point(0,0+(i*100)))

    # Alternating  patch_1 across the bottom
    for i in range(sc_size-1):
        if count % 2 == 0:
            patch_1(win,colour_1,Point(100+(i*100),(sc_size*100) - 100))
        else:
            patch_1(win,colour_3,Point(100+(i*100),(sc_size*100) - 100))
        count += 1

    # Drawing the inner patch_1
    for i in range(sc_size - 3):
        patch_1(win,colour_2,Point(200+(i*100),100))
        patch_1(win,colour_2,Point(300,200))

    # Drawing the inner patch_1 that are not included in the screen size of 5
    if (sc_size != 5):
        for i in range (2):
            patch_1(win,colour_2,Point(400,200+(i*100)))
        for i in range(3):
            patch_1(win,colour_2,Point(500,200+(i*100)))

    # Drawing the inner patch_1 that are only included in screen size 9        
    if (sc_size == 9):
        for i in range(4):
            patch_1(win,colour_2,Point(600,200+(i*100)))
        for i in range(5):
            patch_1(win,colour_2,Point(700,200+(i*100)))
    # Drawing the last Patches of Patch_3 that are only included in screen size 9
        for i in range(2):
            patch_3(win,600,600+(i*100),colour_1)
        patch_3(win,700,700,colour_3)

    # Drawing of patch_2 across the top and Right side of the screen
    for i in range(sc_size - 2):
        Patch_2(win,100+(i*100),0, colour_2)
    for i in range(sc_size-1):
        Patch_2(win,((sc_size*100)-100),0+(i*100), colour_2)

    # Drawing of Patch 3 with alternating colours allowing the columns
    for i in range(sc_size - 2):
        patch_3(win,100,100+(i*100),colour_3)
    for i in range(sc_size - 3):
        patch_3(win,200,200+(i*100),colour_1)
    for i in range(sc_size-4):
        patch_3(win,300,300+(i*100),colour_3)
    for i in range(sc_size-5):
        patch_3(win,400,400+(i*100),colour_1)
    for i in range(sc_size-6):
        patch_3(win,500,500+(i*100),colour_3)

def program():
    screen = [5,7,9]
    colours = ["red", "green", "blue", "magenta", "orange", "purple"]
    flag = True
    while flag == True:
        sc_size = int(input("Size of screen 5, 7 or 9:"))
        if sc_size in screen:
            colour_1 = input("colour 1:")
            colour_2 = input("colour 2:")
            colour_3 = input("colour 3:")
            if colour_1 in colours and colour_3 in colours and colour_2 in colours:
                win = Window("Grid Patterns", sc_size * 100, sc_size * 100)       
                grid(win,sc_size,colour_1,colour_2,colour_3)

                win.get_mouse()
                win.close()
                flag = not flag
            else:
                print("Invalid Selection")
        else:
            print("Invalid Selection")

program()




