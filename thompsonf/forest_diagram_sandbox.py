from thompsonf import ThompsonF
import os
import random as Rand
import matplotlib.pyplot as plt
import turtle as tl
import sys

def draw_forest_turtle(forest,pointer,height,upsideDown = False):
    # Top forest: Draw each of the leaves, equally spaced.
    forestList = forest.strip().split(" ")
    allLeaves = forest.count(".")
    for leaf in range(allLeaves):
        tl.goto(25*(leaf-((allLeaves-1)/2)),height)
        tl.dot()
    totalLeafCount = 0
    for treeNum in range(len(forestList)):
        currTree = forestList[treeNum]
        currLeafCount = totalLeafCount + currTree.count(".")
        leafLocs = [(25*(leafNum-((allLeaves-1)/2)), height, (25*(leafNum-((allLeaves-1)/2))), (25*(leafNum-((allLeaves-1)/2)))) for leafNum in range(totalLeafCount,currLeafCount)]
        # From the "bottom up", look for every adjacent pair of leaves.
        # Replace that pair of leaves with a single root. Continue
        # until the whole tree is built, i.e., we have one
        # single root.

        # Each "location" 4-tuple stores four values: the x-location of the root, the y-location of the root,
        # the x-location of the leftmost vertex, and the y-location of the rightmost vertex.
        while len(leafLocs) > 1:
            indexInTree = currTree.find("(.)(.)")
            leafInTree = currTree.count(".",0,indexInTree)
            newLoc = ((leafLocs[leafInTree][2] + leafLocs[leafInTree+1][3])/2, (max(leafLocs[leafInTree][1], leafLocs[leafInTree+1][1])+25) if upsideDown == False else (min(leafLocs[leafInTree][1], leafLocs[leafInTree+1][1])-25), min(leafLocs[leafInTree][2], leafLocs[leafInTree+1][2]), max(leafLocs[leafInTree][3], leafLocs[leafInTree+1][3]))
            firstLoc = leafLocs.pop(leafInTree)
            tl.goto((firstLoc[0], firstLoc[1]))
            tl.pendown()
            tl.goto((newLoc[0],newLoc[1]))
            secondLoc = leafLocs.pop(leafInTree)
            tl.goto(secondLoc[0],secondLoc[1])
            tl.penup()
            leafLocs.insert(leafInTree,newLoc)
            currTree = currTree[:indexInTree] + "." + currTree[indexInTree+6:]
        totalLeafCount = currLeafCount
        if treeNum == pointer:
            tl.goto((leafLocs[0][0],leafLocs[0][1]))
            if upsideDown:
                tl.right(90)
                tl.forward(10)
                tl.down()
                tl.left(45)
                tl.forward(10)
                tl.backward(10)
                tl.right(90)
                tl.forward(10)
                tl.backward(10)
                tl.left(45)
                tl.forward(25)
                tl.left(90)
                tl.up()
            else:
                tl.left(90)
                tl.forward(10)
                tl.down()
                tl.right(45)
                tl.forward(10)
                tl.backward(10)
                tl.left(90)
                tl.forward(10)
                tl.backward(10)
                tl.right(45)
                tl.forward(25)
                tl.right(90)
                tl.up()
    tl.hideturtle()

def draw_forest_diagram(element):
    os.system('cls')
    playerForest = element.forestDiagram()

    wn = tl.Screen()
    tl.clearscreen()
    tl.speed(0)
    tl.penup()

    wn.tracer(0)
    draw_forest_turtle(playerForest[0], playerForest[1], 50)
    draw_forest_turtle(playerForest[2], playerForest[3], -50, True)
    wn.update()

    print("Current element: " + str(element))
    print("Length in x0, x1: " + str(len(element)))
    print("Q: Quit\n" + "L: Move left\n" + "R: Move right\n" + "C: Place caret\n" + "N: Place negative caret")

def main():
    entry = ""
    player = ThompsonF()
    draw_forest_diagram(player)
    while entry != "Q":
        entry = input("Next move: ")
        if entry == "Q":
            sys.exit()
        if entry == "L":
            player *= ThompsonF([0],[-1])
        elif entry == "R":
            player *= ThompsonF([0],[1])
        elif entry == "C":
            player *= ThompsonF([1],[1])
        elif entry == "N":
            player *= ThompsonF([1],[-1])
        draw_forest_diagram(player)
    sys.exit()

if __name__ == '__main__':
    main()