def calculate_attendance(morning_attendance, afternoon_attendance, number_students, days_opened):
    """
    Calculate the attendance percentage.
    
    Parameters:
    M (int): Total morning attendance per week.
    A (int): Total afternoon attendance per week.
    number_students (int): Number of students in the class.
    days_opened (int): Number of days the school opened in a week.
    
    Returns:
    float: Attendance percentage.
    """
    total_attendance = morning_attendance + afternoon_attendance
    attendance_percentage = (total_attendance * 100) / (number_students * days_opened)
    return attendance_percentage

# Example usage
# Assuming the following values:
# Total morning attendance (M) = 50
# Total afternoon attendance (A) = 45
# Number of students on roll = 30
# Number of days school opened in a week = 5
week = int(input("What week are you calculating for? Eg 1: "))
morning_attendance = int(input("Please enter morning attendance: "))  
afternoon_attendance = int(input("Please enter afternoon attendance: "))
number_students = int(input("Please enter the total number of students: "))
days_opened = int(input("Please enter the number of times school was opened: "))

attendance_percentage = calculate_attendance(morning_attendance, afternoon_attendance, number_students, days_opened)
print(f"The Attendance Percentage for week {week} is: {attendance_percentage:.2f}%")
