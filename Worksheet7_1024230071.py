

def print_board(board):
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == player:
            return True
    return False

def check_tie(board):
    return " " not in board

def get_player_input(player, board):
    while True:
        try:
            pos = int(input(f"Player {player}, enter position (1-9): "))
            if pos < 1 or pos > 9:
                print("Invalid position! Choose between 1-9.")
            elif board[pos-1] != " ":
                print("Position already taken!")
            else:
                return pos - 1
        except:
            print("Enter a number only!")

def play_game():
    while True:
        board = [" "] * 9
        current_player = "X"
        print("Welcome to Tic-Tac-Toe!")

        while True:
            print_board(board)
            pos = get_player_input(current_player, board)
            board[pos] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break

            if check_tie(board):
                print_board(board)
                print("It's a tie!")
                break

            current_player = "O" if current_player == "X" else "X"

        again = input("Play again? (y/n): ")
        if again.lower() != "y":
            print("Thanks for playing!")
            break

# PROJECT 2: TO-DO LIST

tasks = []

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added!")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i}. {task}")
        print()

def delete_task():
    view_tasks()
    if len(tasks) == 0:
        return
    try:
        index = int(input("Enter task index to delete: "))
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Removed: {removed}")
        else:
            print("Invalid index!")
    except:
        print("Enter a valid number!")

def todo_main():
    while True:
        print("\n------ TO-DO LIST MENU ------")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Exiting To-Do App!")
            break
        else:
            print("Invalid choice!")

# PROJECT 3: ROBOT PATH PLANNING A*

import numpy as np
import heapq
import pandas as pd
import matplotlib.pyplot as plt

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_neighbors(node, grid):
    rows, cols = grid.shape
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    neighbors = []
    for d in dirs:
        nr, nc = node[0] + d[0], node[1] + d[1]
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
            neighbors.append((nr, nc))
    return neighbors

def a_star(grid, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    g_score = {start: 0}

    while open_list:
        current = heapq.heappop(open_list)[1]
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]
        for neighbor in get_neighbors(current, grid):
            tentative_g = g_score[current] + 1
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score, neighbor))
                came_from[neighbor] = current
    return None

def robot_main():
    while True:
        rows = int(input("Enter grid rows: "))
        cols = int(input("Enter grid cols: "))
        grid = np.zeros((rows, cols), dtype=int)

        obs = int(input("Enter number of obstacles: "))
        for _ in range(obs):
            r, c = map(int, input("Enter obstacle row col: ").split())
            grid[r][c] = 1

        print("\nGrid:")
        print(pd.DataFrame(grid))

        start = tuple(map(int, input("Enter start (r c): ").split()))
        goal = tuple(map(int, input("Enter goal (r c): ").split()))

        path = a_star(grid, start, goal)

        if not path:
            print("No path found!")
        else:
            print("Path:", path)
            for r, c in path:
                grid[r][c] = 2

            plt.imshow(grid, cmap="gray_r")
            plt.scatter(start[1], start[0], s=200, marker="o", label="Start")
            plt.scatter(goal[1], goal[0], s=200, marker="x", label="Goal")
            plt.legend()
            plt.title("Robot Path Planning")
            plt.show()

        again = input("Run again? (y/n): ")
        if again.lower() != "y":
            break

# MAIN MENU

def main():
    while True:
        print("\n========= MAIN MENU =========")
        print("1. Tic Tac Toe")
        print("2. To-Do List App")
        print("3. Robot Path Planning")
        print("4. Exit Program")
        choice = input("Select option: ")

        if choice == "1":
            play_game()
        elif choice == "2":
            todo_main()
        elif choice == "3":
            robot_main()
        elif choice == "4":
            print("Exiting Program!")
            break
        else:
            print("Invalid choice!")

Uncomment to run automatically:
main()
