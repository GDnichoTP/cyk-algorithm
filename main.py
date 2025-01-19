import tkinter as tk
from grammar import rules

# fungsi untuk membuat CNF
def parse_grammar(grammar_string):
    grammar_dict = {}
    for line in grammar_string.split('\n'):
        if not line.strip():
            continue
        head, productions = line.split(' -> ')
        productions = productions.split(' | ')
        grammar_dict[head.strip()] = [production.split() for production in productions]
    return grammar_dict

R = parse_grammar(rules)

# fungsi untuk menjalankan algoritma CYK
def cyk_parse(w):
    n = len(w)

    # membuat tabel
    T = [[set() for j in range(n)] for i in range(n)]

    # mengisi sel diagonal utama
    for j in range(n):
        # cek aturan produksi
        for lhs, rule in R.items():
            for rhs in rule:
                if len(rhs) == 1 and rhs[0] == w[j]:
                    T[j][j].add(lhs)

        # menerapkan unary rules
        T[j][j] = apply_unary_rules(T[j][j], R)

    # mengisi sel di atas diagonal utama
    for span in range(2, n + 1): # substring panjang 2 sampai n
        for i in range(n - span + 1): # index substring pertama
            j = i + span - 1 # index substring akhir
            for k in range(i, j): # mencoba semua titik pemisah antara i dan j
                for lhs, rule in R.items(): 
                    for rhs in rule:
                        if len(rhs) == 2 and rhs[0] in T[i][k] and rhs[1] in T[k + 1][j]:
                            T[i][j].add(lhs)

            # menerapkan unary rules
            T[i][j] = apply_unary_rules(T[i][j], R)
    
    return T

# fungsi untuk menerapkan unary rules
def apply_unary_rules(cell, rules):

    # himpunan yang berisi non-terminal pada sel
    to_process = set(cell)
    processed = set()

    # pengulangan sampai semua non-terminal diproses
    while to_process:
        current = to_process.pop()
        processed.add(current)

        # cek unary rules untuk menambahkan non-terminal ke sel
        for lhs, rhs in rules.items():
            for production in rhs:
                if len(production) == 1 and production[0] == current:
                    if lhs not in processed:  # menghindari duplikat
                        cell.add(lhs)
                        to_process.add(lhs)

    return cell

# fungsi menampilkan GUI
def displayCYKTable():

    # input string
    w = input_entry.get().strip().split()
    
    if not w:  # jika kosong, error
        result_label.config(text="Please enter a valid input string.")
        return

    # mengambil hasil algoritma CYK
    table = cyk_parse(w)

    # mengosongkan tabel
    for widget in table_frame.winfo_children():
        widget.destroy()

    # menampilkan input string
    for col, word in enumerate(w):
        header = tk.Label(table_frame, text=word, borderwidth=0, relief="solid", padx=5, pady=5, width=15)
        header.grid(row=0, column=col + 1, sticky="nsew")
        table_frame.grid_columnconfigure(col + 1, weight=1)

    for row, word in enumerate(w):
        header = tk.Label(table_frame, text=word, borderwidth=0, relief="solid", padx=5, pady=5, width=15)
        header.grid(row=row + 1, column=0, sticky="nsew")
        table_frame.grid_rowconfigure(row + 1, weight=1)

    # menampilkan tabel
    n = len(w)
    for i in range(n):
        for j in range(n):
            value = ", ".join(list(table[i][j])) if j >= i else ""
            cell = tk.Label(table_frame, text=value, borderwidth=1, relief="solid", padx=5, pady=5, width=15)
            cell.grid(row=i + 1, column=j + 1, sticky="nsew")

    # validasi hasil akhir
    result_label.config(
        text="Nominal Phrase: valid" 
        if "K" in table[0][n - 1] else 
        "Nominal Phrase: NOT-valid"
    )

    # mengosongkan input field
    input_entry.delete(0, tk.END)

# main GUI
root = tk.Tk()
root.title("CYK Parsing Table")

# frame input
input_frame = tk.Frame(root)
input_frame.pack(padx=10, pady=10)

tk.Label(input_frame, text="Input string:").pack(side="left", padx=5)
input_entry = tk.Entry(input_frame, width=30)
input_entry.pack(side="left", padx=5)
parse_button = tk.Button(input_frame, text="Parse", command=displayCYKTable)
parse_button.pack(side="left", padx=5)

# frame tabel
table_frame = tk.Frame(root)
table_frame.pack(padx=10, pady=10, fill="both", expand=True)

# teks hasil
result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
result_label.pack(padx=10, pady=10)

# menjalankan GUI
root.mainloop()