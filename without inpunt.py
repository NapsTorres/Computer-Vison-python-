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


# Example usage:
if __name__ == "__main__":
    # Create some courses
    course1 = Lecture("CS101", "Introduction to Computer Science", "Dr. Smith", "Monday", "9:00 AM")
    course2 = Lab("CS101", "Introduction to Computer Science", "Dr. Smith", "Wednesday", "1:00 PM", "Lab Building Room 101")
    course3 = Lecture("MATH101", "Calculus I", "Prof. Johnson", "Tuesday", "10:00 AM")

    # Create a schedule and add courses to it
    schedule = Schedule()
    schedule.add_course(course1)
    schedule.add_course(course2)
    schedule.add_course(course3)

    # Display the schedule
    schedule.display_schedule()
