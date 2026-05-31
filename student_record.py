import psycopg
class Student:
    def data(self):
        while True:
            name = input("Enter your full name: ")
            if name.strip() != "":
                break
            print("❌ Name cannot be empty")

        # Roll number
        while True:
            roll = input("Roll num: ")
            if roll.strip() != "":
                break
            print("❌ Roll number cannot be empty")

        # Enrollment number
        while True:
            enrollment_num = input("Enter your enrollment num: ")
            if enrollment_num.strip() != "":
                break
            print("❌ Enrollment number cannot be empty")
        while True:
            email = input("Enter your email: ")
            if "@" in email and "." in email:
                break
            print("❌ Invalid email format (example: abc@gmail.com)")
        course=input("enter course :")
        department=input("enter the department :")
        pre_sem=input("previous semester :")
        pre_sem_result=input("enter total result :")
        while True:
            attendance = input("Enter your attendance (0-100): ")
            if attendance.isdigit():
                attendance = int(attendance)
                if 0 <= attendance <= 100:
                    break
            print("❌ Attendance must be between 0 and 100")
        while True:
            paid = input("Paid seat or not (yes/no): ").lower()
            if paid == "yes" or paid == "no":
                break
            print("❌ Please enter only yes or no")
        try:
            conn=psycopg.connect(
            host="localhost",
            port=5432,
            dbname="student_data_2024",
            user="postgres",
            password=1234
            )
            cur=conn.cursor()
            cur.execute("SELECT roll FROM student_registration WHERE roll = %s", (roll,))
            existing = cur.fetchone()

            if existing:
                print(f"⚠️ Student with roll number {roll} already exists. Entry ignored.")
            else:
                query="""insert into student_registration
            (name, roll, enrollment_num, email, course, department, pre_sem, per_sem_result, attendance, paid_seet)
            values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                values=(
                name,
                roll,
                enrollment_num,
                email,
                course,
                department,
                pre_sem,
                pre_sem_result,
                attendance,
                paid  
                )
                cur.execute(query,values)
            conn.commit()
            print("data insert successfully")
            cur.close()
            conn.close()
        except Exception as e :
              print("❌ Error:", e)
s = Student()
s.data()
        
