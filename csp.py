problem = input("Enter cryptarithm (e.g., TWO + TWO + TWO = SIX): ")

lhs, rhs = problem.replace(" ", "").split("=")
addends = lhs.split("+")
words = addends + [rhs]
letters = sorted(set("".join(words)))

def is_valid(solution):
    first_letters = [w[0] for w in words]
    for fl in first_letters:
        if fl in solution and solution[fl] == 0:
            return False
    if len(solution) < len(letters):
        return True
    numbers = [int("".join(str(solution[c]) for c in w)) for w in addends]
    result = int("".join(str(solution[c]) for c in rhs))
    return sum(numbers) == result

def solve(solution, letters_left):
    if not letters_left:
        if is_valid(solution):
            return solution
        return None
    letter = letters_left[0]
    for digit in range(10):
        if digit not in solution.values():
            solution[letter] = digit
            result = solve(solution, letters_left[1:])
            if result:
                return result
            del solution[letter]
    return None

solution = solve({}, letters)

if solution:
    print("Solution found:")
    for letter in letters:
        print(f"{letter} = {solution[letter]}")
else:
    print("No solution found.")
