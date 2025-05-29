import tkinter as tk
from tkinter import messagebox
from sympy import symbols, cos, sin, nsolve
from mpmath import radians
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def solve_and_plot():
    try:
        v0 = float(entry_v0.get())
        u = float(entry_u.get())
        cte = float(entry_cte.get())
        c = float(entry_c.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for all fields.")
        return

    a, b, t = symbols('a b t', real=True)
    eq_x = -22.5 + v0 * cos(radians(a)) * sin(radians(b)) * t + cte * u * t * sin(radians(c))
    eq_y = -0 + v0 * cos(radians(a)) * cos(radians(b)) * t + cte * u * t * cos(radians(c))
    eq_z = -5.97 + v0 * sin(radians(a)) * t - 0.5 * 9.81 * t ** 2

    try:
        solution = nsolve((eq_x, eq_y, eq_z), (a, b, t), (45, 45, 2))
        a_res, b_res, t_res = [float(val) for val in solution]
    except Exception as e:
        messagebox.showerror("Solver Error", f"Could not solve the system:\n{e}")
        return

    # Normalize angles
    a_res = a_res % 360
    b_res = b_res % 360

    result = (
        f"Ángulo de disparo a = {a_res:.2f}°\n"
        f"Ángulo de compensación lateral b = {b_res:.2f}°\n"
        f"Tiempo de trayectoria = {t_res:.2f} s"
    )
    result_label.config(text=result)

    # Plot trajectory
    steps = 100
    t_vals = np.linspace(0, t_res, steps)
    x_vals = -22.5 + v0 * np.cos(np.radians(a_res)) * np.sin(np.radians(b_res)) * t_vals + cte * u * t_vals * np.sin(np.radians(c))
    y_vals = 0 + v0 * np.cos(np.radians(a_res)) * np.cos(np.radians(b_res)) * t_vals + cte * u * t_vals * np.cos(np.radians(c))
    z_vals = -5.97 + v0 * np.sin(np.radians(a_res)) * t_vals - 0.5 * 9.81 * t_vals ** 2

    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x_vals, y_vals, z_vals, label='Trayectoria', color='#00B8D9')
    ax.scatter([x_vals[-1]], [y_vals[-1]], [z_vals[-1]], color='red', label='Gol')
    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    ax.set_zlabel('Z (m)')
    ax.set_title('Trayectoria del balón')
    ax.legend()

    # Dibuja la portería (centrada en Y=0, en X=30)
    poste_x = [30, 30, 30, 30, 30]
    poste_y = [-7.32/2, 7.32/2, 7.32/2, -7.32/2, -7.32/2]
    poste_z = [0, 0, 2.44, 2.44, 0]
    # Base
    ax.plot([poste_x[0], poste_x[1]], [poste_y[0], poste_y[1]], [poste_z[0], poste_z[1]], color='gold', linewidth=3)
    # Poste derecho
    ax.plot([poste_x[1], poste_x[2]], [poste_y[1], poste_y[2]], [poste_z[1], poste_z[2]], color='gold', linewidth=3)
    # Traversa
    ax.plot([poste_x[2], poste_x[3]], [poste_y[2], poste_y[3]], [poste_z[2], poste_z[3]], color='gold', linewidth=3)
    # Poste izquierdo
    ax.plot([poste_x[3], poste_x[4]], [poste_y[3], poste_y[4]], [poste_z[3], poste_z[4]], color='gold', linewidth=3)

    plt.tight_layout()
    plt.show()

# --- GUI ---
root = tk.Tk()
root.title("Simulador de Gol 3D")
root.geometry("400x350")
root.configure(bg="#181A1B")

font_label = ("Consolas", 12)
font_entry = ("Consolas", 12)
accent = "#00B8D9"

tk.Label(root, text="Simulador de Gol 3D", font=("Consolas", 16, "bold"), fg=accent, bg="#181A1B").pack(pady=10)

frame = tk.Frame(root, bg="#181A1B")
frame.pack(pady=10)

tk.Label(frame, text="Velocidad inicial v0 (m/s):", font=font_label, bg="#181A1B", fg="#E6E6E6").grid(row=0, column=0, sticky="e", pady=4)
entry_v0 = tk.Entry(frame, font=font_entry, bg="#232526", fg="#E6E6E6", insertbackground=accent, width=10)
entry_v0.grid(row=0, column=1, pady=4)

tk.Label(frame, text="Velocidad viento u (m/s):", font=font_label, bg="#181A1B", fg="#E6E6E6").grid(row=1, column=0, sticky="e", pady=4)
entry_u = tk.Entry(frame, font=font_entry, bg="#232526", fg="#E6E6E6", insertbackground=accent, width=10)
entry_u.grid(row=1, column=1, pady=4)

tk.Label(frame, text="Constante arrastre cte:", font=font_label, bg="#181A1B", fg="#E6E6E6").grid(row=2, column=0, sticky="e", pady=4)
entry_cte = tk.Entry(frame, font=font_entry, bg="#232526", fg="#E6E6E6", insertbackground=accent, width=10)
entry_cte.grid(row=2, column=1, pady=4)

tk.Label(frame, text="Ángulo viento c (°):", font=font_label, bg="#181A1B", fg="#E6E6E6").grid(row=3, column=0, sticky="e", pady=4)
entry_c = tk.Entry(frame, font=font_entry, bg="#232526", fg="#E6E6E6", insertbackground=accent, width=10)
entry_c.grid(row=3, column=1, pady=4)

tk.Button(root, text="Calcular y Graficar", command=solve_and_plot, font=("Consolas", 13, "bold"),
          bg=accent, fg="#181A1B", activebackground=accent, activeforeground="#181A1B", bd=0, relief="flat", padx=10, pady=8).pack(pady=18)

result_label = tk.Label(root, text="", font=("Consolas", 12), bg="#181A1B", fg=accent, justify="left")
result_label.pack(pady=10)

root.mainloop()