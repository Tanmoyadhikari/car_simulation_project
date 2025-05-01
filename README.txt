===========================
Car Simulation (OOP + CLI)
===========================

📦 Description:
---------------
This project is a simple car simulation written in Python using Object-Oriented Programming (OOP). 
It allows a user to control a virtual car via a terminal interface on Windows.

⚙️ Features:
-------------
- Start and Stop the car engine
- Simulate real-time movement (m/s based)
- Dynamically update the odometer
- Change driving speed
- Inspect car details like model, speed, and distance

🖥️ Requirements:
-----------------
- Python 3.x
- Windows OS (uses `msvcrt` module)

🚗 How It Works:
-----------------
1. Run the script (`python car_simulation.py`)
2. Use the Main Menu to enter drive mode
3. Use the Drive Menu to:
   - Start the car (Press ENTER to stop)
   - Change speed
   - View inspection report
4. Car's odometer and status are updated every second while driving

📝 Note:
---------
- This script only works on Windows because it uses `msvcrt` to detect the ENTER key.
- For cross-platform simulation, use `keyboard` module or manual time-based loops.

📁 Files:
---------
- car_simulation.py → Main code
- README.txt        → Instructions and algorithm

🧠 Concepts Used:
------------------
- OOP: Classes, Objects, Encapsulation
- While loops and conditionals
- Time module for delay
- msvcrt module for Windows key press detection

✍️ Author:
-----------
Tanmoyadhikari
