## Table of Contents
- [Installation](#install)
- [About the Project](#about_project)
- [File Description](#describe)
- [Instructions on How to Run the Files](#Instructions)

<a id='install'></a>
### Installation
Softwares and libraries needed for replicating and smooth running of this app are listed in __requirements.txt__

<a id='about_project'></a>
### About the Project

This Streamlit Web App displays the graphical solution to quadratic equations based on the user's inputs.
It works on the function: $y = ax^2 + bx + c$.<br>
Variables a, b, and c are constants. 
a = constant of second powered term $x^2$,
b = constant of first powered term $bx$
A quadratic equation has a solution when y = 0.<br>

If a = 0, the algorith returns: _Constant of second powered term cannot be zero_ 
Else, it plots a line graph showing the solution to the equation if any.<br> 

<a id='describe'></a>
### File Descriptions
There are two files: `quadratic_equation_app.py` and `requirements.txt`
`quadratic_equation_app.py` contains the code for the app. 
`requirements.txt` contains the following main libraries necessary for running this app:
_matplotlib==3.10.6_, _numpy==1.26.4_, _pandas==2.3.3_ and _streamlit==1.50.0_<br>

<a id='Instructions'></a>
### Instructions on How to Run the App:
One way is:
1.  Open your terminal
2.  Navigate to the root directory of the project files
3.  Activate your environment
4.  Enter the following line to run the app: `streamlit run quadratic_equation_app.py`