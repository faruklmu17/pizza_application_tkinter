import tkinter as tk
from tkinter import messagebox

#sign up window 
root = tk.Tk()
root.title("Sign up Window")

signup_label = tk.Label(root,text="Hello,click the button to sign up to order your pizza!\n")
signup_label.grid(row=0,column=0,sticky="we")
account_label = tk.Label(root,text="Click the button to Go to Account")
account_label.grid(row=0,column=0,sticky="we")
account_label.grid_remove()

account_button = tk.Button(root,text="ORDER PIZZA!",bg="Orange")
account_button.grid(row=1,column=0,sticky="we")
account_button.grid_remove()

social_button = tk.Button(root, text="PIZZA TONIGHT",bg="orange")
social_button.grid(row=1,column=0,sticky="we")


# this function is for signup 
def signup():
    first_name_label = tk.Label(root, text="Type Your First Name-")
    first_name_label.grid(row=2,column=0,sticky="we")
    first_name_entry = tk.Entry(root)
    first_name_entry.grid(row=3,column=0,sticky="we")

    last_name_label = tk.Label(root, text="Type Your Last Name-")
    last_name_label.grid(row=4,column=0,sticky="we")
    last_name_entry = tk.Entry(root)
    last_name_entry.grid(row=5,column=0,sticky="we")

    email_label = tk.Label(root, text="Type Your email-")
    email_label.grid(row=6,column=0,sticky="we")
    email_entry = tk.Entry(root)
    email_entry.grid(row=7,column=0,sticky="we")
    continue_button = tk.Button(root, text="Continue",bg="orange")
    continue_button.grid(row=8,column=0,sticky="we")
    # error_label= tk.Label(root,text="")
    # error_label.grid()



    # create another window here 

    def password_setup():
      root.withdraw()
      root2 = tk.Toplevel(root)
      root2.title("Password Setup")
      def validate_password(*args):
        password = password_entry.get()


        # Check the length of the password
        if len(password) >= 8:
            requirements_details.config(fg="green")
            if any(char.isupper() for char in password):
              requirements_details1.config(fg="green")
              continue1_button.grid()
            else:
              requirements_details1.config(fg="red")
              continue1_button.grid_remove()
        else:
            requirements_details.config(fg="red")
            continue1_button.grid_remove()
        # allowing the continue button to check the match



      password_label = tk.Label(root2, text="Type a password:")
      password_label.grid(row=0, column=0, sticky="e")

      password_entry = tk.Entry(root2, show="*")
      password_entry.grid(row=0, column=1)
      password_entry.bind("<KeyRelease>", validate_password)  # Bind the function to the KeyRelease event

      confirmed_password_label = tk.Label(root2, text="Confirm your password:")
      confirmed_password_label.grid(row=1, column=0, sticky="e")

      confirmed_password_entry = tk.Entry(root2, show="*")
      confirmed_password_entry.grid(row=1, column=1)

      continue1_button = tk.Button(root2, text="Continue")
      continue1_button.grid(row=2, column=1,sticky="ew")

      empty_label = tk.Label(root2, text="")
      empty_label.grid(row=3, column=0)
      # adding the dialog box here 

      def show_confirmation():

        result = messagebox.askyesno("Confirmation", "Do you want to proceed?")
        if result:

          if password_entry.get() == confirmed_password_entry.get():
             messagebox.showinfo("Information", "Password Match!")
             root2.withdraw()
             root.deiconify()
             signup_label.grid_remove()
             social_button.grid_remove()
             first_name_entry.grid_remove()
             first_name_label.grid_remove()
             last_name_entry.grid_remove()
             last_name_label.grid_remove()
             email_label.grid_remove()
             email_entry.grid_remove()
             account_button.grid()
             continue_button.grid_remove()
             account_label.grid()

            
             def pizza_ordering():
               
               def show_order_details():
                 # Display the selected size
                 size = size_var.get()
                 size_label.config(text=f"Size: {size.capitalize()}")

                 # Display the selected toppings
                 toppings = [topping for topping, var in [("Mushroom", mushroom_var), ("Olive", olive_var), ("Bell Pepper", bell_pepper_var)] if var.get()]
                 toppings_label.config(text=f"Toppings: {', '.join(toppings)}")

                 # Calculate the total price based on the selected size and toppings
                 total_price = calculate_total_price(size, toppings)
                 total_price_label.config(text=f"Total Price (without tax): ${total_price:.2f}")

               def confirm_order():
                 global total_price
                 global tip
                 # Get tip amount
                 tip = float(tip_entry.get()) if tip_entry.get() else 0.0

                 # Get total price without tip
                 total_price_str = total_price_label.cget("text").split(": ")[1].replace('$', '')
                 total_price = float(total_price_str)


                 #this window will be called when the confirm button is clicked
                 def receipt_window():
                   pizza_window.withdraw()
                   root1 = tk.Toplevel(pizza_window)
                   root1.configure(bg="white")

                   root1.title("Receipt Window")
                   receipt = tk.Label(root1,text="PIZZA EXPRESS\nOrder Confirmation",bg="white",font=("Helvetica", 10, "bold"))
                   receipt.grid(row=0,column=0,columnspan=3,sticky="ew")
                   line = tk.Label(root1,text="=========================\n",bg="white")
                   line.grid(row=1,column=0,columnspan=3,sticky="ew")

                   total_price_with_tip_label = tk.Label(root1, text="Total Price (with tip, without tax): $0.00", fg="black",bd=2,relief="solid",font=("Helvetica", 10, "bold"))
                   tax_label = tk.Label(root1, text="Tax: $0.00",relief="solid", font=("Helvetica", 10, "bold"))
                   total_price_with_tax_label = tk.Label(root1, text="Total Price (with tip and tax): $0.00\n\n", fg="black",bd=2,relief="solid",font=("Helvetica", 10, "bold"))

                   # Add tip to the total price
                   total_with_tip = total_price + tip
                   total_price_with_tip_label.config(text=f"Total Price (with tip, without tax): ${total_with_tip:.2f}")
                   # Calculate and display tax
                   tax = calculate_tax(total_with_tip)
                   tax_label.config(text=f"Tax: ${tax:.2f}")

                   # Calculate total price with tax
                   total_with_tax = total_with_tip + tax
                   total_price_with_tax_label.config(text=f"Total Price (with tip and tax): ${total_with_tax:.2f}")
                   account_info1 = tk.Label(root1,text="Your full name: "+first_name_entry.get()+" "+last_name_entry.get(),bg="white",fg="green")
                   account_info1.grid(sticky="w",padx=10)
                   account_info2 = tk.Label(root1,text="Your email address: "+email_entry.get()+"\n",bg="white")
                   account_info2.grid(sticky="w",padx=10)
                   
                   
                    




                   total_price_with_tip_label.grid(row=4, column=0, columnspan=3, sticky="w", padx=10)
                   tax_label.grid(row=5, column=0, columnspan=3, sticky="w", padx=10)
                   total_price_with_tax_label.grid(row=6, column=0, columnspan=3, sticky="w", padx=10)
                   empty_label = tk.Label(root1,text="\n",bg="white")
                   empty_label.grid()




                 receipt_window()






               def calculate_total_price(size, toppings):
                 # Define prices
                 size_prices = {"small": 10.00, "medium": 15.00, "large": 20.00}
                 toppings_price = len(toppings) * 2.50  # $2.50 per topping

                 # Calculate total price
                 total_price = size_prices.get(size, 0) + toppings_price
                 return total_price

               def calculate_tax(total_price):
                 # Assuming 5% tax rate
                 tax_rate = 0.05
                 return total_price * tax_rate

               root.withdraw()
               pizza_window = tk.Toplevel(root)
               
               pizza_window.title("Pizza Order")

               # Pizza Size Selection
               pizza_size_text = tk.Label(pizza_window, text="Choose a size of your choice...", font=("Helvetica", 10, "bold"))
               size_var = tk.StringVar()
               size_var.set("")  # Set initially to an empty string
               small_radio = tk.Radiobutton(pizza_window, text="Small", variable=size_var, value="small", command=show_order_details)
               medium_radio = tk.Radiobutton(pizza_window, text="Medium", variable=size_var, value="medium", command=show_order_details)
               large_radio = tk.Radiobutton(pizza_window, text="Large", variable=size_var, value="large", command=show_order_details)

               # Toppings Selection
               toppings_text = tk.Label(pizza_window, text="Choose toppings...", font=("Helvetica", 10, "bold"))
               mushroom_var = tk.StringVar()
               olive_var = tk.StringVar()
               bell_pepper_var = tk.StringVar()

               mushroom_check = tk.Checkbutton(pizza_window, text="Mushroom", variable=mushroom_var, onvalue="Mushroom", offvalue="", command=show_order_details)
               olive_check = tk.Checkbutton(pizza_window, text="Olive", variable=olive_var, onvalue="Olive", offvalue="", command=show_order_details)
               bell_pepper_check = tk.Checkbutton(pizza_window, text="Bell Pepper", variable=bell_pepper_var, onvalue="Bell Pepper", offvalue="", command=show_order_details)

               # Labels to display order details
               order_label = tk.Label(pizza_window, text="Your Order Details:", font=("Helvetica", 10, "bold"))
               size_label = tk.Label(pizza_window, text="Size: ")
               toppings_label = tk.Label(pizza_window, text="Toppings: ")
               total_price_label = tk.Label(pizza_window, text="Total Price (without tax): $0.00", fg="green", font="bold",bd=2,relief="solid")

               # Place widgets using grid layout
               pizza_size_text.grid(row=0, sticky="w", column=0)
               small_radio.grid(row=1, column=0, padx=10, sticky="w")
               medium_radio.grid(row=2, column=0, padx=10, sticky="w")
               large_radio.grid(row=3, column=0, padx=10, sticky="w")

               toppings_text.grid(row=4, sticky="w")
               mushroom_check.grid(row=5, column=0, padx=10, sticky="w")
               olive_check.grid(row=6, column=0, padx=10, sticky="w")
               bell_pepper_check.grid(row=7, column=0, padx=10, sticky="w")

               order_label.grid(row=8, column=0, columnspan=3, sticky="w")
               size_label.grid(row=9, column=0, columnspan=3, sticky="w", padx=10)
               toppings_label.grid(row=10, column=0, columnspan=3, sticky="w", padx=10)
               total_price_label.grid(row=11, column=0, columnspan=3, sticky="w", padx=10)

               # Tip Entry
               tip_label = tk.Label(pizza_window, text="Tip: $", font=("Helvetica", 10, "bold"))
               tip_entry = tk.Entry(pizza_window)
               tip_label.grid(row=12, column=0, columnspan=3, sticky="w", padx=10)
               tip_entry.grid(row=12, column=0, columnspan=3, sticky="e", padx=10)

               # Confirm Button
               confirm_button = tk.Button(pizza_window, text="Confirm Tip", command=confirm_order,bg="orange")
               confirm_button.grid(row=13, column=0, columnspan=3, sticky="w", padx=10)





               
               
             #def account():
              #account_page = tk.Toplevel(root)
              #root.withdraw()
              #account_page.title("Account Page")
              # account_page_label = tk.Label(account_page,text="Welcome to your account!\nHere are your details:")
              # personal_info = tk.Label(account_page,text="Your full name: "+first_name_entry.get()+" "+last_name_entry.get()+"\nYour email address: "+email_entry.get())

              # account_page_label.grid(sticky="ew")
              # personal_info.grid(sticky="ew")
              #pizza_ordering()
             account_button.config(command=pizza_ordering)

          else:
            messagebox.showerror("Information", "Sorry,passwords did not match! Please try again.")

      continue1_button.config(command=show_confirmation)

      # Add a label for password requirements in the new column
      requirements_label = tk.Label(root2, text="Password Requirements:",bd=2,relief="raised")
      requirements_label.grid(row=0, column=2, sticky="w", padx=(10, 0),pady=10)

      requirements_details = tk.Label(root2, text="- At least 8 characters",bd=2,relief="solid")
      requirements_details.grid(row=1, column=2, sticky="ew", padx=(10, 0))
      requirements_details1 = tk.Label(root2, text="- At least 1 uppercase",bd=2,relief="solid")
      requirements_details1.grid(row=2, column=2, sticky="ew", padx=(10, 0))




    # if len(first_name_entry.get())>=1 and len(last_name_entry.get())>=1 and "@" in email_entry.get():


    continue_button.config(command=password_setup)

    # else:
    #     def error_msg():

    #       error_label.config(text="Please fill up the informaiton!",bg="red")
    #     continue_button.config(command=error_msg)



social_button.config(command=signup)






root.mainloop()


