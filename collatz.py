def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1
def main():
    try:
        user_input = int(input("Enter a number: "))
        current_value = user_input
        while current_value != 1:
            current_value = collatz(current_value)
            print(current_value)
    except ValueError:
        print("input must be a valid integer")
if __name__ == "__main__":
    main() 