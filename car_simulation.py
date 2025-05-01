import time
import msvcrt
import os

SAVE_FILE = "odometer.txt"

class Car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
        self.speed = 5
        self.odometer = self.load_odometer()
        self.engine_on = False

    def start_engine(self):
        self.engine_on = True
        print(f"🚗 {self.name} engine started at {self.speed} m/s.")

    def stop_engine(self):
        self.engine_on = False
        print(f"🛑 {self.name} engine stopped.")

    def update_odometer(self, seconds):
        self.odometer += self.speed * seconds
        self.save_odometer()

    def change_speed(self, new_speed):
        self.speed = new_speed
        print(f"⚙️ Speed changed to {self.speed} m/s.")

    def inspect(self):
        os.system('cls')
        return (
            f"\n🔍 Car Info:\n"
            f"Name: {self.name}\n"
            f"Model: {self.model}\n"
            f"Year: {self.year}\n"
            f"Total Distance: {self.odometer} meters\n"
            f"Current Speed: {self.speed} m/s\n"
            f"Engine Status: {'Running' if self.engine_on else 'Stopped'}"
        )

    def save_odometer(self):
        with open(SAVE_FILE, 'w') as f:
            f.write(str(self.odometer))

    def load_odometer(self):
        if os.path.exists(SAVE_FILE):
            with open(SAVE_FILE, 'r') as f:
                return int(f.read().strip())
        return 0

def drive_menu(car):
    while True:
        
        print("\n🚦 1. Start Car\n⚙️ 2. Change Speed\n🛑 3. Stop Car\n🔍 4. Inspect Car\n⬅️ 5. Return to Main Menu")
        choice = input("Choose an option: ")

        if choice == "1":
            os.system('cls')
            car.start_engine()
            print("Press ENTER to stop driving.")
            counter = 1
            while car.engine_on:
                if msvcrt.kbhit() and msvcrt.getch() == b'\r':
                    car.stop_engine()
                    break
                time.sleep(1)
                car.update_odometer(1)
                print(f"{counter}... done. ➤ +{car.speed}m | Total: {car.odometer}m")
                counter += 1

        elif choice == "2":
            os.system('cls')
            try:
                new_speed = int(input("Enter new speed (m/s): "))
                car.change_speed(new_speed)
            except ValueError:
                print("Speed must be an integer.")

        elif choice == "3":
            
            car.stop_engine()

        elif choice == "4":
            print(car.inspect())

        elif choice == "5":
            break
        else:
            print("Invalid option. Try again.")

def main():
    
    print("🚘 Welcome to Car Simulator")
    car = Car("Toyota", "Corolla", 2022)

    while True:
        print("\n1. Enter Drive Mode\n2. Exit")
        option = input("Select: ")

        if option == "1":
            drive_menu(car)
        elif option == "2":
            print("Goodbye 👋")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()