#A poorly written example of a program in Python. It prompts the user for the number of elements to sum, takes those integers as input, and handles some basic error cases

MAX = 100  # Maximum allowed number of elements

def calculate_sum(arr):
   # Calculate the sum of all elements in the array
   result = 0
   for num in arr:
      result += num
   return result

def main():
   try:
      # Prompt user for the number of elements to sum
      n = int(input("Enter the number of elements (1-100): "))
      if not 1 <= n <= MAX:
         print("Invalid input. Please provide a digit ranging from 1 to 100.")
         exit(1)

      arr = []  # List to store user input integers

      # Loop to get each integer from the user
      for i in range(n):
         while True:
            try:
               user_input = input(f"Enter integer #{i+1}: ")
               num = int(user_input.strip())
               arr.append(num)
               break  # Exit the loop if input is valid
            except ValueError:
               print("Invalid input. Please enter a valid integer:")

      total = calculate_sum(arr)  # Calculate the sum

      print("Sum of the numbers:", total)

   except KeyboardInterrupt:
      # Handle user interrupt (Ctrl+C)
      print("\nProgram terminated by user.")
      exit(1)

if __name__ == "__main__":
   main()
