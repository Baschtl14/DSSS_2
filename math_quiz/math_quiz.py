import random

def function_A(min_val, max_val):
    """
    Generate a random integer between min_val and max_val (inclusive).
    """
    return random.randint(min_val, max_val)

def function_B():
    """
    Randomly select an arithmetic operator from +, -, *.
    """
    return random.choice(['+', '-', '*'])

def function_C(n1, n2, operator):
    """
    Create a math problem string and calculate the answer based on the operator.
    """
    problem = f"{n1} {operator} {n2}"
    if operator == '+':
        answer = n1 + n2
    elif operator == '-':
        answer = n1 - n2
    else:  # Multiplication
        answer = n1 * n2
    return problem, answer

def math_quiz():
    """
    Run a math quiz game where the user answers randomly generated math problems.
    """
    score = 0
    total_questions = 3  # Set to an integer for the loop

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        n1 = function_A(1, 10)
        n2 = function_A(1, 5)  # Fixed to an integer
        operator = function_B()

        problem, answer = function_C(n1, n2, operator)
        print(f"\nQuestion: {problem}")
        
        try:
            user_answer = int(input("Your answer: "))
            if user_answer == answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {answer}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
