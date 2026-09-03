import os
import sys

def main():
    print("--- Simple Python Addition Tool ---")
    
    # Automated environments (like Jenkins) can pass inputs via Env Variables to prevent freezing
    if 'NUM1' in os.environ and 'NUM2' in os.environ:
        try:
            num1 = float(os.environ['NUM1'])
            num2 = float(os.environ['NUM2'])
            print(f"Reading numbers from environment: {num1} and {num2}")
        except ValueError:
            print("Error: Invalid numbers provided in environment variables.")
            sys.exit(1)
    else:
        # Fallback values for basic script verification if no inputs are supplied
        print("No environment variables detected. Running baseline verification with default inputs.")
        num1 = 10.0
        num2 = 25.0

    total = num1 + num2
    print(f"The sum of {num1} and {num2} is: {total}")
    print("Application executed successfully!")

if __name__ == "__main__":
    main()
