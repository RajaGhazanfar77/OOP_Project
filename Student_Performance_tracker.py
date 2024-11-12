class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_average(self):
        return sum(self.scores) / len(self.scores)

    def is_passing(self, passing_score=40):
        return all(score >= passing_score for score in self.scores)

class PerformanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, scores):
        self.students[name] = Student(name, scores)

    def calculate_class_average(self):
        total_scores = 0
        num_students = len(self.students)
        for student in self.students.values():
            total_scores += student.calculate_average()
        return total_scores / num_students

    def display_student_performance(self):
        for student in self.students.values():
            print(f"Student: {student.name}")
            print(f"Average Score: {student.calculate_average():.2f}")
            if student.is_passing():
                print("Passing")
            else:
                print("Failing")
            print()

def main():
    tracker = PerformanceTracker()

    while True:
        name = input("Enter student's name (or 'q' to quit): ")
        if name.lower() == 'q':
            break

        scores = []
        for subject in ['Math', 'Science', 'English']:
            while True:
                try:
                    score = int(input(f"Enter score for {subject}: "))
                    scores.append(score)
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")

        tracker.add_student(name, scores)

    tracker.display_student_performance()
    print(f"Class Average: {tracker.calculate_class_average():.2f}")

if __name__ == "__main__":
    main()