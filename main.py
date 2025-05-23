import tkinter as tk

class Currency:

    def __init__(self, root):
        self.variable1 = tk.StringVar(root)
        self.variable1.set("EUR")

        self.variable2 = tk.StringVar(root)
        self.variable2.set("USD")

        self.currencies = {
        "USD": 1.13,   # US-Dollar
        "EUR": 1,      # Euro
        "JPY": 129.53, # Japanischer Yen
        "GBP": 0.85,   # Britisches Pfund
        "AUD": 1.59,   # Australischer Dollar
        "CAD": 1.43,   # Kanadischer Dollar
        "CHF": 1.04,   # Schweizer Franken
        "CNY": 7.19,   # Chinesischer Yuan
        "SEK": 10.21,  # Schwedische Krone
        "NZD": 1.66    # Neuseeländischer Dollar
        }

        self.root = root
        self.root.title("Währungsrechner")
        self.root.minsize(200,100)

        # Entry-Felder
        self.entry = tk.Entry(root)
        self.entry.grid(column=1,row=0,pady=5)

        # Dropdownmenus
        self.dropmenu1 = tk.OptionMenu(root, self.variable1, *self.currencies.keys())
        self.dropmenu1.grid(column=0,row=0,pady=5)
        
        self.dropmenu2 = tk.OptionMenu(root, self.variable2, *self.currencies.keys())
        self.dropmenu2.grid(column=0,row=2,pady=5)

        # Button
        self.button = tk.Button(root, text="Umrechnen", command=self.umrechnung)
        self.button.grid(row=1,pady=5)

        # Label für Ausgabe
        self.output_label = tk.Label(root, text="")
        self.output_label.grid(column=1,row=2,pady=5)



    def umrechnung(self):
        currency1 = self.variable1.get()
        currency2 = self.variable2.get()
        try:
            value1 = float(self.entry.get())
            value2 = (value1/self.currencies[currency1]) * self.currencies[currency2]
            
            self.output_label.config(text=f"{round(value2,2)}")

        except ValueError:
            self.output_label.config(text="Keine Zahl")






if __name__ == "__main__":
    root = tk.Tk()
    gui = Currency(root)
    root.mainloop()


