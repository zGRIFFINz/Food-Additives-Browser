import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

# Colors
backCol = '#cec097'
labCol = '#f0e9d7'

# Window size and position relative to screen.
window = tk.Tk()
window_width = 1000
window_height = 400
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
window.configure(bg = backCol)

# title_bar = Frame(window, bg='#858585', relief="raised", bd=0)
# title_bar.pack()

window.resizable(True, True)
window.title('FDA Substances Added to Food Browser')

# Opens dataframe from file location. Only works after opened and saved.
df = pd.read_csv (r'FoodSubstances.csv', skiprows = 4)

# Redefines dataframe as pertinent rows and columns.
selection = df.loc[0:, ['Substance', 'Used for (Technical Effect)']]

# Input and output variabes.
inp = StringVar()
resp = StringVar()
outp1 = StringVar()
outp2 = StringVar()
q = 0

# Prompts user.
resp.set('Please enter compound name.')

# Progress to follow up question.
def query():

    global q
    q += 1

# This function better organizes the string variables response, output 1, and output 2 for each instance 
# of the query as well as applies string outputs into text widgets.
def strVars(x, y, z):
    resp.set(x),
    outp1.set(y),
    outp2.set(z)
    
    for a, b in zip([output1, output2], [outp1, outp2]):
        a.configure(state = NORMAL)
        a.delete('1.0', END)
        a.insert(END, b.get(), 'tag_center')
        a.configure(state = 'disabled')
        a.tag_configure('tag_center', justify = LEFT)

def error():
    messagebox.showinfo('*ERROR*', 'Please enter a compound name.')

# Define funtion for matching user inputs with dataframe elements.
def FoodAdditives():

    global q

    # Dataframe element the user wants to search datafase for.
    compoundName = inp.get()
    
    # Searches dataframe for instances of compoundName input and represents them as boolean. Target finds
    # rows presenting "True".
    result = selection['Substance'].str.contains(compoundName, case = False)
    rows = list(result[result == True].index)
    target = selection.iloc[rows]

    # Displays error box when search is empty.
    if len(compoundName) == 0:
        error()
    
    # Displays list of matches containing initial compound name and asks for further specification.
    elif len(rows) > 1 and q == 0:

        # Lists matches in target that contain compoundName without indexes.
        (x, y, z) = [
            'There are multiple results.\nCan you be more specific?',
            target['Substance'].to_string(index=False).title(),
            ''
        ]
        strVars(x, y, z)

        query()

    # Finds the shortest match that includes initial and second compound name.
    elif len(rows) > 1 and q == 1:

        # Asks user for specific input beyond initial query. The output is either a specific compound or a
        # compound with the shortest string length containing second compundName input.
        result = selection['Substance'].str.contains(compoundName, case = False)
        rows = list(result[result == True].index)
        target = selection.iloc[rows]

        # Sorts target by string length.
        shortestTarget = min(target.iloc[0:, 0], key=len)

        # Retrieves index of shortestTarget in target and finds element row in selection dataframe.
        final = int(selection[selection['Substance'] == shortestTarget].index.values)
        substance = selection.iloc[final, 0:].apply(str).values

        (x, y, z) = [
            '',
            str(substance[0]).title(),
            str(substance[1]).title()
        ]
        strVars(x, y, z)
        
        # Resets function to initial question.
        q = 0

    # Notifies when there are no matches for user's query.
    elif len(rows) < 1:

        # Displays no results.
        (x, y, z) = [
            'There are no results that match \nyour entry.',
            '',
            ''
        ]
        strVars(x, y, z)

    # Outputs match of compound name when there is only 1 match whether exact or similar.
    else:

        # Prints match if initial query is an exact match.
        target = target.iloc[0, :].apply(str).values

        (x, y, z) = [
            '',
            str(target[0]).title(),
            str(target[1]).title()
        ]
        strVars(x, y, z)
        
# Window widgets and features.
Label(
    window,
    text = 'Food Additives',
    font = ('sans-sarif', 20),
    relief = SOLID,
    padx = 10,
    pady = 10,
    bg = labCol
).place(relx = 0.05, rely = 0.12)

Entry(
    window,
    textvariable = inp,
    bg = labCol,
    font = ('sans-sarif', 18)
).place(relx = 0.015, rely = 0.3)

Label(
    window,
    textvariable = resp,
    bg = backCol,
    font = ('sans-sarif', 14)
).place(relx = 0.015, rely = 0.4)

output1 = Text(bg = labCol, wrap = WORD)
output2 = Text(bg = labCol, wrap = WORD)

output1.place(x = 300, y = 20, height = 200, width = 250)
output2.place(x = 600, y = 20, height = 200, width = 350)

Button(
    window,
    text = 'Search',
    bg = labCol,
    font = ('sans-sarif', 18),
    command = FoodAdditives
).place(relx = 0.095, rely = 0.56)

window.mainloop()

# To Do

# Handle NAN values
# Find most recent update
# Improve text positioning in boxes
# Improve text box locations
# Scroll bar
# Remove <B/> from output text
# PubChemPy for pulling chemical info
# Print CAS no.
# Generate link?

#hex colors
#title  #3f3f3f
#bg     #858585
#label  #d5d5d5
#entry  #d5d5d5
#text   #d5d5d5
