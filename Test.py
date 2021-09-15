import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates
from tkinter import messagebox

c = CurrencyRates()
convert_result = 0

def leftClickButton(event):
    if entry_amountInput.get() == '':
        messagebox.showerror("Error", "Please Input amount before convert!!!")
    convert_result = float(entry_amountInput.get()) * c.get_rate(combobox_currentInput.get(),combobox_currentOutput.get())
    label_valueOutput.configure(text= convert_result)

def leftClickButton_Clear(self):
    entry_amountInput.delete(0,'end')
    label_valueOutput.configure(text = 0)
    combobox_currentInput.set('')
    combobox_currentOutput.set('')

# Create GUI
mainpage = tk.Tk()
mainpage.geometry('400x200')
mainpage.title("Foreign Currency Converter")




#Label
label_currentInput = tk.Label(mainpage,text="Currency Input")
label_currentInput.grid(column=0, row=0,padx = 20)

label_currentTarget = tk.Label(mainpage,text="Currency Target")
label_currentTarget.grid(column=1, row=0)

label_amountInput = tk.Label(mainpage,text="Amount Input")
label_amountInput.grid(column=0, row=2)

label_amountOutput = tk.Label(mainpage, text ="Amount output")
label_amountOutput.grid(column = 1, row = 2,  )

label_valueOutput = tk.Label(mainpage, text ="0")
label_valueOutput.grid(column = 1, row = 3,  )


#Combobox currency

combobox_currentInput = ttk.Combobox(mainpage,
                                     values=[
                                         "USD",
                                         "JPY",
                                         "EUR",
                                         "THB",
                                         "IDR",
                                         "BGN",
                                         "ILS",
                                         "GBP",
                                         "AUD",
                                         "CHF",
                                         "HKD"])


combobox_currentInput.grid(column=0, row=1, columnspan = 1,padx = 10)

combobox_currentOutput = ttk.Combobox(mainpage,
                            values=[
                                "USD",
                                "JPY",
                                "EUR",
                                "THB",
                                "IDR",
                                "BGN",
                                "ILS",
                                "GBP",
                                "AUD",
                                "CHF",
                                "HKD"])

combobox_currentOutput.grid(column=1, row=1, columnspan = 1)

#Entry1

entry_amountInput = tk.Entry(mainpage, width = 23)
entry_amountInput.grid(column = 0, row = 3,columnspan = 1,pady = 5)

#Button convert
button_convert = tk.Button(mainpage, text = "Convert", width=20, bg = '#E5C1CD')
button_convert.bind('<Button-1>', leftClickButton)
button_convert.grid(row=4,column=0,pady = 5)

#Button Clear
button_clear = tk.Button(mainpage, text = "Clear", width=20, bg = '#F3DBCF')
button_clear.bind('<Button-1>', leftClickButton_Clear)
button_clear.grid(row=4,column=1,pady = 5)

mainpage.configure(bg = '#E0ECDE')
mainpage.mainloop()