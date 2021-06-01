
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from math import *

########################################################
# main()
########################################################

def main():

    ########################################################
    # handle_click()
    ########################################################

    def handle_click(min_x_control, max_x_control, min_y_control, max_y_control, x_y_option_control, x_y_equation, canvas):
        # First check min/max x/y values are floats
        (min_x, max_x, min_y, max_y) = (0.0, 0.0, 0.0, 0.0)
        try:
            min_x = float(min_x_control.get())
            max_x = float(max_x_control.get())
            min_y = float(min_y_control.get())
            max_y = float(max_y_control.get())
        except ValueError:
            messagebox.showerror("ERROR", "Unable to parse min/max values")            
            return

        # Then check min values are less than maxes
        if(min_x >= max_x) or (min_y >= max_y):
            messagebox.showerror("ERROR", "Min values must be less than max values")            
            return

        # Get the drop-down to see if we are calculating 'y' based on 'x' or vice-versa
        x_or_y = x_y_option_control.get()
        # Finally, get the actual equation string
        equation = x_y_equation.get()
        
        # Clear the canvas
        canvas.delete("all")

        # Calculate the scalar between the canvas size and the min/max dimenstions
        canvas_width = float(canvas.winfo_width())
        canvas_height = float(canvas.winfo_height())
        x_scalar = canvas_width / (max_x - min_x)
        y_scalar = canvas_height / (max_y - min_y)

        # Draw the x-axis
        canvas.create_line(0, y_scalar * min_y * -1, canvas_width, y_scalar * min_y * -1)
        
        # Draw the y-axis
        canvas.create_line(x_scalar * min_x * -1, 0, x_scalar * min_x * -1, canvas_height)

        # Draw the digits for the x-axis        
        x_scale = min_x
        x_scale_inc = (max_x - min_x)/6
        while (x_scale <= max_x):
            x_pos = x_scalar * (x_scale + (min_x * -1))
            canvas.create_text(x_pos, (y_scalar * min_y * -1) + 5, fill = "black", font = "Courier 10", text = str(round(x_scale, 2)))
            x_scale += x_scale_inc

        # Draw the digits for the y-axis        
        y_scale = min_y
        y_scale_inc = (max_y - min_y)/6
        while (y_scale <= max_y):
            y_pos = y_scalar * (y_scale + (min_y * -1))
            canvas.create_text((x_scalar * min_x * -1) + 5, y_pos, fill = "black", font = "Courier 10", text = str(round(y_scale, 2)))
            y_scale += y_scale_inc

        # Try to eval() the actual equation
        try:
            # If calculating 'y' based on 'x'...
            if x_or_y == "y = ":
                x1, y1 = 0.0, 0.0
                first = True
                for x2 in range(int(min_x), int(max_x), 1):
                    y2 = eval(equation, globals(), {"x": x2})
                    if first:
                        x1 = x_scalar * (x2 + (min_x * -1))
                        y1 = y_scalar * (y2 + (min_y * -1))
                        first = False
                    else:
                        x2 = x_scalar * (x2 + (min_x * -1))
                        y2 = y_scalar * (y2 + (min_y * -1))
                        canvas.create_line(x1, y1, x2, y2)
                        x1 = x2
                        y1 = y2
            # ...otherwise we are calculating 'x' based on 'y'
            else:
                x1, y1 = 0.0, 0.0
                first = True
                for y2 in range(int(min_y), int(max_y), 1):
                    x2 = eval(equation, globals(), {"y": y2})
                    if first:
                        x1 = x_scalar * (x2 + (min_x * -1))
                        y1 = y_scalar * (y2 + (min_y * -1))
                        first = False
                    else:
                        x2 = x_scalar * (x2 + (min_x * -1))
                        y2 = y_scalar * (y2 + (min_y * -1))
                        canvas.create_line(x1, y1, x2, y2)
                        x1 = x2
                        y1 = y2

        except:
            messagebox.showerror("ERROR", "Unable to parse: " + equation)
            return

    ########################################################
    # Actual main() method
    ########################################################

    master_window  = tk.Tk(className="graph plotter")
    
    OPTIONS = [
       "x = ",
       "y = ",
    ]

    ######################################################

    controls_frame = tk.Frame(master_window)
    controls_frame.grid(row=0, column=0, sticky=W+E)    
        
    min_x_equals_label = tk.Label(controls_frame, text = "Min x")
    min_x_equals_label.grid(row=0, column=0, padx=10, pady=10)

    min_x_entry = tk.Entry(controls_frame)
    min_x_entry.grid(row=0, column=1, padx=(10), pady=10)

    max_x_equals_label = tk.Label(controls_frame, text = "Max x")
    max_x_equals_label.grid(row=0, column=2, padx=10, pady=10)

    max_x_entry = tk.Entry(controls_frame)
    max_x_entry.grid(row=0, column=3, padx=10, pady=10)

    min_y_equals_label = tk.Label(controls_frame, text = "Min y")
    min_y_equals_label.grid(row=1, column=0, padx=10, pady=10)

    min_y_entry = tk.Entry(controls_frame)
    min_y_entry.grid(row=1, column=1, padx=10, pady=10)

    max_y_equals_label = tk.Label(controls_frame, text = "Max y")
    max_y_equals_label.grid(row=1, column=2, padx=10, pady=10)

    max_y_entry = tk.Entry(controls_frame)
    max_y_entry.grid(row=1, column=3, padx=10, pady=10)

    ######################################################

    variable = tk.StringVar(controls_frame)
    variable.set(OPTIONS[0])

    x_y_option_menu = tk.OptionMenu(controls_frame, variable, *OPTIONS)
    x_y_option_menu.grid(row=2, column=0, padx=10, pady=10)    

    x_y_equals_entry = tk.Entry(controls_frame)
    x_y_equals_entry.grid(row=2, column=1, padx=10, pady=10)
    
    plot_button = tk.Button(controls_frame, text = "Plot", command = lambda
                            : handle_click(min_x_entry, max_x_entry, min_y_entry, max_y_entry, variable, x_y_equals_entry, canvas))
    plot_button.grid(row=2, column=3, padx=10, pady=10)
    
    ######################################################

    canvas_frame = LabelFrame(master_window, text="Graph", padx=5, pady=5)
    canvas_frame.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky=E+W+N+S)

    master_window.columnconfigure(0, weight=1)
    master_window.rowconfigure(3, weight=1)

    canvas_frame.rowconfigure(0, weight=1)
    canvas_frame.columnconfigure(0, weight=1)

    canvas = tk.Canvas(canvas_frame, highlightthickness = 1, highlightbackground = "black")    
    canvas.grid(row=0, column=0, sticky=E+W+N+S)

    ######################################################

    mainloop()

########################################################
# Entry Point
########################################################
    
if __name__ == "__main__":
    main()