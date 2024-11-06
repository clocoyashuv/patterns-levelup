class SingletonObject:
    # Class-level variable to store the single instance
    _instance = None

    # Private constructor
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonObject, cls).__new__(cls)
        return cls._instance

    # Method to print a message
    def print_message(self):
        print("Hello from Singleton object!!!")

# Main function to demonstrate the Singleton pattern
if __name__ == "__main__":
    # Get the single instance of SingletonObject
    object1 = SingletonObject()
    object2 = SingletonObject()

    # Show the message
    object1.print_message()

    # Demonstrate that both references point to the same instance
    print(f"object1 is object2: {object1 is object2}")