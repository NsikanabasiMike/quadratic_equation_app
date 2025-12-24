import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title='Essiet Quadratic App')
st.title('Quadratic Equation App')


# Quadratic equation solution fuction
def quadratic_solution(a, b, c, lower_x, upper_x):
    '''
    Provide roots to a quadratic equation based on given inputs.
    
    Attributes: 
        a: coefficient of 2nd powered term
        b: coefficient of 1st powered term
        c: constant
    Returns:
        result
        plot (fig)
        dataframe (df)

    '''
    if a == 0:
        return f'Variable a cannot be zero'

        
    x_values = np.linspace(lower_x, upper_x, 40)
    y_values = a * x_values * x_values + b * x_values + c

    # Dataframe
    df = pd.DataFrame({'x': x_values, 'y': y_values})

    df = df.T   # ---Dataframe transposed
    fig, ax = plt.subplots(figsize = (5, 3))
    ax.plot(x_values, y_values)
    ax.set_xlabel("x values")
    ax.set_ylabel("y values")

    # Discriminant
    d = (b)**2 - (4 * a * c)
    if d < 0:
        ax.set_title('No Real Solution')
        return f'Sorry, no solution', fig, df
    
    if d==0:
        single_root = round((-b) / (2 * a), 2)
        ax.plot(single_root,  0, marker = 'o', color = 'r')

        # Plot for a single root
        ax.text(single_root, 0, f"({single_root:.2f})", color='red', fontsize=8, ha='right', va='top')
        ax.set_title('Equation with one solution')
        return f'Solution to the equation: {single_root}', fig, df

    d1 = d**(1/2)
    root_1 = round((-b + d1)/ (2 * a), 2)
    root_2 = round((-b - d1)/ (2 * a), 2)
    roots = sorted([root_1, root_2])
    alignment = ['right', 'left' ]

    # Plot for two roots
    for idx in range(len(roots)):
        ax.plot(roots[idx],  0, marker = 'o', color = 'r')
        ax.text(roots[idx], 0, f"({roots[idx]:.2f})", color='red', fontsize=8, ha=alignment[idx], va='top')

    ax.set_title('Equation with two solutions')
    return f'Solutions to the equation are: {roots[0]} and {roots[1]}', fig, df

st.sidebar.header('User Data')

# Sidebar block function
def user_data():
    '''
        Supply user inputs for a quadratic equation.
        
        Attributes: 
            None
        Returns:
            a: coefficient of 2nd powered term
            b: coefficient of 1st powered term
            c: constant
            lower_x: min range of x
            upper_x: max range of x

    '''
    a = st.sidebar.slider('Constant of 2nd powered term ($ax^2$)  : ', -100, 100, 1)
    b = st.sidebar.slider('Constant of 1st powered term (bx): ', -100, 100, 1)
    c = st.sidebar.slider('Constant (c) or bias: ', -100, 100, 1)
    lower_x = st.sidebar.slider('Min. range of x:', -300, 0, -10, 1)
    upper_x = st.sidebar.slider('Max. range of x:', 0, 300, 10, 1)

    return a, b, c, lower_x, upper_x

# user_data execution block
a, b, c, lower_x, upper_x = user_data()


# Columns
col1, col2, col3 = st.columns([1.5, 0.20, 1])

# Write in column 3
with col3:

    with st.expander('Quadratic Equation App Details and Usage'):
        st.write('''

            This App displays the graphical solution to quadratic equations based on the user's inputs.
            It works on the function: $y = ax^2 + bx + c$.
            Variables a, b, and c are constants. a = constant of second powered term $x^2$,
            b = constant of first powered term $bx$
            A quadratic equation has a solution when y = 0.

            This app is dynamic. To use it, simply adjust the parameters on the side bar :blue[👈].
            Parameters like **_Min. range of x_** and **_Max. range of x_** control the range of x and can be adjusted to fit the line to the roots if not fitted properly.

            Enjoy the app :blue[👍]

            ''')

# quadratic_solution execution block
col1.subheader('Result')
try:
    result, plot, df = quadratic_solution(a, b, c, lower_x, upper_x)
    if plot is not None:
        with col1:
            st.pyplot(plot)
            st.markdown(f'**{result}**')

        with col3:
            st.divider()
            st.markdown('**Table of values**')
            st.dataframe(df)
except ValueError:
    col1.write('_Constant of second powered term cannot be zero_')