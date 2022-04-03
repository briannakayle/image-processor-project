# Image Processer
# Starter code for main.py
# Author(s): _______ & Brianna Espena
# Date: December 7, 2020
# Description: Interactive image processer with multiple manipulation levels

import cmpt120imageProj
import cmpt120imageManip
import tkinter.filedialog
import pygame
pygame.init()


# list of system options
system = [
            "Q: Quit",
            "O: Open image",
            "R: Reload image",
            "S: Save image"
         ]

# list of basic operation options
basic = [
          "1: Switch to Intermediate Functions",
          "2: Switch to Advanced Functions"
         ]

# list of intermediate operation options
intermediate = [
                  "1: Switch to Basic Functions",
                  "2: Switch to Advanced Functions"
                 ]

# list of advanced operation options
advanced = [
                "1: Switch to Basic Functions",
                "2: Switch to Intermediate Functions"
             ]

# a helper function that generates a list of strings to be displayed in the interface
def generateMenu(state):
    """
    Input:  state - a dictionary containing the state values of the application
    Returns: a list of strings, each element represets a line in the interface
    """
    menuString = ["Welcome to CMPT 120 Image Processer!"]
    menuString.append("") # an empty line
    menuString.append("Choose the following options:")
    menuString.append("") # an empty line
    menuString += system
    menuString.append("") # an empty line

    # build the list differently depending on the mode attribute
    if state["mode"] == "basic":
        menuString.append("--Basic Mode--")
        menuString += basic
        menuString.append("3. Invert the image")
        menuString.append("4. Flip Horizontal")
        menuString.append("5. Flip Vertical")

    elif state["mode"] == "intermediate":
        menuString.append("--Intermediate Mode--")
        menuString += intermediate
        menuString.append("3. Remove Red Channel")
        menuString.append("4. Remove Green Channel")
        menuString.append("5. Remvove Blue Channel")
        menuString.append("6. Convert to Grayscale")
        menuString.append("7. Apply Sepia Filter")
        menuString.append("8. Decrease Brightness")
        menuString.append("9. Increase Brightness")

    elif state["mode"] == "advanced":
        menuString.append("--Advanced Mode--")
        menuString += advanced
        menuString.append("3. Rotate Left")
        menuString.append("4. Rotate Right")
        menuString.append("5. Pixelate")
        menuString.append("6. Binarize")

    else:
        menuString.append("Error: Unknown mode!")

    return menuString

# a helper function that returns the result image as a result of the operation chosen by the user
# it also updates the state values when necessary (e.g, the mode attribute if the user switches mode)
def handleUserInput(state, pixels):
    """
        Input:  state - a dictionary containing the state values of the application
                pixels - the 2d array of RGB values to be operated on
        Returns: the 2d array of RGB vales of the result image of an operation chosen by the user
    """
    userInput = state["lastUserInput"].upper()
    # handle the system functionalities
    if userInput.isalpha(): # check if the input is an alphabet
        print("Log: Doing system functionalities " + userInput)
        if userInput == "Q":
            print("Log: Quitting...")
        elif userInput == "O":
            # brianna here
            
            #tkinter.Tk().withdraw()
            #openFilename = tkinter.filedialog.askopenfilename()
            pixels = cmpt120imageProj.getImage('project-photo.jpg')

            #brianna here
            cmpt120imageProj.showInterface(pixels, "Image", generateMenu(appStateValues))
            #appStateValues["lastOpenFilename"] = openFilename
            appStateValues["lastOpenFilename"] = pixels
        elif userInput == "R":
            pixels = cmpt120imageProj.getImage(appStateValues["lastOpenFilename"])
            cmpt120imageProj.showInterface(pixels, "Image", generateMenu(appStateValues))
        elif userInput == "S":
            #tkinter.Tk().withdraw()
            #saveFilename = tkinter.filedialog.asksaveasfilename()
            cmpt120imageProj.saveImage(pixels, saveFilename)
            appStateValues["lastSaveFilename"] = saveFilename
            cmpt120imageProj.showInterface(pixels, "Image", generateMenu(appStateValues))


    # or handle the manipulation functionalities based on which mode the application is in
    elif userInput.isdigit(): # has to be a digit for manipulation options
        print("Log: Doing manipulation functionalities " + userInput)
        if appStateValues["mode"] == "basic":
            if userInput == "1":
                state["mode"] = "intermediate"
                cmpt120imageProj.showInterface(pixels, "Intermediate", generateMenu(appStateValues))
            elif userInput == "2":
                state["mode"] = "advanced"
                cmpt120imageProj.showInterface(pixels, "Advanced", generateMenu(appStateValues))
            elif userInput == "3":
                pixels = cmpt120imageManip.invert(pixels)
                cmpt120imageProj.showInterface(pixels, "Invert", generateMenu(appStateValues))
            elif userInput == "4":
                pixels = cmpt120imageManip.fliphorizontal(pixels)
                cmpt120imageProj.showInterface(pixels, "Flipped Horizental", generateMenu(appStateValues))
            elif userInput == "5":
                pixels = cmpt120imageManip.flipvertical(pixels)
                cmpt120imageProj.showInterface(pixels, "Flipped Vertical", generateMenu(appStateValues))

        elif appStateValues["mode"] == "intermediate":
            if userInput == "1":
                state["mode"] = "basic"
                cmpt120imageProj.showInterface(pixels, "Basic", generateMenu(appStateValues))
            elif userInput == "2":
                state["mode"] = "advanced"
                cmpt120imageProj.showInterface(pixels, "Advanced", generateMenu(appStateValues))
            elif userInput == "3":
                pixels = cmpt120imageManip.removeRed(pixels)
                cmpt120imageProj.showInterface(pixels, "Remove Red", generateMenu(appStateValues))
            elif userInput == "4":
                pixels = cmpt120imageManip.removeGreen(pixels)
                cmpt120imageProj.showInterface(pixels, "Remove Green", generateMenu(appStateValues))
            elif userInput == "5":
                pixels = cmpt120imageManip.removeBlue(pixels)
                cmpt120imageProj.showInterface(pixels, "Remove Blue", generateMenu(appStateValues))
            elif userInput == "6":
                pixels = cmpt120imageManip.grayscale(pixels)
                cmpt120imageProj.showInterface(pixels, "Grayscale", generateMenu(appStateValues))
            elif userInput == "7":
                pixels = cmpt120imageManip.sepia(pixels)
                cmpt120imageProj.showInterface(pixels, "Sepia", generateMenu(appStateValues))
            elif userInput == "8":
                pixels = cmpt120imageManip.dec_brightness(pixels)
                cmpt120imageProj.showInterface(pixels, "Decrease Brightness", generateMenu(appStateValues))
            elif userInput == "9":
                pixels = cmpt120imageManip.inc_brightness(pixels)
                cmpt120imageProj.showInterface(pixels, "Increase Brightness", generateMenu(appStateValues))

        elif appStateValues["mode"] == "advanced":
            if userInput == "1":
                state["mode"] = "basic"
                cmpt120imageProj.showInterface(pixels, "Basic", generateMenu(appStateValues))
            elif userInput == "2":
                state["mode"] = "intermediate"
                cmpt120imageProj.showInterface(pixels, "Intermediate", generateMenu(appStateValues))
            elif userInput == "3":
                pixels = cmpt120imageManip.rotate_L(pixels)
                cmpt120imageProj.showInterface(pixels, "Rotate Left", generateMenu(appStateValues))
            elif userInput == "4":
                pixels = cmpt120imageManip.rotate_R(pixels)
                cmpt120imageProj.showInterface(pixels, "Rotate Right", generateMenu(appStateValues))
            elif userInput == "5":
                pixels = cmpt120imageManip.pixelate(pixels)
                cmpt120imageProj.showInterface(pixels, "Pixelate", generateMenu(appStateValues))
            elif userInput == "6":
                pixels = cmpt120imageManip.binarize(pixels)
                cmpt120imageProj.showInterface(pixels, "Binarize", generateMenu(appStateValues))

    else: # unrecognized user input
            print("Log: Unrecognized user input: " + userInput)
    return pixels


# use a dictionary to remember several state values of the application
appStateValues = {
                    "mode": "basic",
                    "lastOpenFilename": "",
                    "lastSaveFilename": "",
                    "lastUserInput": ""
                 }

currentImg = cmpt120imageProj.createBlackImage(600, 400) # create a default 600 x 400 black image
cmpt120imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues)) # note how it is used

# ***this is the event-loop of the application. Keep the remainder of the code unmodified***
keepRunning = True
# a while-loop getting events from pygame
while keepRunning:
    ### use the pygame event handling system ###
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            appStateValues["lastUserInput"] = pygame.key.name(event.key)
            # prepare to quit the loop if user inputs "q" or "Q"
            if appStateValues["lastUserInput"].upper() == "Q":
                keepRunning = False
            # otherwise let the helper function handle the input
            else:
                currentImg = handleUserInput(appStateValues, currentImg)
        elif event.type == pygame.QUIT: #another way to quit the program is to click the close botton
            keepRunning = False

# shutdown everything from the pygame package
pygame.quit()

print("Log: Program Quit")
