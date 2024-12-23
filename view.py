class View:
    def show_users(self, users):
        print("Users:")
        for user in users:
            print(f"ID: {user[0]}, Name: {user[1]}, Sex: {user[2]}, Age: {user[3]}, Weight: {user[4]}")

    def get_user_input(self):
        name = input("Enter user name: ")
        sex = input("Enter user sex (M/F): ")
        age = int(input("Enter user age: "))
        weight = int(input("Enter user weight: "))
        return name, sex, age, weight

    def get_user_id(self):
        return int(input("Enter user ID: "))

    def show_achievements(self, achievements):
        print("Achievements:")
        for achievement in achievements:
            print(f"Start Time: {achievement[0]}, Achievement Time: {achievement[1]}, User ID: {achievement[2]}")

    def get_achievement_input(self):
        start_time = input("Enter achievement start time: ")
        ach_time = input("Enter achievement time: ")
        user_id = int(input("Enter user ID for achievement: "))
        return start_time, ach_time, user_id

    def get_goal_input(self):
        goal_id = int(input("Enter goal ID: "))
        start_time = input("Enter start time: ")
        app_id = int(input("Enter app ID: "))
        kind = input("Enter goal kind: ")
        priority = int(input("Enter goal priority: "))
        return goal_id, start_time, app_id, kind, priority

    def show_goals(self, goals):
        print("Goals:")
        for goal in goals:
            print(f"Goal ID: {goal[0]}, Start Time: {goal[1]}, App ID: {goal[2]}, Kind: {goal[3]}, Priority: {goal[4]}")

    def get_tracking_input(self):
        title = input("Enter tracking title: ")
        app_id = int(input("Enter app ID: "))
        goal_id = int(input("Enter goal ID: "))
        sleep = input("Enter sleep data: ")
        calories = input("Enter calories data: ")
        return title, app_id, goal_id, sleep, calories

    def show_tracking(self, tracking):
        print("Tracking:")
        for track in tracking:
            print(f"Title: {track[0]}, App ID: {track[1]}, Goal ID: {track[2]}, Sleep: {track[3]}, Calories: {track[4]}")

    def show_message(self, message):
        print(message)

    def get_row_count(self):
        return int(input("Enter the number of rows to generate: "))

    def get_string_input(self, prompt):
        return input(prompt)

    def get_int_input(self, prompt):
        return int(input(prompt))

    def show_results(self, results):
        print("Results:")
        for result in results:
            print(result)
