import streamlit as st1
# from PIL import Image
# img = Image.open('gpa.png')
st1.set_page_config(page_title="CalcGPA", page_icon=":smiley:" )
def gpacal(semester):
    theory = {}
    prac = {}
    final_gpa = 0
    warning = 0
    credits = 0
    col1, col2 = st1.columns(2)

    if semester == 1:
        theory = {'App. Maths-I': 4, 'App. Physics-I': 3, 'Manufacturing Processes': 3, 'Electrical Tech.': 3,
                  'Human Values': 1, 'Fundamentals of Computing': 2, 'App. Chemistry': 3}
        prac = {'App. Physics Lab-I': 1, 'Elecrical Tech. Lab': 1, 'Workshop': 2, 'Engg. Graphics Lab': 2, 'FOC Lab': 1,
                'App. Chemistry Lab': 1}
        credits = 27

    elif semester == 2:
        theory = {'App. Maths-II': 4, 'App. Physics-II': 3, 'Electronic Devices': 3, 'Intro To Programming': 3,
                  'Engineering Mechanics': 3, 'Communication Skills': 3, 'Environmental Studies': 3}
        prac = {'App. Physics Lab-II': 1, 'Programming Lab': 1, 'Electronics Lab': 1, 'Engineering Mechanics Lab': 1,
                'EVS Lab': 1}
        credits = 27

    elif semester == 3:
        theory = {'App. Maths-III': 4, 'Foundation of CS': 4, 'Switching Theory & Logic Design': 4,
                  'Circuits & Systems': 4, 'Data Structures': 4, 'Computer Graphics & Multimedia': 4, }
        prac = {'STLD Lab': 1, 'Data Stucture Lab': 1, 'Circuits & Systems Lab': 1, 'CGMM Lab': 1}
        credits = 28

    elif semester == 4:
        theory = {'App. Maths-IV': 4, 'Computer Organisation & Architecture': 4, 'Theory of Computation': 4,
                  'Database Management': 4, 'Object Oriented Programming': 3, 'Control Systems': 4}
        prac = {'App. Maths Lab': 1, 'COA Lab': 1, 'DBMS Lab': 1, 'OOPS Lab': 1, 'Control Systems Lab': 1}
        credits = 28

    elif semester == 5:
        theory = {'Algo. Design & Analysis': 4, 'Software Engineering': 4, 'Java Programming': 4,
                  'Industrial Management': 3, 'Communication Systems': 4, 'Communication Skills': 1}
        prac = {'Algo. Design Lab': 1, 'Software Engineering Lab': 1, 'Java Programming Lab': 1, 'In-house Workshop': 1,
                'Communication Systems Lab': 1, 'Communication Skills Lab': 1}
        credits = 26

    elif semester == 6:
        theory = {'Compiler Design': 4, 'Operating Systems': 4, 'Data Communication & Networks': 4,
                  'Web Engineering': 3, 'Artificial Intelligence': 4, 'Microprocessors & Microcontrollers': 4, }
        prac = {'Operating Systems Lab': 1, 'Networks Lab': 1, 'Web Engineering Lab': 1,
                'Microprocessor & Microcontroller Lab': 1}
        credits = 27

    elif semester == 7:
        theory = {'Advanced Computer Networks ': 4, 'Wireless Communication ': 3,'Cryptography and Network Security ': 3,
                  'Opted Subject from GroupA(1)': 3, 'Opted Subject from GroupB': 3}
        prac = {'Advanced Computer Networks Lab ': 1, 'Cryptography and Network Security Lab ': 1, 'Wireless Communication Lab': 1,
                'Lab based on Elective Group– A or B ': 1 , 'STP':1 , 'Minor Project': 3}
        credits = 24

    elif semester == 8:
        theory = {'Mobile Computing ': 4, 'Ad hoc and Sensor Networks ': 3,'Human Values and Professional Ethics-II': 1,
                  'Opted Subject from GroupA(1)': 3, 'Opted Subject from GroupB': 3}
        prac = {'Mobile Computing Lab  ': 1, 'Ad hoc and Sensor Networks Lab ': 1, 'Lab based on Elective - I ': 1,
                'Lab based on Elective - II ': 1 , 'Major Project': 8}
        credits = 26


    with col1:
        with st1.expander("Theory Subjects"):
            for theory1 in theory:
                marks = st1.number_input("{}:".format(theory1), 0, 100)
                if marks == 0:
                    warning = 1
                num = grades(marks)
                final_gpa += num * theory[theory1]

    with col2:
        with st1.expander("Practical Subjects"):
            for lab in prac:
                marks = st1.number_input("{}:".format(lab), 0, 100)
                if marks == 0:
                    warning = 1
                num = grades(marks)
                final_gpa += num * prac[lab]

    if warning:
        st1.warning("You haven't entered the marks of all subjects!")

    final_gpa = final_gpa / credits
    return final_gpa


def grades(marks):
    if marks >= 90:
        grade = 10
    elif marks >= 75:
        grade = 9
    elif marks >= 65:
        grade = 8
    elif marks >= 55:
        grade = 7
    elif marks >= 50:
        grade = 6
    elif marks >= 45:
        grade = 5
    elif marks >= 40:
        grade = 4
    else:
        grade = 0

    return grade


st1.title("CalcGPA")
st1.subheader("GPA calculator for IT students in IPU")
clientName = st1.text_input("ENTER YOUR NAME:")
if clientName:
    st1.write(f"Hi,{clientName}, Thank You for using CalcGPA")
    clientInst = st1.text_input("COLLEGE NAME:")
    if clientInst:
        semester = st1.slider("SELECT YOUR SEMESTER:", 1 , 8)
        GPA = gpacal(semester)

        submit = st1.button("SUBMIT")

        if submit:
            st1.header(f"YOUR GPA : {round(GPA,2)}")
            if GPA>8:
                st1.balloons()
                st1.snow()
                st1.balloons()
# img = Image.open('gpa.png')



