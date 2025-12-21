import os
import sys
from mobile_app_react_native.config import Config
from mobile_app_react_native.services import UserService, NotificationService

class MobileApp:
    def __init__(self):
        self.config = Config()
        self.user_service = UserService()
        self.notification_service = NotificationService()

    def run(self):
        try:
            # Load user data
            user_data = self.user_service.get_user_data()
            if user_data:
                # Initialize notification service
                self.notification_service.initialize()
                # Start the app
                print("Mobile app started successfully")
            else:
                print("Failed to load user data")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app = MobileApp()
    app.run()