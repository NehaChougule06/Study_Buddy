import streamlit as st
import mysql.connector


def create_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Parasnath1008",
        database="study_buddy",
        port=3306
    )

def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()

def execute_select_query(connection, query):
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

def execute_modify_query(connection, query, data=None):
    cursor = connection.cursor()
    if data:
        cursor.execute(query, data)
    else:
        cursor.execute(query)
    connection.commit()
    cursor.close()

def handle_signup(username, password):
    connection = create_connection()

    # Inserting data into User table
    signup_query = f"INSERT INTO Login (Username, Password) VALUES ('{username}', '{password}')"
    execute_query(connection, signup_query)

    st.success("Sign up successful!")
    connection.close()

def is_admin_logged_in():
    admin_password = "Neha"
    entered_password = st.text_input("Enter Admin Password", type="password")
    
    return entered_password == admin_password
    
def admin():
    st.title("Admin Page")

    if not is_admin_logged_in():
        st.warning("Access denied. Please log in as an admin.")
        return
    
    st.empty()
    
    selected_table = st.selectbox("Select Table", ["Home", "Users", "Class", "Faculty", "Student", "Subject", "Tutor"]) 

    if selected_table == "Home":
        st.write("Welcome to the Admin Page. Select a table from the dropdown to perform CRUD operations.")
    
    elif selected_table == "Users":
        display_Users_table()
        users_operations()

    elif selected_table == "Class":
        display_Class_table()
        Class_operations()
    
    elif selected_table == "Faculty":
        display_Faculty_table()
        Faculty_operations()
    
    elif selected_table == "Student":
        display_Student_table()
        Student_operations()

    elif selected_table == "Subject":
        display_Subject_table()
        Subject_operations()

    elif selected_table == "Tutor":
        display_Tutor_table()
        Tutor_operations()

def display_Users_table():
    connection = create_connection()
    query = "SELECT * FROM Login"
    result = execute_select_query(connection, query)
    st.table(result)
    connection.close()

def add_login(Username, Password):
    connection = create_connection()
    query = f"INSERT INTO Login (Username, Password) VALUES ('{Username}', '{Password}')"
    execute_query(connection, query)
    connection.close()
    st.success("Login added successfully!")

def update_login(Username, new_Password):
    connection = create_connection()
    update_query = f"UPDATE Login SET Password = '{new_Password}' WHERE Username = '{Username}'"
    execute_query(connection, update_query)
    st.success(f"Login for Username {Username} updated successfully!")
    connection.close()

def delete_login(Username):
    connection = create_connection()
    delete_query = f"DELETE FROM Login WHERE Username = '{Username}'"
    execute_query(connection, delete_query)
    st.success(f"Login for Username {Username} deleted successfully!")
    connection.close()

def users_operations():
    st.subheader("User Operations")

    st.subheader("Add New Login")
    new_username = st.text_input("Username")
    new_password = st.text_input("Password", type="password")
    add_button = st.button("Add User", key="add_login")
    if add_button:
        add_login(new_username, new_password)

    st.subheader("Update User")
    update_username = st.text_input("Username to Update")
    update_password = st.text_input("New Password  ", type="password")
    update_button = st.button("Update Login")
    if update_button:
        update_login(update_username, update_password)

    st.subheader("Delete User")
    delete_username = st.text_input("Username to Delete")
    delete_button = st.button("Delete Login", key="delete_login")
    if delete_button:
        delete_login(delete_username)

def display_Faculty_table():
    connection = create_connection()
    query = "SELECT * FROM F_faculty"
    result = execute_select_query(connection, query)
    st.table(result)
    connection.close()

def add_faculty(F_ID, F_time, classes_conducted, F_name, class_ID=None, course_ID=None):
    connection = create_connection()
    if class_ID is None:
        class_ID = "NULL"
    if course_ID is None:
        course_ID = "NULL"
    
    query = f"INSERT INTO F_faculty (F_ID, F_time, classes_conducted, F_name, class_ID, course_ID) VALUES ('{F_ID}', '{F_time}', {classes_conducted}, '{F_name}', {class_ID}, '{course_ID}')"
    execute_query(connection, query)
    connection.close()
    st.success("Faculty added successfully!")

def update_faculty(F_ID, new_F_time=None, new_classes_conducted=None, new_F_name=None, new_class_ID=None, new_course_ID=None):
    connection = create_connection()
    set_values = []

    if new_F_time is not None:
        set_values.append(f"F_time = '{new_F_time}'")
    if new_classes_conducted is not None:
        set_values.append(f"classes_conducted = {new_classes_conducted}")
    if new_F_name is not None:
        set_values.append(f"F_name = '{new_F_name}'")
    if new_class_ID is not None:
        set_values.append(f"class_ID = {new_class_ID}")
    if new_course_ID is not None:
        set_values.append(f"course_ID = '{new_course_ID}'")

    set_clause = ", ".join(set_values)
    update_query = f"UPDATE F_faculty SET {set_clause} WHERE F_ID = '{F_ID}'"

    execute_query(connection, update_query)
    st.success(f"Faculty with ID {F_ID} updated successfully!")
    connection.close()

def delete_faculty(F_ID):
    connection = create_connection()
    query = f"DELETE FROM F_faculty WHERE F_ID = '{F_ID}'"
    execute_query(connection, query)
    st.success(f"Faculty with ID {F_ID} deleted successfully!")
    connection.close()

def display_Class_table():
    connection = create_connection()
    query = "SELECT * FROM Class"
    result = execute_select_query(connection, query)
    st.table(result)
    connection.close()

def add_class(duration, class_status, class_date, building, floor_number, room_no, class_time, class_type, class_category):
    connection = create_connection()
    query = f"INSERT INTO Class (duration, class_status, class_date, building, Floor_number, Room_no, Class_time, class_type, class_category) VALUES ('{duration}', '{class_status}', '{class_date}', '{building}', {floor_number}, '{room_no}', '{class_time}', '{class_type}', '{class_category}')"
    execute_query(connection, query)
    connection.close()
    st.success("Class added successfully!")

def update_class(class_id, new_duration=None, new_class_status=None, new_class_date=None, new_building=None, new_floor_number=None, new_room_no=None, new_class_time=None, new_class_type=None, new_class_category=None):
    connection = create_connection()
    set_values = []

    if new_duration is not None:
        set_values.append(f"duration = '{new_duration}'")
    if new_class_status is not None:
        set_values.append(f"class_status = '{new_class_status}'")
    if new_class_date is not None:
        set_values.append(f"class_date = '{new_class_date}'")
    if new_building is not None:
        set_values.append(f"building = '{new_building}'")
    if new_floor_number is not None:
        set_values.append(f"Floor_number = {new_floor_number}")
    if new_room_no is not None:
        set_values.append(f"Room_no = '{new_room_no}'")
    if new_class_time is not None:
        set_values.append(f"Class_time = '{new_class_time}'")
    if new_class_type is not None:
        set_values.append(f"class_type = '{new_class_type}'")
    if new_class_category is not None:
        set_values.append(f"class_category = '{new_class_category}'")

    set_clause = ", ".join(set_values)
    update_query = f"UPDATE Class SET {set_clause} WHERE class_id = {class_id}"

    execute_query(connection, update_query)
    st.success(f"Class with ID {class_id} updated successfully!")
    connection.close()

def delete_class(class_id):
    connection = create_connection()
    query = f"DELETE FROM Class WHERE class_id = {class_id}"
    execute_query(connection, query)
    st.success(f"Class with ID {class_id} deleted successfully!")
    connection.close()

def Class_operations():
    st.subheader("Class Operations")

    st.subheader("Add New Class")
    duration = st.text_input("Duration")
    class_status = st.selectbox("Class Status", ['in progress', 'canceled', 'scheduled'])
    class_date = st.date_input("Class Date")
    building = st.text_input("Building")
    floor_number = st.number_input("Floor Number", min_value=1, step=1)
    room_no = st.text_input("Room Number")
    class_time = st.text_input("Class Time")
    class_type = st.selectbox("Class Type", ['online', 'offline'])
    class_category = st.selectbox("Class Category", ['Faculty', 'Tutor', 'Group Study'])
    add_button = st.button("Add Class", key="add_class")
    if add_button:
        add_class(duration, class_status, class_date, building, floor_number, room_no, class_time, class_type, class_category)

    st.subheader("Update Class")
    update_class_id = st.number_input("Class ID to Update", min_value=1, step=1)
    update_duration = st.text_input("New Duration  ")
    update_class_status = st.selectbox("New Class Status  ", ['in progress', 'canceled', 'scheduled'])
    update_class_date = st.date_input("New Class Date  ")
    update_building = st.text_input("New Building  ")
    update_floor_number = st.number_input("New Floor Number  ", min_value=1, step=1)
    update_room_no = st.text_input("New Room Number  ")
    update_class_time = st.text_input("New Class Time  ")
    update_class_type = st.selectbox("New Class Type  ", ['online', 'offline'])
    update_class_category = st.selectbox("New Class Category  ", ['Faculty', 'Tutor', 'Group Study'])
    update_button = st.button("Update Class")
    if update_button:
        update_class(update_class_id, update_duration, update_class_status, update_class_date, update_building, update_floor_number, update_room_no, update_class_time, update_class_type, update_class_category)

    st.subheader("Delete Class")
    delete_class_id = st.number_input("Class ID to Delete", min_value=1, step=1)
    delete_button = st.button("Delete Class", key="delete_class")
    if delete_button:
        delete_class(delete_class_id)

def Faculty_operations():
    st.subheader("Faculty Operations")

    st.subheader("Add New Faculty")
    new_F_ID = st.text_input("Faculty ID")
    new_F_time = st.text_input("Faculty Time")
    new_classes_conducted = st.number_input("Classes Conducted", min_value=0, step=1)
    new_F_name = st.text_input("Faculty Name")
    new_class_ID = st.text_input("Class ID  ")
    new_course_ID = st.text_input("Course ID  ")
    add_button = st.button("Add Faculty", key="add_faculty")
    if add_button:
        add_faculty(new_F_ID, new_F_time, new_classes_conducted, new_F_name, new_class_ID, new_course_ID)

    st.subheader("Update Faculty")
    update_F_ID = st.text_input("Faculty ID to Update")
    update_F_time = st.text_input("New Faculty Time  ")
    update_classes_conducted = st.number_input("New Classes Conducted  ", min_value=0, step=1)
    update_F_name = st.text_input("New Faculty Name  ")
    update_class_ID = st.text_input("New Class ID  ")
    update_course_ID = st.text_input("New Course ID  ")
    update_button = st.button("Update Faculty")
    if update_button:
        update_faculty(update_F_ID, update_F_time, update_classes_conducted, update_F_name, update_class_ID, update_course_ID)

    st.subheader("Delete Faculty")
    delete_F_ID = st.text_input("Faculty ID to Delete")
    delete_button = st.button("Delete Faculty", key="delete_faculty")
    if delete_button:
        delete_faculty(delete_F_ID)

def display_Student_table():
    connection = create_connection()
    query = "SELECT * FROM Student"
    result = execute_select_query(connection, query)
    st.table(result)
    connection.close()

def add_student(S_section, S_name, S_sem, S_SRN):
    connection = create_connection()

    query = f"INSERT INTO Student (S_SRN, S_section, S_name, S_sem) VALUES ('{S_SRN}', '{S_section}', '{S_name}', {S_sem})"
    execute_query(connection, query)
    connection.close()
    st.success("Student added successfully!")

def update_student(S_UID, new_S_SRN=None, new_S_section=None, new_S_name=None, new_S_sem=None):
    connection = create_connection()
    set_values = []

    if new_S_SRN is not None:
        set_values.append(f"S_SRN = '{new_S_SRN}'")
    if new_S_section is not None:
        set_values.append(f"S_section = '{new_S_section}'")
    if new_S_name is not None:
        set_values.append(f"S_name = '{new_S_name}'")
    if new_S_sem is not None:
        set_values.append(f"S_sem = {new_S_sem}")

    set_clause = ", ".join(set_values)
    update_query = f"UPDATE Student SET {set_clause} WHERE S_UID = {S_UID}"

    execute_query(connection, update_query)
    st.success(f"Student with ID {S_UID} updated successfully!")
    connection.close()

def delete_student(S_UID):
    connection = create_connection()
    query = f"DELETE FROM Student WHERE S_UID = {S_UID}"
    execute_query(connection, query)
    st.success(f"Student with ID {S_UID} deleted successfully!")
    connection.close()

def Student_operations():
    st.subheader("Student Operations")

    st.subheader("Add New Student")
    new_S_SRN = st.text_input("SRN")
    new_S_section = st.text_input("Section")
    new_S_name = st.text_input("Name")
    new_S_sem = st.number_input("Semester", min_value=1, step=1)
    add_button = st.button("Add Student", key="add_student")
    if add_button:
        add_student(new_S_section, new_S_name, new_S_sem, new_S_SRN)

    st.subheader("Update Student")
    update_S_UID = st.number_input("Student ID to Update", min_value=1, step=1)
    update_S_SRN = st.text_input("New SRN")
    update_S_section = st.text_input("New Section")
    update_S_name = st.text_input("New Name")
    update_S_sem = st.number_input("New Semester", min_value=1, step=1)
    update_button = st.button("Update Student")
    if update_button:
        update_student(update_S_UID, update_S_SRN, update_S_section, update_S_name, update_S_sem)

    st.subheader("Delete Student")
    delete_S_UID = st.number_input("Student ID to Delete", min_value=1, step=1)
    delete_button = st.button("Delete Student", key="delete_student")
    if delete_button:
        delete_student(delete_S_UID)

def display_Subject_table():
    connection = create_connection()
    query = "SELECT * FROM Subject"
    result = execute_select_query(connection, query)
    st.table(result)
    connection.close()

def add_subject(courseID, course_name, resources):
    connection = create_connection()
    query = f"INSERT INTO Subject (courseID, course_name, resources) VALUES ('{courseID}', '{course_name}', '{resources}')"
    execute_query(connection, query)
    connection.close()
    st.success("Subject added successfully!")

def update_subject(courseID, new_course_name=None, new_resources=None):
    connection = create_connection()
    set_values = []

    if new_course_name is not None:
        set_values.append(f"course_name = '{new_course_name}'")
    if new_resources is not None:
        set_values.append(f"resources = '{new_resources}'")

    set_clause = ", ".join(set_values)
    update_query = f"UPDATE Subject SET {set_clause} WHERE courseID = '{courseID}'"

    execute_query(connection, update_query)
    st.success(f"Subject with Course ID {courseID} updated successfully!")
    connection.close()

def delete_subject(courseID):
    connection = create_connection()
    query = f"DELETE FROM Subject WHERE courseID = '{courseID}'"
    execute_query(connection, query)
    st.success(f"Subject with Course ID {courseID} deleted successfully!")
    connection.close()

def display_Tutor_table():
    connection = create_connection()
    query = "SELECT * FROM tutor_details"
    result = execute_select_query(connection, query)
    st.table(result)
    connection.close()

def add_tutor(T_SRN, T_section, T_name, T_sem, T_time, Class_ID=None, Course_ID=None):
    connection = create_connection()
    
    if Class_ID is None:
        Class_ID = "NULL"
    if Course_ID is None:
        Course_ID = "NULL"
    
    query = f"INSERT INTO tutor_details (T_SRN, T_section, T_name, T_sem, T_time, Class_ID, Course_ID) VALUES ({T_SRN}, '{T_section}', '{T_name}', {T_sem}, '{T_time}', {Class_ID}, '{Course_ID}')"
    execute_query(connection, query)
    connection.close()
    st.success("Tutor added successfully!")

def update_tutor(T_ID,new_T_SRN=None, new_T_section=None, new_T_name=None, new_T_sem=None, new_T_time=None, new_Class_ID=None, new_Course_ID=None):
    connection = create_connection()
    set_values = []

    if new_T_SRN is not None:
        set_values.append(f"T_SRN = '{new_T_SRN}'")
    if new_T_section is not None:
        set_values.append(f"T_section = '{new_T_section}'")
    if new_T_name is not None:
        set_values.append(f"T_name = '{new_T_name}'")
    if new_T_sem is not None:
        set_values.append(f"T_sem = {new_T_sem}")
    if new_T_time is not None:
        set_values.append(f"T_time = '{new_T_time}'")
    if new_Class_ID is not None:
        set_values.append(f"Class_ID = {new_Class_ID}")
    if new_Course_ID is not None:
        set_values.append(f"Course_ID = '{new_Course_ID}'")

    set_clause = ", ".join(set_values)
    update_query = f"UPDATE tutor_details SET {set_clause} WHERE T_SRN = {T_ID}"

    execute_query(connection, update_query)
    st.success(f"Tutor with SRN {T_ID} updated successfully!")
    connection.close()

def delete_tutor(T_ID):
    connection = create_connection()
    query = f"DELETE FROM tutor_details WHERE T_ID = {T_ID}"
    execute_query(connection, query)
    st.success(f"Tutor with SRN {T_ID} deleted successfully!")
    connection.close()

def Tutor_operations():
    st.subheader("Tutor Operations")

    st.subheader("Add New Tutor")
    new_T_SRN = st.number_input("Tutor SRN")
    new_T_section = st.text_input("Tutor Section")
    new_T_name = st.text_input("Tutor Name")
    new_T_sem = st.number_input("Tutor Semester", min_value=1, step=1)
    new_T_time = st.text_input("Tutor Time")
    new_Class_ID = st.text_input("Class ID  ")
    new_Course_ID = st.text_input("Course ID  ")
    add_button = st.button("Add Tutor", key="add_tutor")
    if add_button:
        add_tutor(new_T_SRN, new_T_section, new_T_name, new_T_sem, new_T_time, new_Class_ID, new_Course_ID)

    st.subheader("Update Tutor")
    update_T_ID = st.number_input("Tutor ID", min_value=1, step=1)
    update_T_SRN = st.number_input("Tutor SRN", min_value=1, step=1)
    update_T_section = st.text_input("New Tutor Section  ")
    update_T_name = st.text_input("New Tutor Name  ")
    update_T_sem = st.number_input("New Tutor Semester  ", min_value=1, step=1)
    update_T_time = st.text_input("New Tutor Time  ")
    update_Class_ID = st.text_input("New Class ID  ")
    update_Course_ID = st.text_input("New Course ID  ")
    update_button = st.button("Update Tutor")
    if update_button:
        update_tutor(update_T_ID,update_T_SRN, update_T_section, update_T_name, update_T_sem, update_T_time, update_Class_ID, update_Course_ID)

    st.subheader("Delete Tutor")
    delete_T_ID = st.number_input("Tutor ID to Delete", min_value=1, step=1)
    delete_button = st.button("Delete Tutor", key="delete_tutor")
    if delete_button:
        delete_tutor(delete_T_ID)

def Subject_operations():
    st.subheader("Subject Operations")

    st.subheader("Add New Subject")
    new_courseID = st.text_input("Course ID")
    new_course_name = st.text_input("Course Name")
    new_resources = st.text_area("Resources")
    add_button = st.button("Add Subject", key="add_subject")
    if add_button:
        add_subject(new_courseID, new_course_name, new_resources)

    st.subheader("Update Subject")
    update_courseID = st.text_input("Course ID to Update")
    update_course_name = st.text_input("New Course Name  ")
    update_resources = st.text_area("New Resources  ")
    update_button = st.button("Update Subject")
    if update_button:
        update_subject(update_courseID, update_course_name, update_resources)

    st.subheader("Delete Subject")
    delete_courseID = st.text_input("Course ID to Delete")
    delete_button = st.button("Delete Subject", key="delete_subject")
    if delete_button:
        delete_subject(delete_courseID)

def query_students_for_faculty():
    connection = create_connection()

    # Your SQL query
    sql_query = """
    SELECT S_name
    FROM Student
    WHERE S_UID IN (
        SELECT S_UID
        FROM Class
        WHERE class_type = 'offline'
          AND class_category = 'Faculty'
          AND Class.class_id IN (
              SELECT class_ID
              FROM F_faculty
              WHERE F_name = 'David'
          )
    );
    """

    result = execute_select_query(connection, sql_query)
    connection.close()

    return result

def query_tutors_for_faculty():
    connection = create_connection()

    # Your SQL query
    sql_query = """
    SELECT T_name
    FROM tutor_details
    WHERE Course_ID IN (
        SELECT Course_ID
        FROM F_faculty
        WHERE F_name = 'Faculty 2'
    );
    """

    result = execute_select_query(connection, sql_query)
    connection.close()

    return result

def user_page():
    st.title("User Page")
    username = st.text_input("Enter Username")
    password = st.text_input("Enter Password", type="password")
    if not username or not password:
        st.warning("Please enter both username and password.")
        return
    
    connection = create_connection()
    login_query = f"SELECT * FROM Login WHERE Username='{username}' AND Password='{password}'"
    user_data = execute_select_query(connection, login_query)
    connection.close()

    if user_data:
        st.success("Login successful!")
        selected_table = st.selectbox("Select Table", ["Home","Functions","Procedure","Class", "Faculty", "Student", "Subject", "Tutor"])

        if selected_table == "Home":
            st.write("Welcome to the User Page. Select a table from the dropdown to perform operations.")

            st.subheader("Aggregate Queries")
            st.write("Query Building Total Duration")
            st.write("This query retrieves the total duration of all offline classes grouped by building.")

            if st.button("Execute Aggregate Query 1"):
                building_duration_result = get_building_total_duration()
                st.table(building_duration_result)

            st.write("Query Tutor Classes Conducted")
            st.write("This query retrieves the count of classes conducted by each Tutor with more than 5 classes.")

            if st.button("Execute Aggregate Query 2"):
                faculty_classes_result = get_faculty_classes_conducted()
                st.table(faculty_classes_result)

            st.markdown("---")
        
            st.subheader("Nested Queries")
            st.write("Query for Faculty")
            st.write("This nested query retrieves classes conducted by a specific faculty")

            if st.button("Execute Nested Query 1"):
                students_result = query_students_in_online_classes()
                st.table(students_result)
            st.markdown("---")

            st.subheader("Correlated Queries")
            st.write("Query Tutors for Faculty")
            st.write("This query retrieves the names of tutors assigned to the same courses as the faculty member 'Faculty 2'.")

            if st.button("Execute Correlated Query 1"):
                tutors_result = query_tutors_for_faculty()
                st.table(tutors_result)



        elif selected_table == "Functions":
            stored_functions()

        elif selected_table == "Procedure":
            stored_procedure()

        elif selected_table == "Class":
            display_Class_table()
        
        elif selected_table == "Faculty":
            display_Faculty_table()
        
        elif selected_table == "Student":
            display_Student_table()
        
        elif selected_table == "Subject":
            display_Subject_table()
        
        elif selected_table == "Tutor":
            display_Tutor_table()

def query_students_in_online_classes():
    connection = create_connection()

    # Your SQL query
    sql_query = """
    SELECT *
    FROM Class
    WHERE class_id IN (
        SELECT class_ID
        FROM F_faculty
        WHERE F_ID = 'PES3001'
    );
    """

    result = execute_select_query(connection, sql_query)
    connection.close()

    return result

def query_subjects_with_more_than_2_resources():
    connection = create_connection()

    # Your SQL query
    sql_query = """
    SELECT course_name
    FROM Subject
    WHERE courseID IN (
        SELECT courseID
        FROM Subject
        GROUP BY courseID
        HAVING COUNT(*) > 2
    );
    """

    result = execute_select_query(connection, sql_query)
    connection.close()

    return result

def home_page():
    st.title("Study Buddy - Educational Support Platform")
    st.markdown("""
    Welcome to Study Buddy, where students come together to enhance their learning experience!
    """)

def get_faculty_class_count(faculty_id):
    connection = create_connection()

    # Your SQL query
    sql_query = f"SELECT GetFacultyClassCount('{faculty_id}') AS classCount;"

    result = execute_select_query(connection, sql_query)
    connection.close()

    return result[0]['classCount']

def is_student_enrolled(student_srn, class_id):
    connection = create_connection()

    # Your SQL query
    sql_query = f"SELECT IsStudentEnrolled('{student_srn}', {class_id}) AS isEnrolled;"

    result = execute_select_query(connection, sql_query)
    connection.close()

    return result[0]['isEnrolled']

def calculate_average_classes():
    connection = create_connection()

    # Your SQL query
    sql_query = "SELECT CalculateAverageClasses() AS avgClasses;"

    result = execute_select_query(connection, sql_query)
    connection.close()

    return result[0]['avgClasses']

def stored_functions():
    st.header("Stored Functions") 
    st.subheader("Is Student Enrolled")
    student_srn = st.text_input("Enter Student SRN:")
    class_id = st.number_input("Enter Class ID:")

    if st.button("Check Enrollment"):
        is_enrolled = is_student_enrolled(student_srn, class_id)
        st.write(f"Student {student_srn} {'is' if is_enrolled else 'is not'} enrolled in class {class_id}.")

    st.markdown("---") 

    st.subheader("Calculate Average Classes")
    
    if st.button("Calculate Average Classes"):
        avg_classes = calculate_average_classes()
        st.write(f"The average number of classes conducted per faculty is: {avg_classes}")

def get_student_class_schedule(student_srn):
    connection = create_connection()

    sql_query = f"CALL GetStudentClassSchedule('{student_srn}');"

    result = execute_select_query(connection, sql_query)
    connection.close()

    return result

def enroll_student(student_srn, class_id):
    connection = create_connection()

    sql_query = f"CALL EnrollStudent('{student_srn}', {class_id});"

    execute_modify_query(connection, sql_query)
    connection.close()

def get_faculty_classes(faculty_id):
    connection = create_connection()

    sql_query = f"CALL GetFacultyClasses('{faculty_id}');"

    result = execute_select_query(connection, sql_query)
    connection.close()

    return result

def assign_tutor_to_class(p_T_SRN, p_T_section, p_T_name, p_T_sem, p_T_time, p_Class_ID, p_Course_ID):
    try:
        connection = create_connection()
        cursor = connection.cursor()

        cursor.callproc('AssignTutorToClass', (p_T_SRN, p_T_section, p_T_name, p_T_sem, p_T_time, p_Class_ID, p_Course_ID))
        connection.commit()

        st.success("Tutor assigned to class successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err.msg}")
    finally:
        cursor.close()
        connection.close()
        
def stored_procedure():
    st.header("Assign Tutor to Class")

    p_T_SRN = st.number_input("Tutor SRN")
    p_T_section = st.text_input("Tutor Section")
    p_T_name = st.text_input("Tutor Name")
    p_T_sem = st.number_input("Tutor Semester", step=1)
    p_T_time = st.text_input("Tutor Time")
    p_Class_ID = st.number_input("Class ID", step=1)
    p_Course_ID = st.text_input("Course ID")

    if st.button("Assign Tutor"):
        assign_tutor_to_class(p_T_SRN, p_T_section, p_T_name, p_T_sem, p_T_time, p_Class_ID, p_Course_ID)

    st.markdown("---")

    st.subheader("Enroll Student")
    enroll_student_srn = st.text_input("Enter Student SRN to get the list:")
    enroll_class_id = st.number_input("Enter Class ID:")

    if st.button("Enroll Student"):
        enroll_student(enroll_student_srn, enroll_class_id)
        st.success(f"Student {enroll_student_srn} enrolled in class {enroll_class_id} successfully.")

    st.markdown("---")

    st.subheader("Get Faculty Classes")
    faculty_id = st.text_input("Enter Faculty ID:")

    if st.button("Get Faculty Classes"):
        faculty_classes = get_faculty_classes(faculty_id)
        st.table(faculty_classes)

def get_building_total_duration():
    connection = create_connection()

    # Your SQL query
    sql_query = """
    SELECT building, SUM(duration) AS total_duration
    FROM Class
    WHERE class_type = 'offline' AND building IS NOT NULL
    GROUP BY building;
    """

    result = execute_select_query(connection, sql_query)
    connection.close()

    return result

def get_faculty_classes_conducted():
    connection = create_connection()

    # Your SQL query
    sql_query = """
    SELECT T_SRN, COUNT(*) AS ClassesConducted
    FROM tutor_details
    GROUP BY T_SRN
    HAVING COUNT(*) > 5;
    """

    result = execute_select_query(connection, sql_query)
    connection.close()

    return result

def main():
    pages = ["Home", "Signup","Users", "Admins"]
    page = st.sidebar.radio("Select Page", pages)

    if page == "Home":
        home_page()

    elif page == "Signup":
        st.title("Sign Up")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        signup_button = st.button("Sign Up")

        if signup_button:
            handle_signup(username, password)

    elif page == "Users":
        user_page()

    elif page == "Admins":
        admin()

if __name__ == "__main__":
    main()
