from shortest_path_solver import solve_shortest_path
from dp_solver import solve_dynamic_programming

def print_results(method, cost, aligned1, aligned2):
    """Prints the formatted results from a solver."""
    print("\n" + "="*40)
    print(f"Algorithm: {method}")
    print("="*40)
    print(f"The minimum alignment cost is: {cost}")
    print("Optimal Alignment:")
    print(f"  String 1: {aligned1}")
    print(f"  String 2: {aligned2}")
    print("="*40 + "\n")

def main():
    """Main function to run the string alignment tool."""
    print("--- String Alignment & Edit Distance Calculator ---")
    
    # Simplified input for clarity
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")

    while True:
        print("\nPlease choose an algorithm to solve:")
        print("  1. Shortest Path (A* Search)")
        print("  2. Dynamic Programming (Classic Edit Distance)")
        print("  3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            cost, aligned1, aligned2 = solve_shortest_path(string1, string2)
            print_results("Shortest Path (A*)", cost, aligned1, aligned2)
        elif choice == '2':
            cost, aligned1, aligned2 = solve_dynamic_programming(string1, string2)
            print_results("Dynamic Programming", cost, aligned1, aligned2)
        elif choice == '3':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == '__main__':
    main()