# -RealTime-Process-Monitor-cd-RealTime-Process-Monitor

1. Project Overview
This project is a real-time process monitoring system developed using Python. It provides live insights into CPU and memory usage along with a dynamic table of active processes. Additionally, it features a pop-up graph window for real-time visualization of system resource usage. This tool is especially useful for developers, system administrators, and students for system diagnostics and educational purposes.
2. Module-Wise Breakdown
•	System Resource Monitor (Tkinter GUI): Displays real-time CPU and memory usage.
•	Process List Table: Dynamically updates to show all currently running processes with PID, CPU%, and Memory%.
•	Live Graph Module (Matplotlib): Opens in a separate window and shows CPU and memory trends over time.
•	Graph Launch Button: Allows the user to launch the real-time graph from the GUI.
•	Threading Module: Ensures GUI doesn’t freeze during updates.
3. Functionalities
•	Live display of CPU and memory usage
•	Live table of running processes
•	Graphical display of CPU and memory usage in real-time (separate window)
•	Multi-threaded updates to keep the GUI responsive
________________________________________
4. Technology Used
• Programming Languages:
•	Python
• Libraries and Tools:
•	psutil: For fetching system data
•	tkinter: For the GUI
•	matplotlib: For graph visualization
•	threading: For background updates
•	subprocess: To open the graph script
• Other Tools:
•	GitHub for version control


6. Revision Tracking on GitHub
•	Repository Name: RealTime-Process-Monitor
•	GitHub Link: https://github.com/Roshan2027/-RealTime-Process-Monitor-cd-RealTime-Process-Monitor
________________________________________
7. Conclusion and Future Scope
This project demonstrates how system monitoring tools can be built with Python using real-time data visualization and multi-threaded interfaces. Future enhancements could include:
•	Option to kill selected processes
•	Custom alerts and notifications
•	Save logs and trends
•	Remote monitoring over network
________________________________________
8. References
•	psutil Documentation
•	Tkinter GUI Guide
•	Matplotlib Guide

A. AI-Generated Project Elaboration/Breakdown Report
This tool combines data collection (psutil), display (tkinter), and analysis (matplotlib) in a modular design. Threading ensures the UI remains responsive even during continuous updates. The graphing tool opens in a separate process to keep the architecture clean and prevent main window lag.

B. Problem Statement
To create a real-time system monitoring tool that can track and display CPU and memory usage dynamically and also visualize the data graphically using Python.
