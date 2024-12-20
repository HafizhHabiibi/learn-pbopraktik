import tkinter as tk # Jadul
from tkinter import ttk, messagebox #Baru

class AppOrder:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Pemesanan Makanan")
        self.root.geometry("1000x700")
        self.root.configure(bg="pink")

        self.widget_create()

    def widget_create(self):
        # Title label
        title_label = tk.Label(text="Aplikasi Pemesanan Makanan", font=("Times New Roman", 20, "bold"), bg="pink", fg="white")
        title_label.pack(pady=10)

        # Nama Pemesan
        name_label = tk.Label(text="Nama Pemesan : ", bg="pink")
        name_label.pack()
        self.name_entry = tk.Entry(self.root, width=35)
        self.name_entry.pack(pady=5)

        # Pilihan Makanan
        self.food_list = {"Nasi Goreng":10000, "Bakso":12000, "Mie Ayam":15000, "Soto":10000}
        food_label = tk.Label(text="Pilih Makanan : ", bg="pink")
        food_label.pack()
        food_list = list(self.food_list.keys())

        self.food_var = tk.StringVar(value="")
        self.food_menu = ttk.Combobox(self.root, values=food_list, width=25, textvariable=self.food_var, state="readonly")
        self.food_menu.pack(pady=5)
        qty_label = tk.Label(text="Jumlah Pesanan : ", bg="pink")
        qty_label.pack()
        self.qty_entry = tk.Entry(self.root, width=25)
        self.qty_entry.pack(pady=5)

        # tombol tambah pesanan
        add_button = tk.Button(self.root, text="Tambah Pesanan", command=self.add_data)
        add_button.pack(pady=10)

        # Daftar Pesanan
        order_label = tk.Label(text="Daftar Pesanan : ", bg="pink")
        order_label.pack()
        self.order_table = ttk.Treeview(self.root, columns=("Nama", "Makanan", "Jumlah", "Harga"), show="headings")
        self.order_table.heading("Nama", text="Nama")
        self.order_table.heading("Makanan", text="Makanan")
        self.order_table.heading("Jumlah", text="Jumlah")
        self.order_table.heading("Harga", text="Harga")

        self.order_table.column("Nama", width=200, anchor="center")
        self.order_table.column("Makanan", width=200, anchor="center")
        self.order_table.column("Jumlah", width=200, anchor="center")
        self.order_table.column("Harga", width=200, anchor="center")
        self.order_table.pack(pady=10)

        # Clear Table
        clear_button = tk.Button(self.root, text="Reset", width=20, command=self.clear_data)
        clear_button.pack(pady=10)
    
# Fungsi tambah data
    def add_data(self):
        name = self.name_entry.get()
        food = self.food_var.get()
        qty = self.qty_entry.get()
        
        if name and qty.isdigit():
            price = self.food_list[food] * int(qty)
            self.order_table.insert("", "end", values=(name, food, qty, f"Rp.{price:,}"))
        else:
            messagebox.showerror("Error", "Pastikan Inputan Tidak Kosong !")

# Fungsi mereset data
    def clear_data(self):
        confirm = messagebox.askquestion("", "Apakah Anda Yakin Mereset Tabel ?")
        if confirm == "YES".lower():
            for item in self.order_table.get_children():
                self.order_table.delete(item)

if __name__ == "__main__":
    root = tk.Tk()
    app = AppOrder(root)
    root.mainloop()
