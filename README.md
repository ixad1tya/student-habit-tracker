# Smart Student Habit Tracker

**Domain:** Productivity & Self-Improvement  
**Course:** Vityarthi Python Programming

---

## Phase 1: Problem Definition

### Real-World Problem
University students often struggle to maintain consistency with their studies, hobbies, and health routines. Without a system to track progress, it is easy to lose motivation or forget daily tasks, leading to poor time management and lack of discipline.

### Objective
To develop a command-line interface (CLI) application that allows students to define habits, log their daily completion status (including time spent), and generate reports to visualize their consistency and productivity.

---

## Phase 2: Requirement Analysis
To solve this problem, the system requires the following features:

1. **Habit Management:** The user must be able to Add (with a limit of 15), Edit, and View habits with categories.
2. **Daily Logging:** A mechanism to log specific dates, mark habits as completed/missed, and record hours spent.
3. **Data Persistence:** The data must be saved to a JSON file (`habits_data.json`) so records and structure are preserved between sessions.
4. **Analytics:** The system must calculate "Consistency %" for daily and weekly reports.
5. **Feedback:** The system should provide feedback (e.g., "Great", "Improve") based on performance percentages.

---

## Phase 3: Top-Down Design (Modularization)
We will break the program into specific functions to handle logic and file operations efficiently.

* `main_program()`: The central controller that loads data, displays the menu, and handles user choices.
* `load_data_file()` & `save_everything()`: Handles JSON file input/output to ensure data persistence.
* `add_new_habit()`: Validates limits and appends new habits to the list.
* `edit_some_habit()`: Allows modification of existing habit names or categories.
* `log_habit_day()`: Records completion status and time spent for a specific date.
* `show_daily_report()`: Calculates the completion percentage for a single date.
* `week_report()`: Aggregates data over 7 user-provided dates to calculate a weekly average.

---

## Phase 4: Algorithm Development (Pseudocode)

```text
START
  Load data from 'habits_data.json' (Create empty structure if missing)
  LOOP forever:
    Display Menu (1. Add, 2. Edit, 3. View, 4. Log, 5. Daily Report, 6. Weekly Report, 0. Exit)
    Get User Choice
    IF Choice is 1:
      If habit count < 15:
        Get Name and Category
        Add to habit list and Save
    ELSE IF Choice is 2:
      Display habits
      Select habit index
      Update Name/Category if input provided
      Save
    ELSE IF Choice is 4:
      Get Date
      For each habit:
        Ask if completed (y/n)
        If yes, ask for hours spent
      Save log to database under Date key
    ELSE IF Choice is 5:
      Get Date
      Calculate (Completed Habits / Total Habits) * 100
      Print Consistency Score and Feedback
    ELSE IF Choice is 6:
      Get 7 Dates from user
      Calculate average consistency across those dates
      Print Weekly Status
    ELSE IF Choice is 0:
      Break Loop
  END LOOP
STOP
```
### Phase 5: Implementation (Python Code)
--- 
It is in the file named “Habit_Tracker.py”

### Phase 6: Testing and Refinement
---
When we run the code, we should perform these tests to ensure it works correctly.

**Test Case 1: Input Validation (Hours)**

Action: Select "Log Habit Completion". Mark a habit as done ('y'), then enter "two" when asked for "Hours spent".

Expected Result: The program should catch the exception, print "Invalid hours," and treat the time spent as 0, rather than crashing.

**Test Case 2: Logic & Calculation** 

Action: Create 2 habits. Log a day where you complete 1 habit but miss the other. Run "Daily Report".

Expected Result: The report should show "Total: 2", "Done: 1", and "Consistency: 50.0%".

**Test Case 3: Persistence***

Action: Add a habit named "Python Practice". Exit the program. Run it again and select "View Habits".

Expected Result: "Python Practice" should appear in the list, loaded from habits_data.json.
---
### Note:- The screenshot of the testing, refinement and how to run code are attached in the file named "screenshot.md"
