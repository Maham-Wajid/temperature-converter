import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # For adding background images

class TemperatureConverterApp:
    """
    A GUI-based application for converting temperatures between Celsius, Fahrenheit, and Kelvin.

    Attributes:
        root (tk.Tk): The root window for the application.
        history (list): A list to store the conversion history.
        canvas (tk.Canvas): Canvas for displaying UI elements like background image and text.
        conversion_var (tk.StringVar): Variable to hold the selected conversion type from the combobox.
        temperature_var (tk.StringVar): Variable to hold the input temperature value.
        history_listbox (tk.Listbox): Listbox to display the conversion history.
        result_text_id (int): ID of the text object on the canvas used for displaying the conversion result.
    """

    def __init__(self, root):
        """
        Initializes the Temperature Converter application.

        Args:
            root (tk.Tk): The root window for the application.
        """
        self.root = root
        self.root.title("Temperature Converter")
        self.root.geometry("1000x700")
        self.root.resizable(False, False)

        # Conversion history
        self.history = []

        # Adding background image using canvas
        self.canvas = tk.Canvas(self.root, width=1000, height=700)
        self.canvas.place(relwidth=1, relheight=1)

        self.background_image = Image.open("asset/img/background.jpg").resize((1000, 700), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.background_image)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Title label using canvas
        self.canvas.create_text(500, 70, text="Temperature Converter", font=("Arial", 22, "bold"), fill="#F6FCDF")

        # Conversion options using canvas
        self.canvas.create_text(500, 120, text="Select Conversion Type:", font=("Arial", 12), fill="#ffffff")
        
        # Conversion menu (Combobox)
        self.conversion_var = tk.StringVar()
        self.conversion_menu = ttk.Combobox(self.root, textvariable=self.conversion_var, font=("Arial", 12), state="readonly")
        self.conversion_menu["values"] = [
            "Celsius to Fahrenheit",
            "Fahrenheit to Celsius",
            "Celsius to Kelvin",
            "Kelvin to Celsius",
            "Fahrenheit to Kelvin",
            "Kelvin to Fahrenheit"
        ]
        self.conversion_menu.place(x=500, y=150, anchor="n")
        self.conversion_menu.current(0)

        # Temperature input using canvas
        self.canvas.create_text(500, 200, text="Enter Temperature:", font=("Arial", 12), fill="#ffffff")

        self.temperature_var = tk.StringVar()
        self.input_entry = tk.Entry(self.root, textvariable=self.temperature_var, font=("Arial", 12), width=20)
        self.input_entry.place(x=500, y=220, anchor="n")

        # Convert button
        convert_button = tk.Button(self.root, text="Convert", font=("Arial", 12, "bold"), bg="#7ED4AD", fg="#000000", command=self.convert_temperature)
        convert_button.place(x=500, y=270, anchor="n")

        # Result display using canvas (Initial placeholder)
        self.result_text_id = self.canvas.create_text(500, 350, text="Result will appear here!", font=("Arial", 12, "bold"), fill="#ffffff")

        # History label using canvas
        self.canvas.create_text(500, 400, text="Conversion History:", font=("Arial", 22, "bold"), fill="#F6FCDF")

        # History frame and listbox
        history_frame = tk.Frame(self.root, bg="#C2FFC7", padx=5, pady=5)
        history_frame.place(x=500, y=450, width=350, height=150, anchor="n")

        self.history_listbox = tk.Listbox(history_frame, font=("Arial", 10), height=5, justify="center")
        self.history_listbox.pack(side="left", fill="both", expand=True)

        history_scrollbar = tk.Scrollbar(history_frame, orient="vertical", command=self.history_listbox.yview)
        history_scrollbar.pack(side="right", fill="y")
        self.history_listbox.config(yscrollcommand=history_scrollbar.set)

        # Clear history button
        clear_button = tk.Button(self.root, text="Clear History", font=("Arial", 12, "bold"), bg="#FF5733", fg="#000000", command=self.clear_history)
        clear_button.place(x=500, y=620, anchor="n")

    def convert_temperature(self):
        """
        Converts the input temperature based on the selected conversion type and updates the result and history.

        Handles invalid inputs and ensures Kelvin temperatures are non-negative.
        """
        try:
            temp = float(self.temperature_var.get())
            conversion_type = self.conversion_var.get()

            # Validate Kelvin values
            if "Kelvin" in conversion_type and temp < 0:
                messagebox.showerror("Invalid Input", "Temperatures in Kelvin cannot be negative.")
                return

            if conversion_type == "Celsius to Fahrenheit":
                result = (temp * 9 / 5) + 32
                result_text = f"{temp}°C = {result:.2f}°F"
            elif conversion_type == "Fahrenheit to Celsius":
                result = (temp - 32) * 5 / 9
                result_text = f"{temp}°F = {result:.2f}°C"
            elif conversion_type == "Celsius to Kelvin":
                result = temp + 273.15
                result_text = f"{temp}°C = {result:.2f}K"
            elif conversion_type == "Kelvin to Celsius":
                result = temp - 273.15
                result_text = f"{temp}K = {result:.2f}°C"
            elif conversion_type == "Fahrenheit to Kelvin":
                result = ((temp - 32) * 5 / 9) + 273.15
                result_text = f"{temp}°F = {result:.2f}K"
            elif conversion_type == "Kelvin to Fahrenheit":
                result = ((temp - 273.15) * 9 / 5) + 32
                result_text = f"{temp}K = {result:.2f}°F"

            # Update the result text on the canvas
            self.canvas.itemconfig(self.result_text_id, text=result_text)

            self.history.append(result_text)
            self.history_listbox.insert(tk.END, result_text)
            self.history_listbox.insert(tk.END, "----------------------------------") 

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid numeric temperature.")

    def clear_history(self):
        """
        Clears the conversion history and updates the UI.
        """
        self.history.clear()
        self.history_listbox.delete(0, tk.END)
        self.temperature_var.set("")
        self.canvas.itemconfig(self.result_text_id, text="Result will appear here!")
        messagebox.showinfo("History Cleared", "Conversion history has been cleared!")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureConverterApp(root)
    root.mainloop()
