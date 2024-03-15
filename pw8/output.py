import curses

def display_gpa_table(sorted_students):
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

    try:
        while True:
            stdscr.clear()
            stdscr.addstr(0, 0, "GPA Table")
            stdscr.addstr(2, 0, "Rank\tName\t\tGPA")
            for i, student in enumerate(sorted_students):
                stdscr.addstr(3 + i, 0, f"{i + 1}\t{student.name.ljust(20)}\t{student.calculate_gpa():.2f}")

            stdscr.addstr(len(sorted_students) + 4, 0, "Press q to quit...")
            stdscr.refresh()

            c = stdscr.getch()
            if c == ord('q'):
                break
    finally:
        curses.echo()
        curses.nocbreak()
        stdscr.keypad(False)
        curses.endwin()
