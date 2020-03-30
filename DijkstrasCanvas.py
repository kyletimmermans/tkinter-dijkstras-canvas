'''
Kyle Timmermans
March 18th, 2020
python v3.8.2
'''

# Vertex's must be created first, then edges, 'Done' buttons

# Adjacency matrix (2D Array) to store adjacency
# Do I make it so that the user input length changes the weight or just the distance of edge is automatic?

from tkinter import *
from string import ascii_uppercase, ascii_lowercase  # Use to label edges

#############
# Variables #
#############
alphabet1 = ascii_uppercase
alphabet2 = ascii_lowercase
letter = 0
vertexNumber = 10    # ID's start being assigned at 1, but we already have the widgets, they make up first 10 ID's
helperNumber = 1
edgeNumber = vertexNumber  # Continue numbering shapes after vertexes are placed
clickNumber = 0     # Start click number at 0, i.e. start first of 2 clicks to make line
vertexes = {}       # Store vertex number and its location
edges = {}          # Store edge and its location
adjacencyMatrix = []  # Store all weights and vertexes to be traversed over, edited by addEdgeWeight()


#############
# Functions #
#############
def addVertex(event):
    global vertexNumber   # Grab vertexNumber from earlier, it is now global, no need to pass it through as a param now
    global helperNumber   # # Need a dynamic number to add to vertex number
    x0 = event.x    # Current X-Coord for mouse click
    y0 = event.y    # Current Y-Coord for mouse click
    vertex = draw_space.create_oval(x0, y0, x0+50, y0+50, fill="Green", tags="vertex")  # Create the vertex, give it a function soon to add to the dictionary
    vertex_text = draw_space.create_text((x0+25, y0+25), text=vertexNumber-9, tags="vertex")  # +25 to get to the center of a 50 circle
    draw_space.pack()
    if vertexNumber == 1:  # ID's go up by odd numbers b/c be are essentially creating two objects, the circle and its textbox label
        vertexes[vertexNumber-9] = draw_space.coords(vertexNumber)   # Coords just going with continuity of id's auto-assigning
    else:
        vertexes[vertexNumber-9] = draw_space.coords(vertexNumber+helperNumber)  ##### Maybe not use .coords but just ID??
        helperNumber += 1  # increment and add to vertex labels so we get just the vertex circle, place here because we want it to start adding after VN=1
    vertexNumber += 1  # increment vertex labels

def addEdge(event):  # Why does *args work for this?
    global clickNumber
    global edgeNumber
    global letter
    global x1, y1
    if clickNumber == 0:  # start pos before mouse is clicked
        x1 = event.x   # start x pos of mouse
        y1 = event.y   # start y pos of mouse
        clickNumber = 1   # On next click, define x2, y2
    else:                  # end coords when mouse is unclicked
        x2 = event.x    # end x pos of mouse
        y2 = event.y    # end y pos of mouse
        line = draw_space.create_line(x1, y1, x2, y2, fill='Black', width=5)   # Draw line with those coords
        if letter <= 25:  # Go through uppercase letters
            if ((x1 < x2) and (y1 < y2)) or ((x1 > x2) and (y1 > y2)):  # Get Edge labeling correct, if same do one way, if different, do other way
                line_text = draw_space.create_text(((x1 + x2) / 2) - 10, ((y1 + y2) / 2) + 10, text=alphabet1[letter], font=("Courier", 25))
            elif ((x1 > x2) and (y1 < y2)) or ((x1 < x2) and (y1 > y2)):
                line_text = draw_space.create_text(((x1 + x2) / 2) + 10, ((y1 + y2) / 2) + 10, text=alphabet1[letter], font=("Courier", 25))
        elif letter > 25:
            if ((x1 < x2) and (y1 < y2)) or ((x1 > x2) and (y1 > y2)):  # Get Edge labeling correct, if same do one way, if different, do other way
                line_text = draw_space.create_text(((x1 + x2) / 2) - 10, ((y1 + y2) / 2) + 10, text=alphabet2[letter-26], font=("Courier", 25))
            elif ((x1 > x2) and (y1 < y2)) or ((x1 < x2) and (y1 > y2)):
                line_text = draw_space.create_text(((x1 + x2) / 2) + 10, ((y1 + y2) / 2) + 10, text=alphabet2[letter-26], font=("Courier", 25))
        draw_space.pack()  # Pack into canvas and give unique ID
        # If start of edge is found in a vertex (x1, y1) and end of edge is found in a vertex (x2, y2), place them in edges {}
        for key in vertexes:
            if (vertexes[key][0] < x1 < vertexes[key][2]) == True:
                vertexStart = key
        for key in vertexes:
            if (vertexes[key][0] < x2 < vertexes[key][2]) == True:
                vertexDestination = key
        edges[edgeNumber-9] = (vertexStart, vertexDestination)
        edgeNumber += 1
        clickNumber = 0   # We have a line drawn, go back and determine the x1, y1 start coords for the next line)
        letter += 1     # Next letter, eventually goes to lowercase


# Vertex Button
def vertexButtonSet():
    draw_space.unbind("<Button 1>")
    draw_space.tag_bind('vertex', '<Button-1>', addEdge)  # tags used for clicking function, the declared variables in addVertex need the 'vertex' tag

# Edge Finish Button
def edgeButtonSet():
    global adjacencyMatrix
    adjacencyMatrix = [[0] * vertexNumber] * vertexNumber  # Fill adjacency matrix with zeros
    draw_space.unbind("<Button 1>")

# Input button next to entry field for getting weights
def addEdgeWeight():
    #global adjacencyMatrix
    #get user weight from entry using get(), add to adjacencyMatrix using edges{} and vertexes{}
    #draw next to corresponding letter by using edges{} to determine which vertexes, then midpoint of the two vertexes referenced


#def dijkstra():
    #global adjacencyMatrix
    #get two vertexes user wants
    #dijkstra on adjacency matrix
    #show results in pop-up window
    #Throw error if no weight for edge if created

####################
# Window / Widgets #
####################
root = Tk()
root.title("Dijkstra's Canvas - @KyleTimmermans")
draw_space = Canvas(root, width=1500, height=1000, background='white')  # Canvas for drawing, make dynamic sizing in the future
draw_space.pack()

draw_space.bind('<Button-1>', addVertex)  # Bind addVertex to mouse1 to begin program

# Widgets
### We have 10 widgets, they take up first ten ID Numbers, so start vertexNumber at 10
vertexText = Label(text='Input Vertexes by left clicking mouse: ', font=('helvetica', 14))
draw_space.create_window(126, 30, window=vertexText)
vertexButton = Button(text="Done", command=vertexButtonSet)
draw_space.create_window(276, 30, window=vertexButton)
edgeText = Label(text='Input Edges by left clicking the start vertex and then the destination vertex: ', font=('helvetica', 14))
draw_space.create_window(245, 75, window=edgeText)
edgeButton = Button(text="Done", command=edgeButtonSet)
draw_space.create_window(510, 75, window=edgeButton)
weightText = Label(text='Input the weights of edges between nodes e.g. A,B=5', font=('helvetica', 14))
draw_space.create_window(178, 120, window=weightText)
weightEntry = Entry(root)
draw_space.create_window(462, 120, window=weightEntry)
weightInput = Button(text="Input")
draw_space.create_window(592, 120, window=weightInput)
shortpathText = Label(text="Enter the two vertexes for the shortest path you want e.g. v2,v4", font=('helvetica', 14))
draw_space.create_window(210, 165, window=shortpathText)
shortpathEntry = Entry(root)
draw_space.create_window(521, 165, window=shortpathEntry)
shortpathButton = Button(text="Show Result")
draw_space.create_window(671, 165, window=shortpathButton)

root.mainloop()  # Keep window open and loop all its functions

###########
# Testing #
###########
print(vertexes)  # Testing purposes, storing vertex locations
print(edges)     # Testing purposes, storing edges and where they start/end
