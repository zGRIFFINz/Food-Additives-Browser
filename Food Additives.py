
import pandas as pd
import tkinter
from tkinter import *
from tkinter import messagebox

# Handles error box.
#def searchCallBack():
    #messagebox.showinfo('Food Additives DB', 'Please search')

# Window size and position relative to screen.
window = tkinter.Tk()
window_width = 1000
window_height = 400
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
#window.resizable(False, False)
window.title('Common Food Additives Browser')

# Opens dataframe from file location.
#df = pd.read_csv (r'C:\Users\griff\OneDrive\Documents\Databases\FoodSubstances.csv')
df = pd.read_csv (r'FoodSubstances.csv')

# Redefines dataframe as pertinent rows and columns.
selection = df.loc[0:, ['Substance', 'Used for (Technical Effect)']]

# Input and output variabes.
inp = StringVar()
outp1 = StringVar()
outp2 = StringVar()
resp = StringVar()
msg = ''

# Query for user.
resp.set('Please enter compound name.')



# Define funtion for matching user inputs with dataframe elements.
def FoodAdditives():

    global msg

    # Dataframe element the user wants to search datafase for.
    compoundName = inp.get()
    
    # Searches dataframe for instances of compoundName input and represents them as boolean. Target finds
    # rows presenting "True".
    result = selection['Substance'].str.contains(compoundName, case = False)
    rows = list(result[result == True].index)
    target = selection.iloc[rows]
    
    # Differentiates between a complete match of input compoundName and a list of strings containing
    # input compoundName.
    if len(rows) > 1:

        # Lists matches in target that contain compoundName without indexes.
        suggest = target['Substance'].to_string(index = False)
        print(suggest)
        msg = 'There are multiple results.\nCan you be more specific?'

        outp1.set(suggest)
        resp.set(msg)
        # inp.set('')

        # Asks user for specific input beyond initial query. The output is either a specific compound or a
        # compound with the shortest string length containing second compundName input.
        result = selection['Substance'].str.contains(compoundName, case = False)
        rows = list(result[result == True].index)
        target = selection.iloc[rows]

        # Sorts target by string length.
        shortestTarget = min(target.iloc[0:, 0], key = len)

        # Retrieves index of shortestTarget in target and finds element row in selection dataframe.
        final = int(selection[selection['Substance'] == shortestTarget].index.values)
        #print(selection.loc[[final], ['Substance', 'Used for (Technical Effect)']])
        substance = selection.loc[[final], ['Substance', 'Used for (Technical Effect)']]

        outp1.set(substance)
        print(substance)

        # def check_empty():

        #     compoundName2 = inp.get()

        #     if inp.get():
        #         print('Okay')
        #         print('hey')
        #         # Asks user for specific input beyond initial query. The output is either a specific compound or a
        #         # compound with the shortest string length containing second compundName input.
        #         result = selection['Substance'].str.contains(compoundName2, case = False)
        #         rows = list(result[result == True].index)
        #         target = selection.iloc[rows]

        #         # Sorts target by string length.
        #         shortestTarget = min(target.iloc[0:, 0], key = len)

        #         # Retrieves index of shortestTarget in target and finds element row in selection dataframe.
        #         final = int(selection[selection['Substance'] == shortestTarget].index.values)
        #         #print(selection.loc[[final], ['Substance', 'Used for (Technical Effect)']])
        #         substance = selection.loc[[final], ['Substance', 'Used for (Technical Effect)']]

        #         outp1.set(substance)
        #         print(substance)
            
        #     else:
        #         print('Woops')

        #         check_empty()   
        
        # if len(compoundName) > 1:

        # def FoodAdditives2():

        #     # Asks user for specific input beyond initial query. The output is either a specific compound or a
        #     # compound with the shortest string length containing second compundName input.
        #     result = selection['Substance'].str.contains(compoundName, case = False)
        #     rows = list(result[result == True].index)
        #     target = selection.iloc[rows]

        #     # Sorts target by string length.
        #     shortestTarget = min(target.iloc[0:, 0], key = len)

        #     # Retrieves index of shortestTarget in target and finds element row in selection dataframe.
        #     final = int(selection[selection['Substance'] == shortestTarget].index.values)
        #     print(selection.loc[[final], ['Substance', 'Used for (Technical Effect)']])
        #     substance = selection.loc[[final], ['Substance', 'Used for (Technical Effect)']]

    elif len(rows) < 1:

        msg = 'There are no results that match your entry.'
        substance = ''

    else:

        # Prints match if initial query is an exact match.
        target = target.iloc[0, :].apply(str).values
        print(str(target[0] + target[1]))
        substance = str(target[0])
        usedFor = str(target[1])

        outp1.set(substance)
        outp2.set(usedFor)

# Window widgets and features.
Label(
    window,
    text = 'Food Additives',
    font = ('sans-sarif', 20),
    relief = SOLID,
    padx = 10,
    pady = 10,
    bg = '#FFF'
).place(relx = 0.05, rely = 0.12)

Entry(
    window,
    textvariable = inp,
    font = ('sans-sarif', 18)
).place(relx = 0.015, rely = 0.3)

Label(
    window,
    textvariable = resp,
    bg = '#FFF',
    font = ('sans-sarif', 14)
).place(relx = 0.015, rely = 0.4)

Label(
    window,
    textvariable = outp1,
    bg = '#FFF',
    #padx = 100,
    #pady = 100,
    font = ('sans-sarif', 14)
).place(x = 300, y = 20)

Label(
    window,
    textvariable = outp2,
    bg = '#FFF',
    #padx = 100,
    #pady = 100,
    font = ('sans-sarif', 14)
).place(x = 600, y = 20)

Button(
    window,
    text = 'Search',
    font = ('sans-sarif', 18),
    command = FoodAdditives
).place(relx = 0.095, rely = 0.5)

window.mainloop()



#matching = df['col2'].str.contains('substr', case=True, regex=False).head(n)
#and:

#matching = df['col2'].str.contains('substr', case=True, regex=False).sample(n)



#compoundName = input('\nThere are multiple results.\n\n' + suggest + '\n\nCan you be more specific?\n\n')

    #listOfPos = List()
   #seriesObj = result.any()

    #columnNames = list(seriesObj[seriesObj == True].index)

    #print(targetCompound['Substance'].str.contains('True'))

    #search_result = df.isin([compoundName]).any()
    #print (search_result)
    #results = selection.isin([compoundName])
    #print(results)
    #df.target(selection == compoundName)
#print(selection == ' ACETAL')
#print(selection[selection == ' ACETAL'])
#print(selection)
    #series = targetCompound.any()
    #print(series)
    #print(seriesTarget)
    #print (selection.str.contains(compoundName))
#if compoundName == "no":
#print("well okay")

#target['strLen'] = target['Substance'].apply(len)
        #shortestTarget = target.loc[:,['strLen']]
        #shortestTarget.sort_values('strLen')
        #shortestTarget = target['strLen']
        #print(shortestTarget)

