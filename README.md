# 🏈 Field Goal Kicker: 3D Parabolic Motion Modeling with Wind Compensation

## 👥 Authors

* Mauricio Monroy A01029647
* Ana Maria Franco A01785354

## 📝 Project Overview

This project focuses on the development of a physical launcher and a 3D simulation to study the parabolic motion of projectiles, specifically modeling a field goal kick under varying wind conditions. Our primary objective was to build a system capable of accurately launching ping-pong balls and then analyze their trajectory, incorporating the complexities of wind influence in a 3D environment. This tool aims to provide a robust platform for understanding the principles of parabolic motion, evaluating the impact of launch angle, initial velocity, and projectile mass, and offering a repeatable experimental setup.

🏆 **This project won 3rd place in Tecnológico de Monterrey's Expo Ingenierías 2023, in the category of Basic Physical Prototype.**

## ✨ Features

* **Physical Launcher Prototype:** A 3D-printed device designed for precise projectile launches, allowing for repeatable experiments and data collection.
* **Adjustable Launch Parameters:** The physical launcher is designed to control and adjust multiple parameters, including launch angle and initial velocity.
* **3D GeoGebra Simulator:** A detailed simulation of parabolic trajectory using GeoGebra, incorporating parametric equations and sliders for adjusting wind conditions (velocity and angle).
* **Vector-based Goal Post Modeling:** The simulator includes a static representation of a goal post using fixed vectors, allowing for visual tracing of the projectile's path relative to the target.
* **Python Calculation & Visualization Program:** A Python script with a GUI that calculates optimal launch angles (vertical and lateral compensation) and trajectory time, given environmental parameters like wind velocity and direction. The program also generates a 3D plot of the ball's trajectory, vectors, and the goal post for visual analysis.

## ⚙️ Technical Details

### Methodology

The project's development involved a strong understanding of kinematic equations and external factors such as wind velocity. The physical prototype's design required considerations for Hooke's Law to select an appropriate spring.

Key equations utilized:
* Kinematic equations for projectile motion.
* Force equations incorporating mass, gravity, spring force (Hooke's Law), and kinetic friction.
* Equations for final velocity derived from the work-energy theorem.

### Physical Prototype Development

The launcher's design was created using Tinkercad, a 3D modeling tool. Following the design phase, the launcher was 3D printed. A spring with an elastic constant of 2.77 N/m was chosen to balance manual compression ease with necessary launching power. Due to its small size, two springs were tied in series to achieve the required length for an effective launch.

### 3D Simulator Development

The simulation in GeoGebra required adjusting kinematic equations to a 3D Cartesian coordinate system. A hypothetical goal post was "drawn" using fixed vectors based on real-world measurements. New parameters like wind speed, wind angle, and a "kick angle" for wind compensation were introduced.

### Results

The theoretical maximum launch velocity calculated from the spring constant was 2.08 ms⁻¹, which differed by 20.78% from the experimental value of 2.51 ms⁻¹ obtained using Tracker. The Python program, receiving wind data, approximates the required kick angles and adjustments, which are then visualized in the GeoGebra simulator.

---

## 🐍 Python Program

This Python script provides a **graphical interface** to calculate the optimal launch and compensation angles for a field goal kick, considering wind conditions, and displays a 3D visualization of the trajectory, vectors, and the goal post.

### 🧩 Dependencies

* `sympy`
* `mpmath`
* `numpy`
* `matplotlib`

### 🚀 How to Run

1.  Make sure you have the required libraries installed:
    ```bash
    pip install sympy mpmath numpy matplotlib
    ```
2.  Save the provided Python code as `testretoexpo.py`.
3.  Run the script from your terminal:
    ```bash
    python testretoexpo.py
    ```
4.  The program will open a window where you can enter:
    * `v0`: Initial velocity of the kick (m/s)
    * `u`: Wind velocity (m/s)
    * `cte`: Drag constant of the wind (between 0 and 1)
    * `c`: Wind direction angle (0-360 degrees)
5.  Click **"Calcular y Graficar"**. The program will:
    - Show the calculated optimal vertical launch angle (`a`), lateral compensation angle (`b`), and total time of flight (`t`).
    - Display a 3D plot with:
        - The full ball trajectory (cyan line)
        - The goal post (gold)
        - The initial velocity vector (lime)
        - The wind vector (orange)
        - The goal point (red dot)

### 🖥️ Code Explanation

- The script uses `sympy` for symbolic mathematics to solve a system of three parametric equations representing the projectile's trajectory in 3D space (`x`, `y`, `z` coordinates).
- The GUI is built with `tkinter` for easy parameter input.
- The 3D plot is generated with `matplotlib`, showing the trajectory, vectors, and the goal post for clear visual analysis.
- The output provides the calculated optimal vertical launch angle (`a`), lateral compensation angle (`b`), and the total time of flight (`t`).

---

## 🔮 Future Improvements

* **Physical Launcher Precision:** Enhance the quality of 3D printing for the launcher's components (e.g., the lever mechanism) to achieve more precise and consistent launches.
* **Simulator Control:** Improve user control over parameters and data input within the GeoGebra simulator for a more user-friendly experience.
* **Numerical Accuracy:** Refine the program's approximation methods for trigonometric functions to provide more accurate predictions rather than approximations, addressing current inaccuracies in the output information.
* **Enhanced Visualization:** Add animation of the ball, more realistic field elements, or export options for further analysis.

---

**Note:** This README is based on the provided poster content and Python code. Further details on specific mathematical derivations or experimental setups might be found in the full project report.
