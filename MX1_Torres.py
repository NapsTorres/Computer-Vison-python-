class ClassSubject:
    def __init__(self):
        self.subjects = {}

    def add_subject(self, subject, schedule):
        if subject not in self.subjects:
            self.subjects[subject] = schedule
            print(f"Added Subject '{subject}'")
        else:
            print(f"Subject '{subject}' already exists")

    def update_subject_schedule(self, subject, new_schedule):
        if subject in self.subjects:
            self.subjects[subject] = new_schedule
            print(f"Updated schedule for subject '{subject}' to {new_schedule}")
        else:
            print(f"Subject '{subject}' not found.")


class ClassTeacher:
    def __init__(self):
        self.teachers = {}

    def add_teacher(self, teacher, schedule):
        if teacher not in self.teachers:
            self.teachers[teacher] = schedule
            print(f"Added teacher '{teacher}'")
        else:
            print(f"Teacher '{teacher}' already exists.")

    def update_teacher_schedule(self, teacher, new_schedule):
        if teacher in self.teachers:
            self.teachers[teacher] = new_schedule
            print(f"Updated schedule for teacher '{teacher}' to {new_schedule}")
        else:
            print(f"Teacher '{teacher}' not found.")


class ClassSchedule:
    def __init__(self):
        self.subjects = {}
        self.teachers = {}

    def add_schedule(self, subject, teacher, day, time, room):
        if subject not in self.subjects:
            self.subjects[subject] = []
        if teacher not in self.teachers:
            self.teachers[teacher] = []

        self.subjects[subject].append((teacher, day, time, room))
        self.teachers[teacher].append((subject, day, time, room))
        print(f"Added schedule: Teacher {teacher} teaching {subject} on {day} at {time} in room {room}")

    def update_subject_teacher(self, subject, teacher):
        if subject in self.subjects and teacher in self.teachers:
            for sched in self.subjects[subject]:
                if sched[0] == teacher:
                    print(f"Teacher '{teacher}' already assigned to subject '{subject}'.")
                    return
            for sched in self.subjects[subject]:
                if sched[1:] not in self.teachers[teacher]:
                    self.subjects[subject].append((teacher, *sched[1:]))
                    print(f"Assigned teacher '{teacher}' to subject '{subject}'.")
                    return
            print("Teacher's schedule conflicts with subject's existing schedule.")
        else:
            print("Subject or teacher not found.")


class ClassroomSchedule:
    def __init__(self):
        self.subjects = {}

    def display_schedule(self):
        print("Teacher Subject Day Time Room")
        for subject, schedules in self.subjects.items():
            for schedule in schedules:
                print(f"{schedule[0]} {subject} {schedule[1]} {schedule[2]} {schedule[3]}")


subject = ClassSubject()
teacher = ClassTeacher()
schedule = ClassSchedule()
classroom = ClassroomSchedule()


subject.add_subject("Comp Prog", [])
subject.add_subject("Comp Vision", [])
subject.add_subject("App Dev", [])
subject.add_subject("Data Structure", [])


teacher.add_teacher("RBaldemoro", [])
teacher.add_teacher("FImperial", [])
teacher.add_teacher("LGardose", [])
teacher.add_teacher("MAlbos", [])


schedule.add_schedule("Comp Prog", "RBaldemoro", "MW", "1:00 - 4:00", "ST202")
schedule.add_schedule("Comp Vision", "RBaldemoro", "TTH", "4:00 - 5:30", "ST201")
schedule.add_schedule("App Dev", "FImperial", "TTH", "2:30 - 4:00", "ST201")
schedule.add_schedule("App Dev", "FImperial", "MW", "9:00 - 10:30", "ST202")
schedule.add_schedule("Data Structure", "LGardose", "MW", "7:30 - 9:00", "ST201")
schedule.add_schedule("Data Structure", "MAlbos", "TTH", "9:00 - 10:30", "ST202")

subject.update_subject_schedule("Comp Prog", "1:00 - 3:00")
teacher.update_teacher_schedule("RBaldemoro", "MW 1:00 - 4:00")  
schedule.update_subject_teacher("Comp Vision", "FImperial")  


classroom.subjects = schedule.subjects

classroom.display_schedule()

