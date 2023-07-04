import streamlit as st
import math


st.set_page_config(page_title='MathProdigy Calculator', page_icon='calc.png', layout="centered", initial_sidebar_state="auto", menu_items=None)

def bmi():
    def calculate_bmi(weight, height):
        bmi = weight / (height ** 2)
        return bmi

    st.markdown(
        "<center><h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>BMI Calculator</h1></center>",
        unsafe_allow_html=True)

    weight = st.number_input("Enter your weight (in kg)")
    height = st.number_input("Enter your height (in meters)")

    calculate_button = st.button("Calculate BMI")

    if calculate_button:
        if weight > 0 and height > 0:
            bmi = calculate_bmi(weight, height)
            st.success(f"Your BMI is: **{bmi:.2f}**")
        else:
            st.warning("Please enter valid weight and height values.")


def nCal():
    st.markdown(
        "<center><h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>Normal Calculator</h1></center>",
        unsafe_allow_html=True)

    num1 = st.number_input("Enter the first number")
    num2 = st.number_input("Enter the second number")

    operation = st.selectbox("Select an operation", ["+", "-", "*", "/", "%"])

    calculate_button = st.button("Calculate")

    if calculate_button:
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                st.warning("Cannot divide by zero.")
                result = None
        elif operation == "%":
            result = (num1 * num2) / 100

        if result is not None:
            st.success(f"Result: **{result}**")


def sCal():
    st.markdown(
        "<center><h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>Scientific Calculator</h1></center>",
        unsafe_allow_html=True)

    num1 = st.number_input("Enter the number")

    operation = st.selectbox("Select an operation", ["sqrt", "sin", "cos", "tan"])

    calculate_button = st.button("Calculate")

    if calculate_button:
        if operation == "sqrt":
            result = math.sqrt(num1)
        elif operation == "sin":
            result = math.sin(num1)
        elif operation == "cos":
            result = math.cos(num1)
        elif operation == "tan":
            result = math.tan(num1)

        formatted_result = "{:.2f}".format(result)
        st.success(f"Result: **{formatted_result}**")





def main():
    st.sidebar.markdown("""
            <style>
                .sidebar-text {
                    text-align: center;
                    font-size: 32px;
                    font-weight: bold;
                    font-family: Comic Sans MS;
                }
            </style>
            <p class="sidebar-text">Calculator</p>
        """, unsafe_allow_html=True)
    st.sidebar.image(
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQXQ6TjjZlNL1X6yug3xJcOzMNx2K2hByEH9g&usqp=CAU",
        use_column_width=True)
    st.sidebar.markdown("<h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 24px;'>MathProdigy "
                "Calculator</h1></center>", unsafe_allow_html=True)
    selected_sidebar = st.sidebar.radio("Please Select One", ["BMI Calculator", "Normal Calculator","Scientific Calculator"])

    if selected_sidebar == "BMI Calculator":
        bmi()
    elif selected_sidebar == "Normal Calculator":
        nCal()
    elif selected_sidebar == "Scientific Calculator":
        sCal()


if __name__ == "__main__":
    main()
