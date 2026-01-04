import os
from mobile_app-react_native.config import Config
from mobile_app-react_native.utils import Logger

class Main:
    def __init__(self):
        self.config = Config()
        self.logger = Logger()

    def run(self):
        try:
            self.logger.info("Mobile App React Native started")
            # self.config.load_config()
            # self.config.save_config()
        except Exception as e:
            self.logger.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main = Main()
    main.run()