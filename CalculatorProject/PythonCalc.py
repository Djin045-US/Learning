def get_number(prompt):
	while True:
		try:
			return float(input(prompt))
		except ValueError:
			print("Please enter a valid number.")


def main():
	while True:
		print("\nCalculator")
		print("1. Add")
		print("2. Subtract")
		print("3. Multiply")
		print("4. Divide")
		print("q. Quit")

		choice = input("Choose an operation: ").strip().lower()

		if choice == "q":
			print("Goodbye!")
			break

		if choice not in {"1", "2", "3", "4"}:
			print("Please choose 1, 2, 3, 4, or q.")
			continue

		first_number = get_number("Enter the first number: ")
		second_number = get_number("Enter the second number: ")

		if choice == "1":
			result = first_number + second_number
			operation = "+"
		elif choice == "2":
			result = first_number - second_number
			operation = "-"
		elif choice == "3":
			result = first_number * second_number
			operation = "*"
		elif second_number == 0:
			print("Cannot divide by zero.")
			continue
		else:
			result = first_number / second_number
			operation = "/"

		print(f"Result: {first_number:g} {operation} {second_number:g} = {result:g}")


if __name__ == "__main__":
	main()
