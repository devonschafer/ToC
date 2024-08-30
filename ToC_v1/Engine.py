from tkinter import *
import time
import random


class UI:
    def __init__(self, master):
        
        self.input_supply = 0
        self.a_supply = 0
        self.b_supply = 0
        self.c_supply = 0
        self.output_supply = 0
        self.cycle = 0
        self.goal = 50
        self.running = 0
        self.time = 2000
        self.money = 10
        self.supply_cost = 1
        self.machine_cost = 0
        self.product_cost = 6
        self.font = ('Helvetica 20 bold')
        self.fontsmall = ('Helvetica 10')
        self.orange = '#ff7b00'
        self.blue = '#0084ff'
        self.black = '#000000'
        
        self.frame_0 = Frame(master, bg=self.blue)
        self.frame_0.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

        self.frame_1 = Frame(master, bg=self.blue)
        self.frame_1.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

        self.frame_2 = Frame(master, bg=self.blue)
        self.frame_2.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

        self.frame_3 = Frame(master, bg=self.blue)
        self.frame_3.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

        self.frame_4 = Frame(master, bg=self.blue)
        self.frame_4.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

        self.frame_5 = Frame(master, bg=self.blue)
        self.frame_5.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

        self.input = Label(self.frame_0, text='supply', bg=self.blue, fg='white', font=self.font)
        self.input.pack(side=TOP, padx=10, pady=10, expand=True)

        self.entry_0 = Entry(self.frame_0, width=5, relief=FLAT, justify='center')
        self.entry_0.insert(0, '0')
        self.entry_0.pack(side=TOP, padx=20, expand=True)

        self.entry_label_0 = Label(self.frame_0, text='items\nper\nday', bg=self.blue, font=self.fontsmall)
        self.entry_label_0.pack(side=TOP, expand=True)

        self.step_a = Label(self.frame_1, text='Step A', bg=self.blue, fg=self.black, font=self.font)
        self.step_a.pack(side=TOP, padx=10, pady=10, expand=True)

        self.entry_1 = Entry(self.frame_1, width=5, relief=FLAT, justify='center')
        self.entry_1.insert(0, '0')
        self.entry_1.pack(side=TOP, padx=20, expand=True)

        self.entry_label_1 = Label(self.frame_1, text='items\nper\nday', bg=self.blue, font=self.fontsmall)
        self.entry_label_1.pack(side=TOP, expand=True)

        self.step_b = Label(self.frame_2, text='Step B', bg=self.blue, fg=self.black, font=self.font)
        self.step_b.pack(side=TOP, padx=10, pady=10, expand=True)

        self.entry_2 = Entry(self.frame_2, width=5, relief=FLAT, justify='center')
        self.entry_2.insert(0, '0')
        self.entry_2.pack(side=TOP, padx=20, expand=True)

        self.entry_label_2 = Label(self.frame_2, text='items\nper\nday', bg=self.blue, font=self.fontsmall)
        self.entry_label_2.pack(side=TOP, expand=True)

        self.step_c = Label(self.frame_3, text='Step C', bg=self.blue, fg=self.black, font=self.font)
        self.step_c.pack(side=TOP, padx=10, pady=10, expand=True)

        self.entry_3 = Entry(self.frame_3, width=5, relief=FLAT, justify='center')
        self.entry_3.insert(0, '0')
        self.entry_3.pack(side=TOP, padx=20, expand=True)

        self.entry_label_3 = Label(self.frame_3, text='items\nper\nday', bg=self.blue, font=self.fontsmall)
        self.entry_label_3.pack(side=TOP, expand=True)

        self.output = Label(self.frame_4, text='products', bg=self.blue, fg='white', font=self.font)
        self.output.pack(side=TOP, padx=10, pady=10, expand=True)

        self.goal_text = Label(self.frame_5, text='Goal %s Products\nin 10 Days' % self.goal, bg=self.blue, fg=self.black, font=self.font)
        self.goal_text.pack(side=TOP, padx=10, pady=10, expand=True)

        self.cycles = Label(self.frame_5, text='0 days', bg=self.blue, fg='white', font=self.font)
        self.cycles.pack(side=TOP, padx=10, pady=10, expand=True)

        self.button = Button(self.frame_5, text='Start', bg='green', relief=FLAT, command=self.start_stop)
        self.button.pack(side=TOP, padx=10, pady=10, expand=True)

        self.wallet = Label(self.frame_5, text='$$ %s' % self.money, bg=self.blue, fg='white', font=self.font)
        self.wallet.pack(side=TOP, padx=10, pady=10, expand=True)

    def start_stop(self):
        if self.running == 0:
            self.running = 1
            self.button.config(text='Stop', bg='red')
        elif self.running == 1:
            self.running = 0
            self.button.config(text='Start', bg='green')

    def update(self):
        
        self.input.config(text='supply\n%s Stored' % self.input_supply)
        self.input.after(self.time, self.update)

        if self.running == 1:

            self.supply_rph = int(self.entry_0.get())
            self.a_rph = int(self.entry_1.get())
            self.b_rph = int(self.entry_2.get())
            self.c_rph = int(self.entry_3.get())
            self.cycle += 1
            self.cycles.config(text='%s days' % self.cycle)

            if self.supply_rph > 0:
                self.input_supply += self.supply_rph
                self.machine_cost = (self.a_rph + self.b_rph + self.c_rph) * 1
                self.money = self.money - (self.supply_cost * self.supply_rph)
                self.money = self.money - self.machine_cost
                self.wallet.config(text='$$ %s' % self.money)
                self.input.config(text='supply\n%s Stored' % self.input_supply)
                
            if self.a_rph > 0 and self.input_supply >= self.a_rph:
                self.a_supply += self.a_rph
                self.input_supply -= self.a_rph
                self.step_a.config(text='Step A\n%s Stored' % self.a_supply)

            if self.b_rph > 0 and self.a_supply >= self.b_rph:
                self.b_supply += self.b_rph
                self.a_supply -= self.b_rph
                self.step_b.config(text='Step B\n%s Stored' % self.b_supply)

            if self.c_rph > 0 and self.b_supply >= self.c_rph:
                self.c_supply += self.c_rph
                self.b_supply -= self.c_rph
                self.step_c.config(text='Step C\n%s Stored' % self.c_supply)

            if self.c_supply >= self.c_rph:
                self.output_supply += self.c_rph
                self.c_supply -= self.c_rph
                self.money = self.money + (self.product_cost * self.c_rph)
                self.wallet.config(text='$$ %s' % self.money)
                self.output.config(text='products\n%s Made & Sold' % self.output_supply)

        
        




        
