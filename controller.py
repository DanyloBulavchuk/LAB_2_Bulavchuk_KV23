from model import Model
from view import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        while True:
            choice = self.show_menu()
            if choice == '1':
                self.add_user()
            elif choice == '2':
                self.view_users()
            elif choice == '3':
                self.update_user()
            elif choice == '4':
                self.delete_user()
            elif choice == '5':
                self.add_achievement()
            elif choice == '6':
                self.view_achievements()
            elif choice == '7':
                self.update_achievement()
            elif choice == '8':
                self.delete_achievement()
            elif choice == '9':
                self.add_goal()
            elif choice == '10':
                self.view_goals()
            elif choice == '11':
                self.update_goal()
            elif choice == '12':
                self.delete_goal()
            elif choice == '13':
                self.add_tracking()
            elif choice == '14':
                self.view_tracking()
            elif choice == '15':
                self.update_tracking()
            elif choice == '16':
                self.delete_tracking()
            elif choice == '17':
                self.add_app()
            elif choice == '18':
                self.view_apps()
            elif choice == '19':
                self.update_app()
            elif choice == '20':
                self.delete_app()
            elif choice == '21':
                rows = self.view.get_row_count()
                self.generate_random_data(rows)
            elif choice == '22':
                self.search_user_and_achievement()
            elif choice == '23':
                self.search_app_and_goal()
            elif choice == '24':
                self.search_tracking_and_goal()
            elif choice == '25':
                break

    def show_menu(self):
        self.view.show_message("\nMenu:")
        self.view.show_message("1. Add User")
        self.view.show_message("2. View Users")
        self.view.show_message("3. Update User")
        self.view.show_message("4. Delete User")
        self.view.show_message("5. Add Achievement")
        self.view.show_message("6. View Achievements")
        self.view.show_message("7. Update Achievement")
        self.view.show_message("8. Delete Achievement")
        self.view.show_message("9. Add Goal")
        self.view.show_message("10. View Goals")
        self.view.show_message("11. Update Goal")
        self.view.show_message("12. Delete Goal")
        self.view.show_message("13. Add Tracking")
        self.view.show_message("14. View Tracking")
        self.view.show_message("15. Update Tracking")
        self.view.show_message("16. Delete Tracking")
        self.view.show_message("17. Add App")
        self.view.show_message("18. View Apps")
        self.view.show_message("19. Update App")
        self.view.show_message("20. Delete App")
        self.view.show_message("21. Generate Random Data")
        self.view.show_message("22. Search by User and Achievement")
        self.view.show_message("23. Search by App and Goal")
        self.view.show_message("24. Search by Tracking and Goal")
        self.view.show_message("25. Quit")
        return input("Enter your choice: ")

    def add_user(self):
        try:
            name, sex, age, weight = self.view.get_user_input()
            self.model.add_user(name, sex, age, weight)
            self.view.show_message("User added successfully!")
        except Exception as e:
            self.model.abort()
            self.view.show_message(f"Error adding user: {str(e)}")

    def view_users(self):
        users = self.model.get_users()
        self.view.show_users(users)

    def update_user(self):
        try:
            user_id = self.view.get_user_id()
            name, sex, age, weight = self.view.get_user_input()
            self.model.update_user(user_id, name, sex, age, weight)
            self.view.show_message("User updated successfully!")
        except Exception as e:
            self.model.abort()
            self.view.show_message(f"Error updating user: {str(e)}")

    def delete_user(self):
        try:
            user_id = self.view.get_user_id()
            self.model.delete_user(user_id)
            self.view.show_message("User deleted successfully!")
        except Exception as e:
            self.model.abort()
            self.view.show_message(f"Error deleting user: {str(e)}")

    def add_achievement(self):
        try:
            start_time, ach_time, user_id = self.view.get_achievement_input()
            self.model.add_achievement(start_time, ach_time, user_id)
            self.view.show_message("Achievement added successfully!")
        except Exception as e:
            self.model.abort()
            self.view.show_message(f"Error adding achievement: {str(e)}")

    def view_achievements(self):
        achievements = self.model.get_achievements()
        self.view.show_achievements(achievements)

    def update_achievement(self):
        try:
            start_time = self.view.get_string_input("Enter start time: ")
            ach_time, user_id = self.view.get_achievement_update_input()
            self.model.update_achievement(start_time, ach_time, user_id)
            self.view.show_message("Achievement updated successfully!")
        except Exception as e:
            self.model.abort()
            self.view.show_message(f"Error updating achievement: {str(e)}")

    def delete_achievement(self):
        try:
            start_time = self.view.get_string_input("Enter start time: ")
            self.model.delete_achievement(start_time)
            self.view.show_message("Achievement deleted successfully!")
        except Exception as e:
            self.model.abort()
            self.view.show_message(f"Error deleting achievement: {str(e)}")

    def add_goal(self):
        try:
            goal_id, start_time, app_id, kind, priority = self.view.get_goal_input()
            self.model.add_goal(goal_id, start_time, app_id, kind, priority)
            self.view.show_message("Goal added successfully!")
        except Exception as e:
            self.model.abort()
            self.view.show_message(f"Error adding goal: {str(e)}")

    def view_goals(self):
        goals = self.model.get_goals()
        self.view.show_goals(goals)

    def update_goal(self):
        try:
            goal_id = self.view.get_int_input("Enter goal ID: ")
            start_time, app_id, kind, priority = self.view.get_goal_update_input()
            self.model.update_goal(goal_id, start_time, app_id, kind, priority)
            self.view.show_message("Goal updated successfully!")
        except Exception as e:
            self.model.abort()
            self.view.show_message(f"Error updating goal: {str(e)}")

    def delete_goal(self):
        try:
            goal_id = self.view.get_int_input("Enter goal ID: ")
            self.model.delete_goal(goal_id)
            self.view.show_message("Goal deleted successfully!")
        except Exception as e:
            self.model.abort()
            self.view.show_message(f"Error deleting goal: {str(e)}")

    def add_tracking(self):
        try:
            title, app_id, goal_id, sleep, calories = self.view.get_tracking_input()
            self.model.add_tracking(title, app_id, goal_id, sleep, calories)
            self.view.show_message("Tracking data added successfully!")
        except Exception as e:
            self.model.abort()
            self.view.show_message(f"Error adding tracking: {str(e)}")

    def view_tracking(self):
        tracking = self.model.get_tracking()
        self.view.show_tracking(tracking)

    def update_tracking(self):
        try:
            title = self.view.get_string_input("Enter tracking title: ")
            app_id, goal_id, sleep, calories = self.view.get_tracking_update_input()
            self.model.update_tracking(title, app_id, goal_id, sleep, calories)
            self.view.show_message("Tracking data updated successfully!")
        except Exception as e:
            self.model.abort()
            self.view.show_message(f"Error updating tracking: {str(e)}")

    def delete_tracking(self):
        try:
            title = self.view.get_string_input("Enter tracking title: ")
            self.model.delete_tracking(title)
            self.view.show_message("Tracking data deleted successfully!")
        except Exception as e:
            self.model.abort()
            self.view.show_message(f"Error deleting tracking: {str(e)}")

    def add_app(self):
        try:
            app_id, version, rate, price = self.view.get_app_input()
            self.model.add_app(app_id, version, rate, price)
            self.view.show_message("App added successfully!")
        except Exception as e:
            self.model.abort()
            self.view.show_message(f"Error adding app: {str(e)}")

    def view_apps(self):
        apps = self.model.get_apps()
        self.view.show_apps(apps)

    def update_app(self):
        try:
            app_id = self.view.get_int_input("Enter app ID: ")
            version, rate, price = self.view.get_app_update_input()
            self.model.update_app(app_id, version, rate, price)
            self.view.show_message("App updated successfully!")
        except Exception as e:
            self.model.abort()
            self.view.show_message(f"Error updating app: {str(e)}")

    def delete_app(self):
        try:
            app_id = self.view.get_int_input("Enter app ID: ")
            self.model.delete_app(app_id)
            self.view.show_message("App deleted successfully!")
        except Exception as e:
            self.model.abort()
            self.view.show_message(f"Error deleting app: {str(e)}")

    def generate_random_data(self, rows):
        self.model.generate_random_data(rows)
        self.view.show_message(f"Random data generation for {rows} rows completed successfully!")

    def search_user_and_achievement(self):
        try:
            user_name_pattern = self.view.get_string_input("Enter user name pattern (e.g., %John%): ")
            min_weight = self.view.get_int_input("Enter minimum weight: ")
            max_weight = self.view.get_int_input("Enter maximum weight: ")
            results, elapsed_time = self.model.search_by_user_and_achievement(user_name_pattern, min_weight, max_weight)
            self.view.show_results(results)
            self.view.show_message(f"Query executed in {elapsed_time:.2f} ms.")
        except Exception as e:
            self.model.abort()
            self.view.show_message(f"Error searching by user and achievement: {str(e)}")

    def search_app_and_goal(self):
        try:
            min_version = self.view.get_int_input("Enter minimum app version: ")
            max_version = self.view.get_int_input("Enter maximum app version: ")
            goal_kind = self.view.get_string_input("Enter goal kind pattern (e.g., %Fitness%): ")
            results, elapsed_time = self.model.search_by_app_and_goal(min_version, max_version, goal_kind)
            self.view.show_results(results)
            self.view.show_message(f"Query executed in {elapsed_time:.2f} ms.")
        except Exception as e:
            self.model.abort()
            self.view.show_message(f"Error searching by app and goal: {str(e)}")

    def search_tracking_and_goal(self):
        try:
            sleep_pattern = self.view.get_string_input("Enter sleep pattern (e.g., %hours%): ")
            min_calories = self.view.get_int_input("Enter minimum calories: ")
            max_calories = self.view.get_int_input("Enter maximum calories: ")
            results, elapsed_time = self.model.search_by_tracking_and_goal(sleep_pattern, min_calories, max_calories)
            self.view.show_results(results)
            self.view.show_message(f"Query executed in {elapsed_time:.2f} ms.")
        except Exception as e:
            self.model.abort()
            self.view.show_message(f"Error searching by tracking and goal: {str(e)}")
