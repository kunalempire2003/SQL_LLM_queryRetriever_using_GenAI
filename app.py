from dotenv import load_dotenv
load_dotenv()


import streamlit as st
import os
import sqlite3


import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#function to load gemini model
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

#function to retrieve 
def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows    

#DEFINING PROMPT
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENTS and has the following columns - NAME, CLASS, 
    SECTION \n\nFor example, \nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENTS; 
    \nExample 2 -What are the names of all students?,
    The SQL command will be something like this SELECT NAME FROM STUDENTS;
    \nExample 3 - How many students are in section 'A'?,
    The SQL command will be something like this SELECT COUNT(*) FROM STUDENTS WHERE SECTION = 'A';
    \nExample 4 - Show all the details of students in the 'IT' class.,
    The SQL command will be something like this SELECT * FROM STUDENTS WHERE CLASS = 'IT';
    \nExample 5 - What are the sections available without duplicates?,
    The SQL command will be something like this SELECT DISTINCT SECTION FROM STUDENTS;
    \nExample 6 - Find all students whose names start with 'A'.,
    The SQL command will be something like this SELECT * FROM STUDENTS WHERE NAME LIKE 'A%';
    \nExample 7 - Retrieve all information about students sorted by class in descending order.,
    The SQL command will be something like this SELECT * FROM STUDENTS ORDER BY CLASS DESC;
    \nExample 8 - List all students in section 'B' with their names and classes.,
    The SQL command will be something like this SELECT NAME, CLASS FROM STUDENTS WHERE SECTION = 'B';
    \nExample 9 - Count the number of students in 'computer engineering'.,
    The SQL command will be something like this SELECT COUNT(*) FROM STUDENTS WHERE CLASS = 'computer engineering';
    \nExample 10 - Find students who are not in section 'A'.,
    The SQL command will be something like this SELECT * FROM STUDENTS WHERE SECTION != 'A';
    \nExample 11 - Display students' names and sections where the class contains 'Data'.,
    The SQL command will be something like this SELECT NAME, SECTION FROM STUDENTS WHERE CLASS LIKE '%Data%';
    also the sql code should not have ``` in beginning or end and sql word in output 
     
    """
]

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.markdown(
    """
    <style>
    .main{
        background-color: black;
        color: white;
    }
  
    </style>
    """,
    unsafe_allow_html=True
)
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

if submit:
    # Assuming get_gemini_response is defined somewhere and returns the prompt's response
    response = get_gemini_response(question, prompt)
    print(response)
    
    # Assuming read_sql_query takes the response and returns the result of a SQL query
    response_data = read_sql_query(response, "STUDENTS.db")
    
    if response_data:  # Check if there is data returned
        st.subheader("The Response is")
        
        # Displaying each row in a formatted way
        for row in response_data:
            # You may want to display specific columns or format the row better
            print(row)
            st.write(row)  # Use st.write instead of st.header for better formatting
        
    else:
        st.write("No data returned for this query.")

