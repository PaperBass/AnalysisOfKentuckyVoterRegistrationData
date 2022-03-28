# Analysis of Kentucky Voter Registration Data


## Description

Hello!

This program is designed to visualize voter registration data for the US state Kentucky as of February 15, 2022 (more recent data may be available online at https://elect.ky.gov/Resources/Pages/Registration-Statistics.aspx). When ran, the program displays a list of all the counties in Kentucky. The user is then prompted to enter the desired counties to examine. The user input is not case sensitive and multiple counties can be listed in a single line, so long as the counties are separated by a space (e.g. Jefferson Lee Trigg). Entering the character "C" will complete the list of counties and tell the program to continue. A list of demographic options is displayed and again the user is prompted to select their choices for examination. Once completed, the program will create a bar graph displaying demographic totals for the selected counties. The user can press "enter/return" to continue to repeat the program. At any point, the user can enter "q" to quit the program.

----------------------------------------------------------------------------------------------------

## Packages

The packages needed for this progam are listed below and can be found in the requirements.txt file:

cycler==0.11.0
fonttools==4.31.2
kiwisolver==1.4.1
matplotlib==3.5.1
numpy==1.22.3
packaging==21.3
pandas==1.4.1
Pillow==9.0.1
pyparsing==3.0.7
python-dateutil==2.8.2
pytz==2022.1
six==1.16.0
xlrd==2.0.1

----------------------------------------------------------------------------------------------------

## How to run

To run this progam in the Mac Terminal, first enter the program folder from the directory.

Then create a virtual environment by entering "python -m venv venv" from the command line.

Then enter "source venv/bin/activate".

Once the virtual environment is created, you can enter "pip install -r requirements.txt" in your shell to download the necessary packages.

After the necessary packages have been installed in your virtual environment, enter "python main.py" to run the program.

----------------------------------------------------------------------------------------------------

## Features used

### From Category 1: Python Programming Basics:

#### Found in line 87 of main.py
1. Implement a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program.

#### Found in lines 84, 30, 46, 60, 68 of main.py
2. Create and call at least 3 functions or methods, at least one of which must return a value that is used somewhere else in your code. To clarify, at least one function should be called in your code, that function should calculate, retrieve, or otherwise set the value of a variable or data structure, return a value to where it was called, and use that value somewhere else in your code. For example, you could create a function that reads how many items there are in a text file, returns that value, and later uses that value to execute a loop a certain number of times.

### From Category 2: Utilize External Data:

#### Found in line 21 of main.py
3. Read data from an external file, such as text, JSON, CSV, etc, and use that data in your application.

### From Category 3: Data Display:

#### Defined at line 68, called at line 37 of main.py
4. Visualize data in a graph, chart, or other visual representation of data.

#### Found in line 36 of main.py
5. Display data in tabular form

### From Category 4: Best Practices:

#### Found in lines 36-38 of README.md // requirements.txt is included in program folder
6. The program should utilize a virtual environment and document library dependencies in a requirements.txt file.