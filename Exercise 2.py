def print_triangle(lines):

    for i in range(1, lines):
        # Calculate number of tabs to print based on the current line
        tabs = lines - i
        # Print the tabs first
        for t in range(tabs):
            print("\t", end="")
        # Print each line's star and the ensuing tab after the star
        for j in range(0, i):
            print("*\t\t", end="")
        # Print new line to begin next line on triangle
            print("\n")
            lines = 10
            print_triangle(lines)


