class Course:
    def __init__(self, course_code, course_name, instructor):
        self.course_code = course_code
        self.course_name = course_name
        self.instructor = instructor

    def display_info(self):
        return f"{self.course_code}: {self.course_name} - Instructor: {self.instructor}"


class Lecture(Course):
    def __init__(self, course_code, course_name, instructor, day, time):
        super().__init__(course_code, course_name, instructor)
        self.day = day
        self.time = time

    def display_info(self):
        return super().display_info() + f" - Lecture: {self.day} at {self.time}"


class Lab(Course):
    def __init__(self, course_code, course_name, instructor, day, time, lab_location):
        super().__init__(course_code, course_name, instructor)
        self.day = day
        self.time = time
        self.lab_location = lab_location

    def display_info(self):
        return super().display_info() + f" - Lab: {self.day} at {self.time}, Location: {self.lab_location}"


class Schedule:
    def __init__(self):
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def display_schedule(self):
        for course in self.courses:
            print(course.display_info())


# Function to create a course based on user input
def create_course():
    course_code = input("Enter course code: ")
    course_name = input("Enter course name: ")
    instructor = input("Enter instructor: ")
    return course_code, course_name, instructor


# Function to create a lecture based on user input
def create_lecture():
    day = input("Enter lecture day: ")
    time = input("Enter lecture time: ")
    return day, time


# Function to create a lab based on user input
def create_lab():
    day = input("Enter lab day: ")
    time = input("Enter lab time: ")
    lab_location = input("Enter lab location: ")
    return day, time, lab_location


# Example usage:
if __name__ == "__main__":
    schedule = Schedule()

    while True:
        print("\n1. Add Lecture\n2. Add Lab\n3. Display Schedule\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            course_code, course_name, instructor = create_course()
            day, time = create_lecture()
            course = Lecture(course_code, course_name, instructor, day, time)
            schedule.add_course(course)
        elif choice == "2":
            course_code, course_name, instructor = create_course()
            day, time, lab_location = create_lab()
            course = Lab(course_code, course_name, instructor, day, time, lab_location)
            schedule.add_course(course)
        elif choice == "3":
            schedule.display_schedule()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
