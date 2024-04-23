import tkinter as tk
from tkinter import messagebox, simpledialog

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contacts = []

        self.root.configure(bg="#b2ebf2")  

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Name:", bg="#b2ebf2", font=("Arial", 12, "bold"), fg="black").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        tk.Label(self.root, text="Phone:", bg="#b2ebf2", font=("Arial", 12, "bold"), fg="black").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        tk.Label(self.root, text="Email:", bg="#b2ebf2", font=("Arial", 12, "bold"), fg="black").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        tk.Label(self.root, text="Address:", bg="#b2ebf2", font=("Arial", 12, "bold"), fg="black").grid(row=3, column=0, padx=5, pady=5, sticky="e")

        entry_width = 40
        self.name_entry = tk.Entry(self.root, width=entry_width)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.phone_entry = tk.Entry(self.root, width=entry_width)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.phone_entry.config(validate="key", validatecommand=(self.root.register(self.validate_phone), "%P"))
        self.email_entry = tk.Entry(self.root, width=entry_width)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        self.address_entry = tk.Entry(self.root, width=entry_width)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        button_font = ("Arial", 10)
        button_width = 12
        tk.Button(self.root, text="Add", font=button_font, width=button_width, command=self.add_contact).grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="we")
        tk.Button(self.root, text="View", font=button_font, width=button_width, command=self.view_contacts).grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="we")
        tk.Button(self.root, text="Search", font=button_font, width=button_width, command=self.search_contact).grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="we")
        tk.Button(self.root, text="Update", font=button_font, width=button_width, command=self.update_contact).grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="we")
        tk.Button(self.root, text="Delete", font=button_font, width=button_width, command=self.delete_contact).grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky="we")

    def validate_phone(self, value):
        if all(char.isdigit() or char == "+" for char in value) or value == "":
            return True
        else:
            return False

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if not name or not phone:
            messagebox.showinfo("Error", "Name and Phone Number are mandatory fields.")
            return

        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        messagebox.showinfo("Success", "Contact added successfully.")
        self.clear_entries()

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "Contact list is empty.")
        else:
            contacts_info = ""
            for i, contact in enumerate(self.contacts, start=1):
                contacts_info += f"--------------\n{i}. Name: {contact.name}\n   Phone: {contact.phone}\n   Email: {contact.email}\n   Address: {contact.address}\n\n"
            messagebox.showinfo("Contacts", contacts_info)

    def search_contact(self):
        search_term = simpledialog.askstring("Search", "Enter a letter of the name or any letter inside the name to search:")
        if search_term:
            found_contacts = [contact for contact in self.contacts if search_term.lower() in contact.name.lower()]
            if not found_contacts:
                messagebox.showinfo("Info", "No matching contacts found.")
            else:
                contacts_info = ""
                for i, contact in enumerate(found_contacts, start=1):
                    contacts_info += f"--------------\n{i}. Name: {contact.name}\n   Phone: {contact.phone}\n   Email: {contact.email}\n   Address: {contact.address}\n\n"
                messagebox.showinfo("Matching Contacts", contacts_info)

    def update_contact(self):
        search_term = simpledialog.askstring("Update Contact", "Enter a letter of the name or any letter inside the name of the contact to update:")
        if search_term:
            found_contacts = [contact for contact in self.contacts if search_term.lower() in contact.name.lower()]
            if not found_contacts:
                messagebox.showinfo("Info", "Contact not found.")
                return
            elif len(found_contacts) > 1:
                selection_window = tk.Toplevel(self.root)
                selection_window.title("Select Contact to Update")

                def update_selected_contact():
                    selected_index = listbox.curselection()
                    if selected_index:
                        contact_to_update = found_contacts[selected_index[0]]
                        self.update_contact_details(contact_to_update)
                        selection_window.destroy()
                    else:
                        messagebox.showinfo("Info", "Please select a contact to update.")

                listbox = tk.Listbox(selection_window, selectmode=tk.SINGLE, font=("Arial", 12))
                listbox.pack(fill=tk.BOTH, expand=True)

                for contact in found_contacts:
                    listbox.insert(tk.END,f"{contact.name}, {contact.phone}, {contact.email}, {contact.address}")

                update_button = tk.Button(selection_window, text="Update Selected", font=("Arial", 10), command=update_selected_contact)
                update_button.pack(pady=5)
            else:
                self.update_contact_details(found_contacts[0])

    def update_contact_details(self, contact):
        fields_to_update = simpledialog.askstring("Update Contact","Enter the fields you want to update (separated by commas, Example:, name, email, phone, address):")
        fields_to_update = [field.strip().lower() for field in fields_to_update.split(',')]
        updated_info = []
        for field in fields_to_update:
            if field == "name":
                new_name = simpledialog.askstring("Update Contact", "Enter new name:", initialvalue=contact.name)
                if new_name:
                    contact.name = new_name
                    updated_info.append(f"Name: {new_name}")
            elif field == "email":
                new_email = simpledialog.askstring("Update Contact", "Enter new email:", initialvalue=contact.email)
                if new_email:
                    contact.email = new_email
                    updated_info.append(f"Email: {new_email}")
            elif field == "phone":
                new_phone = simpledialog.askstring("Update Contact", "Enter new phone:",initialvalue=contact.phone)
                if new_phone:
                    contact.phone = new_phone
                    updated_info.append(f"Phone: {new_phone}")
            elif field == "address":
                new_address = simpledialog.askstring("Update Contact", "Enter new address:",initialvalue=contact.address)
                if new_address:
                    contact.address = new_address
                    updated_info.append(f"Address: {new_address}")
            else:
                messagebox.showinfo("Info", f"Invalid field '{field}' will be skipped.")
        if updated_info:
            messagebox.showinfo("Success", "Contact updated successfully.\nUpdated info:\n" + '\n'.join(updated_info))

    def delete_contact(self):
        search_term = simpledialog.askstring("Delete Contact", "Enter a letter of the name or any letter inside the name of the contact to delete:")
        if search_term:
            found_contacts = [contact for contact in self.contacts if search_term.lower() in contact.name.lower()]
            if not found_contacts:
                messagebox.showinfo("Info", "Contact not found.")
            else:
                if len(found_contacts) == 1:
                    contact_to_delete = found_contacts[0]
                    self.contacts.remove(contact_to_delete)
                    messagebox.showinfo("Success", "Contact deleted successfully.")
                else:
                    selection_window = tk.Toplevel(self.root)
                    selection_window.title("Select Contact to Delete")

                    def delete_selected_contact():
                        selected_index = listbox.curselection()
                        if selected_index:
                            contact_to_delete = found_contacts[selected_index[0]]
                            self.contacts.remove(contact_to_delete)
                            messagebox.showinfo("Success", "Contact deleted successfully.")
                            selection_window.destroy()
                        else:
                            messagebox.showinfo("Info", "Please select a contact to delete.")

                    listbox = tk.Listbox(selection_window, selectmode=tk.SINGLE, font=("Arial", 12))
                    listbox.pack(fill=tk.BOTH, expand=True)

                    for contact in found_contacts:
                        listbox.insert(tk.END,f"{contact.name}, {contact.phone}, {contact.email}, {contact.address}")

                    delete_button = tk.Button(selection_window, text="Delete Selected", font=("Arial", 10), command=delete_selected_contact)
                    delete_button.pack(pady=5)


def main():
    root = tk.Tk()
    root.geometry("500x400")
    app = ContactBookApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
