def determine_grade(marks):
    """
    Function to determine grade and message based on marks.
    Logic based on the requirements:
    A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: 0-59
    """
    if 90 <= marks <= 100:
        return "A", "Excellent work! You're a star!"
    elif 80 <= marks <= 89:
        return "B", "Very Good! Keep it up!"
    elif 70 <= marks <= 79:
        return "C", "Good job! You're doing well."
    elif 60 <= marks <= 69:
        return "D", "You passed! Keep pushing harder."
    else:
        return "F", "Don't lose hope. Work hard and you will succeed!"

def main():
    print("--- Student Grade Calculator ---")
    
    # Get student name
    name = input("Enter student name: ")

    # Input Validation Loop (Requirement: Use while loop to handle invalid inputs)
    while True:
        try:
            user_input = input("Enter marks (0-100): ")
            marks = float(user_input)
            
            # Check if marks are within valid range
            if 0 <= marks <= 100:
                break # Exit the loop if input is valid
            else:
                print("Invalid input! Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # Get grade and message using our function
    grade, message = determine_grade(marks)

    # Print Result (Matching the Sample Output format)
    print("\n📊 RESULT FOR " + name.upper() + ":")
    print(f"Marks: {int(marks)}/100")
    print(f"Grade: {grade}")
    print(f"Message: {message} 👍")

# Run the program
if __name__ == "__main__":
    main()