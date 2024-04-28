import tkinter as tk
from tkinter import messagebox
from tkinter import Button

class AddToCartPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Add to Cart Page")
        self.root.geometry("1100x700")

        # Create a teal rectangle
        self.canvas_teal = tk.Canvas(root, width=1100, height=50, bg='TEAL')
        self.canvas_teal.place(relx=0, rely=0.00, relwidth=1, relheight=0.2, anchor='nw')  # Adjusted position and size

        # Logo
        logo_label = tk.Label(root, text="Netmeds.com", font="times 15 bold", foreground="White", bg='TEAL')
        logo_label.place(x=50, y=50)

        # Project Name Label
        project_label = tk.Label(root, text="Add to Cart", font="times 50 bold", bg='teal', fg='white')
        project_label.place(relx=0.5, rely=0.07, anchor='n')  # Positioned above the teal rectangle

        # Back Button
        back_button = tk.Button(root, text="BACK", foreground="TEAL", background="purple", font="times 15 bold", bg='White', height=1, width=5,command=self.open_back)
        back_button.place(x=1000, y=30)

        # Initialize cart list
        self.cart_items = []

        # Create a frame for the product list
        self.product_frame = tk.Frame(root, height=600)  # Adjusted height
        self.product_frame.pack(side=tk.LEFT, padx=10, pady=10)

        # Add products to the frame
        self.add_product("Product 1", 10)
        self.add_product("Product 2", 20)
        self.add_product("Product 3", 30)

        # Create a frame for the cart
        self.cart_frame = tk.Frame(root)
        self.cart_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        # Create a frame for the bill summary
        self.bill_frame = tk.Frame(root, height=600)  # Adjusted height
        self.bill_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        # Create a button to view cart
        self.proceed_button = tk.Button(root, text="Proceed", command=self.proceed, height=3, width=20)  # Increased height and width
        self.proceed_button.place(relx=0.5, rely=0.90, anchor='s')  # Positioned above the white rectangle

        # Create a white rectangle at the middle
        self.canvas_white_middle = tk.Canvas(root, width=1100, height=50, bg='WHITE')
        self.canvas_white_middle.place(relx=0, rely=0.2, relwidth=1, relheight=0.08, anchor='nw')  # Adjusted position and size

        # Create another white rectangle at the bottom
        self.canvas_white_bottom = tk.Canvas(root, width=1100, height=50, bg='WHITE')
        self.canvas_white_bottom.place(relx=0, rely=1, relwidth=1, relheight=0.08, anchor='sw')  # Positioned at the bottom

        # Create a label for total bill
        self.total_bill_label = tk.Label(self.bill_frame, text="Total Bill: Rs0", font=("Helvetica", 18))
        self.total_bill_label.pack()

        # Initialize variable to keep track of row index
        self.row_index = 0

    def add_product(self, name, price):
        product_label = tk.Label(self.product_frame, text=f"{name} - Rs{price}", font=("Helvetica", 14))
        product_label.pack()

        add_to_cart_button = tk.Button(self.product_frame, text="Add to Cart",
                                       command=lambda: self.add_to_cart(name, price), height=2, width=20)  # Increased height and width
        add_to_cart_button.pack()

    def add_to_cart(self, name, price):
        for item in self.cart_items:
            if item['name'] == name:
                item['quantity'] += 1
                messagebox.showinfo("Added to Cart", f"Another {name} added to cart.")
                self.update_cart()
                return

        self.cart_items.append({"name": name, "price": price, "quantity": 1})
        messagebox.showinfo("Added to Cart", f"{name} added to cart.")
        self.update_cart()

    def update_cart(self):
        # Clear previous items in the cart frame
        for widget in self.cart_frame.winfo_children():
            widget.destroy()

        # Display items in the cart
        for item in self.cart_items:
            cart_label = tk.Label(self.cart_frame,
                                  text=f"{item['name']} - Rs{item['price']} - Quantity: {item['quantity']}", font=("Helvetica", 14))
            cart_label.grid(row=self.row_index, column=0, sticky='w')
            self.row_index += 1

        # Calculate and display total bill
        total_bill = sum(item['price'] * item['quantity'] for item in self.cart_items)
        self.total_bill_label.config(text=f"Total Bill: Rs{total_bill}")
        self.total_bill_label.pack()  # Place the total bill label below the cart items

    def proceed(self):
        # Display message box for order placed successfully
        messagebox.showinfo("Success", "Order placed successfully!")

        # Reset cart items and update display
        self.cart_items = []
        self.update_cart()


    def open_back(self):
        self.root.destroy()
        from Medicine_Home import HomePage
        new_root = tk.Tk()
        app = HomePage(new_root)
        new_root.geometry("1100x600")
        new_root.title('NEW_PAGE')
        new_root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = AddToCartPage(root)
    root.mainloop()