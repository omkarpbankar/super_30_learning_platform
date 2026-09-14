class User:
    # Class variable
    total_users = 0

    def __init__(self, name, email, user_id):
        self.name = name
        self.email = email
        self.user_id = user_id
        User.total_users += 1

    # Instance method
    def display_info(self):
        print(f"User ID: {self.user_id} | Name: {self.name} | Email: {self.email}")

    # Class method
    @classmethod
    def get_total_users(cls):
        return cls.total_users

    # Static method
    @staticmethod
    def is_valid_email(email):
        return "@" in email and "." in email

class Student(User):
    def __init__(self, name, email, user_id, course_name="Unassigned"):
        super().__init__(name, email, user_id)
        self.course_name = course_name
        self.completed_assignments = 0

    def assign_course(self, course_name):
        self.course_name = course_name
        print(f"Course '{course_name}' assigned to Student {self.name}.")

    def submit_assignment(self):
        self.completed_assignments += 1
        print(f"Student {self.name} submitted an assignment. Total completed: {self.completed_assignments}")

    def display_info(self):
        super().display_info()
        print(f"Role: Student | Course: {self.course_name} | Completed Assignments: {self.completed_assignments}")

class Mentor(User):
    def __init__(self, name, email, user_id, expertise):
        super().__init__(name, email, user_id)
        self.expertise = expertise
        self.students_assigned = 0

    def assign_student(self):
        self.students_assigned += 1
        print(f"A new student has been assigned to Mentor {self.name}. Total students assigned: {self.students_assigned}")

    def display_info(self):
        super().display_info()
        print(f"Role: Mentor | Expertise: {self.expertise} | Students Assigned: {self.students_assigned}")

if __name__ == "__main__":
    print(f"Testing static method (valid email check): {User.is_valid_email('student@super30.com')}")
    print("-" * 50)

    # Registering students
    student1 = Student("Alice", "alice@super30.com", "S001")
    student2 = Student("Bob", "bob@super30.com", "S002")

    # Creating a mentor
    mentor1 = Mentor("Charlie", "charlie@super30.com", "M001", "Python Programming")

    # Assigning courses
    student1.assign_course("Data Science Basics")
    student2.assign_course("Machine Learning")
    print("-" * 50)

    # Submitting assignments
    student1.submit_assignment()
    student1.submit_assignment()
    student2.submit_assignment()
    print("-" * 50)

    # Assigning students to mentor
    mentor1.assign_student()
    mentor1.assign_student()
    print("-" * 50)

    # Displaying information
    student1.display_info()
    print("-" * 50)
    student2.display_info()
    print("-" * 50)
    mentor1.display_info()
    print("-" * 50)

    # Using class method
    print(f"Total number of users registered: {User.get_total_users()}")
