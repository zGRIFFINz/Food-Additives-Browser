# Food-Additives-Browser


**This project is a work in progress. In its current state, it contains all features initially planned for it but I want to expand its features as I become more familiar with using Pandas and TKinter.**


Description:

Many processed food packages contain long lists of confusing chemical names as food additives which are not immediately evident what their use is. This is a simple program with a GUI that searches 'FoodSubstances.csv' file from 'Substances Added to Food' FDA inventory (https://www.cfsanappsexternal.fda.gov/scripts/fdcc/index.cfm?set=FoodSubstances&amp;sort=Used_for_Technical_Effect&amp;order=ASC&amp;type=basic&amp;search=) for common unintuitive ingredients you may find on food packaging. The browser will return a single result ingredient/compound and uses if an exact match is entered or will return a suggested list if the search has multiple results. The follow up search will return info on the shortest-named ingredient containing the searched text and its uses.


Installation:

Download both files and place them in the same folder/direcotry. This code is not yet available as an executable and requires a python code interpreter to function (*most IDEs are able to write and run or 'interpret' code). This program will only run a file named 'FoodSubstances.csv' unless you change the target path in the code.
