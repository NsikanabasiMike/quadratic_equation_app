import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import os

st.set_page_config(page_title='Quadratic Equation Solver With Graph', layout="wide")


st.markdown(
    "<h1 style='text-align: center;'>Quadratic Equation Solver</h1>",
    unsafe_allow_html=True
)
# st.title('Quadratic Equation Solver')

# Quadratic equation solution function
def quadratic_solution(a, b, c):
    '''
    Provide roots to a quadratic equation based on given inputs.
    
    Attributes: 
        a: coefficient of 2nd powered term
        b: coefficient of 1st powered term
        c: constant
    Returns:
        result
        plot (fig)

    '''

    lower_x = -20
    upper_x = 20
    if a == 0:
        return f'Variable _a_ cannot be zero', None

    fig, ax = plt.subplots(figsize = (5, 3))

    # Discriminant
    d = (b)**2 - (4 * a * c)

    if d < 0: 
        x_values = np.linspace(lower_x, upper_x, 400)
        y_values = a * x_values * x_values + b * x_values + c
        ax.plot(x_values, y_values)

        ax.set_xlabel("x values")
        ax.set_ylabel("y values")
        ax.set_title('No Real Solution')
        return f'Sorry, no solution', fig
    
    if d==0:
        single_root = round((-b) / (2 * a), 2)

        lower_x = int(single_root + lower_x)
        upper_x = int(single_root + upper_x)

        x_values = np.linspace(lower_x, upper_x, 400)
        y_values = a * x_values * x_values + b * x_values + c
        ax.plot(x_values, y_values)

        # Plot for a single root
        ax.plot(single_root,  0, marker = 'o', color = 'r')
        ax.text(single_root, 0, f"({single_root:.2f})", color='red', fontsize=8, ha='right', va='top')
        ax.set_title('Equation with one solution')
        return f'Solution to the equation: {single_root}', fig

    d1 = d**(1/2)
    root_1 = round((-b + d1)/ (2 * a), 2)
    root_2 = round((-b - d1)/ (2 * a), 2)
    roots = sorted([root_1, root_2])
    alignment = ['right', 'left' ]

    lower_x = int(roots[0] + lower_x)
    upper_x = int(roots[1] + upper_x)
    x_values = np.linspace(lower_x, upper_x, 400)
    y_values = a * x_values * x_values + b * x_values + c
    ax.plot(x_values, y_values)

    # Plot for two roots
    for idx in range(len(roots)):
        ax.plot(roots[idx],  0, marker = 'o', color = 'r')
        ax.text(roots[idx], 0, f"({roots[idx]:.2f})", color='red', fontsize=8, ha=alignment[idx], va='top')

    ax.set_title('Equation with two solutions')
    return f'Solutions to the equation are: {roots[0]} and {roots[1]}', fig

# Columns
col1, col2, col3 = st.columns([1.5, 0.20, 1])

# User data function
def user_data():
    '''
        Supply user inputs for a quadratic equation.
        
        Attributes: 
            None
        Returns:
            a: coefficient of 2nd powered term
            b: coefficient of 1st powered term
            c: constant
    '''

    with col1:
        col1.subheader('Input Data')
        with st.form(key = 'form info', enter_to_submit = False, clear_on_submit = False):
            
            a = st.number_input('Constant of 2nd powered term ($ax^2$)  : ', value = 1, step = 1)
            b = st.number_input('Constant of 1st powered term (bx): ', value = 0, step = 1)
            c = st.number_input('Constant (c) or bias: ', value = 0, step = 1)
            submit = st.form_submit_button()


    return a, b, c

# user_data execution block
a, b, c = user_data()

# Write in column 3
with col3:

    with st.expander('Quadratic Equation App Details and Usage'):
        st.image(os.path.join(os.getcwd(), 'static', 'IMG-20251222-WA0004.jpg'), width = 200)
        st.write('''
            📈 Solve and visualize quadratic equations with ease! 📊

            Quadratic Equations Web App lets you input the coefficients (a, b, c) and:
            - View the graph of the equation
            - Get the roots (real and complex)
            - Understand quadratic equation concepts better
            - Perfect for students, teachers, and math enthusiasts!

            *Why use it?*:
            - Instant graph visualization 📊
            - Step-by-step understanding of solutions
            - Handy tool for math practice & exams

            FREE to download, with occasional ads to support the app.

            ''')

# quadratic_solution execution block
col3.subheader('Result')
result, plot = quadratic_solution(a, b, c)

with col3:
    if plot is not None:
        st.pyplot(plot)
        col3.markdown(f'**{result}**')
    else:
        col3.markdown(f'**{result}**')
