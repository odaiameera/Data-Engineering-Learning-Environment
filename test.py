# Simple calculation script
def calculate(a, b):
    """Calculate the sum of two numbers"""
    result = a + b
    return result

# Main execution
if __name__ == "__main__":
    num1 = 10
    num2 = 20
    answer = calculate(num1, num2)
    print(f"The sum of {num1} and {num2} is: {answer}")