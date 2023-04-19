import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()


class gui(tk.Frame):

    def __init__(self, parent=None):
        super().__init__()

        #initialize variables
        self.top = None
        self.toppinglist = None
        self.cheeselist = None
        self.sauce = None
        self.saucelist = None

        parent.title("Procedural Object-Oriented Pizza Company (P00P inc)")
        parent.geometry("800x600")
        #Title and Size

        self.pack(fill='both')
        self.columnconfigure(1, weight=1)
        tk.Label(self, text="Build Your Own Pizza!").grid(row=0, column=0, columnspan=2)

        #Aligning menu to left side of screen
        alignment = tk.Frame(self)
        alignment.grid(row=1, column=0, sticky='news')

        # button to make pizza
        tk.Button(alignment, text="Build Pizza", command=self.bakePizza,width=40).grid(row=22, column=0)

        #Calling methods
        self.size(alignment)
        self.Crust(alignment)
        self.Toppings(alignment)
        self.Sauce(alignment)
        self.seasoning(alignment)
        self.Cheese(alignment)

    def size(self, alignment):
        ttk.Separator(alignment, orient='horizontal').grid(row=1, column=0, sticky='ew')
        self.Size = tk.StringVar()
        tk.Label(alignment, text='Choose size').grid(row=2, column=0,pady=5)
        vFrame = tk.Frame(alignment)
        vFrame.grid(row=3, column=0, sticky="w")
        #small medium large buttons
        tk.Radiobutton(vFrame, text="Small", value="small", variable=self.Size).pack(side="left", padx=30,pady=5)
        tk.Radiobutton(vFrame, text="Medium", value="medium", variable=self.Size).pack(side="left",padx=20,pady=5)
        tk.Radiobutton(vFrame, text="Large", value="large", variable=self.Size).pack(side="left",padx=20,pady=5)
        #default value
        self.Size.set("medium")

    def Toppings(self, alignment):
        ttk.Separator(alignment, orient='horizontal').grid(row=12, column=0, sticky='ew')
        tk.Label(alignment, text="Choose Toppings").grid(row=13, column=0, sticky='w', padx=120)
        self.toppinglist = ['Chicken', 'Ham', 'Jalapeno', 'Mushroom', 'Olive', 'Onion', 'Pepper', 'Pepperoni', 'Tomato']
        # List of toppings
        self.top = [tk.IntVar() for _ in self.toppinglist]
        col = 2
        topbox = tk.Frame(alignment)
        topbox.grid(row=14, column=0, sticky='w',padx=100)
        for i, (text, var) in enumerate(zip(self.toppinglist, self.top)):
            # Enumerate over topping list, return tuple of index/value
            row = i // col
            column = i % col
            #create new checkbutton
            checkbox = tk.Checkbutton(topbox, text=text, variable=var)
            checkbox.grid(row=row, column=column, sticky='w', padx=5)

    def Cheese(self, alignment):
        Cheeses = ['None', 'Normal', 'Extra']
        #list of cheeses
        tk.Label(alignment, text="Choose Cheese").grid(row=11, column=0, sticky='w')
        self.cheeselist = tk.Listbox(alignment, height=len(Cheeses), width=15)
        self.cheeselist.grid(row=11, column=0, sticky="w", padx=120)
        #loop through cheeses
        for c in Cheeses:
            self.cheeselist.insert("end", c)
        #clear selections
        self.cheeselist.selection_clear(0, "end")
        #set to first option
        self.cheeselist.selection_set(0)

    def Crust(self, alignment):
        self.crust = tk.StringVar()
        ttk.Separator(alignment, orient='horizontal').grid(row=5, column=0, sticky='ew')
        tk.Label(alignment, text='Choose your crust').grid(row=6, column=0,pady=5)
        #label for crust

        vFrame = tk.Frame(alignment)
        vFrame.grid(row=7, column=0)
        #buttons
        tk.Radiobutton(vFrame, text='Chicago Deep Dish', value='CH', variable=self.crust).pack(side='left', padx=20)
        tk.Radiobutton(vFrame, text='New York Thick Crust', value='NY', variable=self.crust).pack(side='left')
        #default crust
        self.crust.set('NY')

    def Sauce(self, alignment):
        self.saucey = tk.StringVar()
        ttk.Separator(alignment, orient='horizontal').grid(row=8, column=0, sticky='ew')
        #label
        tk.Label(alignment, text='Choose your sauce').grid(row=9, sticky='w')
        vFrame = tk.Frame(alignment)
        #default sauce
        self.saucey.set(('Marinara'))
        vFrame.grid(row=9, column=0, sticky='news', padx=120)
        #options for sauce
        tk.OptionMenu(vFrame, self.saucey, 'Marinara', 'Chipotle', 'Alfredo', 'Barbeque').pack(side='left')

    def seasoning(self, alignment):
        ttk.Separator(alignment, orient='horizontal').grid(row=19, column=0, sticky='ew')
        self.saucelist = ['seasoning']
        #seasonings

        self.sauce = [tk.IntVar() for _ in self.saucelist]
        vFrame = tk.Frame(alignment)
        vFrame.grid(row=20, column=0)

        for text, var in zip(self.saucelist, self.sauce):
            #loop over saucelist to add seasoning properly
            checkbox = tk.Checkbutton(vFrame, text='Add Seasoning?', variable=var, pady=5)
            #checkbox with proper text
            checkbox.pack(anchor='w')
        ttk.Separator(alignment, orient='horizontal').grid(row=21, column=0, sticky='ew', pady=10)

    def bakePizza(self):
        if hasattr(self, 'pizzaLabel'):
            self.pizzaLabel.grid_forget()
        pizzaFrame = tk.Frame(self)
        pizzaFrame.grid(row=5, column=1, sticky='nsew')

        #getting variable values
        sauce = self.saucey.get()
        cheese = self.cheeselist.get(self.cheeselist.curselection())
        size = self.Size.get()
        crust = self.crust.get()

        # loop through toppings and sauce using i, grabs toppings and seasonings and sauce
        toppings = [self.toppinglist[i] for i, var in enumerate(self.top) if var.get()]
        seasonings = [self.saucelist[i] for i, var in enumerate(self.sauce) if var.get()]

        #sizes dictionary
        sizes = {
            "small": (350, 350),
            "medium": (400, 400),
            "large": (450, 450)
        }
        # size tuple from dictionary
        zasize = sizes.get(size)

        # cheeses
        cheese_images = {
            'None': None,
            'Normal': Image.open('./images/images/cheese_normal.png'),
            'Extra': Image.open('./images/images/cheese_extra.png')
        }
        currentCheese = cheese_images.get(cheese, None)
        if currentCheese:
            currentCheese = currentCheese.resize(zasize)

        # crusts
        crust_images = {
            'CH': Image.open('./images/images/crust_chicago.png'),
            'NY': Image.open('./images/images/crust_nyc.png')
        }
        currentCrust = crust_images.get(crust, None)
        if currentCrust:
            currentCrust = currentCrust.resize(zasize)

        # sauces
        sauce_images = {
            'Marinara': Image.open('./images/images/sauce_marinara.png'),
            'Chipotle': Image.open('./images/images/sauce_chipotle.png'),
            'Alfredo': Image.open('./images/images/sauce_alfredo.png'),
            'Barbeque': Image.open('./images/images/sauce_barbeque.png')
        }
        currentSauce = sauce_images.get(sauce, None)
        if currentSauce:
            currentSauce = currentSauce.resize(zasize)

        #topping dictionaries
        topping_images = {
            'pepperoni': './images/images/topping_pepperoni.png',
            'mushrooms': './images/images/topping_mushrooms.png',
            'olives': './images/images/topping_olives.png',

        }
        #sauces dictionaries
        sauce_images = {
            'Marinara': './images/images/sauce_marinara.png',
            'Chipotle': './images/images/sauce_chipotle.png',
            'Alfredo': './images/images/sauce_alfredo.png',
            'Barbeque': './images/images/sauce_barbeque.png',

        }

        #cheeses dictionaries
        cheese_images = {
            'Normal': './images/images/cheese_normal.png',
            'Extra': './images/images/cheese_extra.png',
        }

        # create pizza
        finalPizza = Image.new('RGBA', zasize, (255, 255, 255, 0))
        finalPizza.paste(currentCrust, (0, 0), currentCrust)
        finalPizza.paste(currentSauce, (0, 0), currentSauce)
        if currentCheese:
            finalPizza.paste(currentCheese, (0, 0), currentCheese)

        # add toppings
        for topping in toppings:
            toppingImage = Image.open(f'./images/images/topping_{topping}.png')
            toppingImage = toppingImage.resize(zasize)
            finalPizza.paste(toppingImage, (0, 0), toppingImage)

        # add seasoning
        for season in seasonings:
            seasonImage = Image.open('./images/images/seasoning.png')
            seasonImage = seasonImage.resize(zasize)
            finalPizza.paste(seasonImage, (0, 0), seasonImage)

        # convert final image to object
        pizza = ImageTk.PhotoImage(finalPizza)

        # create label, initialize properties, set height,width,image and position pizza
        self.pizzaLabel = tk.Label(self)
        self.pizzaLabel.config(image='')
        self.pizzaLabel.config(width=pizza.width(), height=pizza.height(), image=pizza)
        self.pizzaLabel.image = pizza  # reference to image

        self.pizzaLabel.grid(row=1, column=1, columnspan=2, sticky='e')  # position


window = gui(parent=root)
root.mainloop()

#Images
extraCheese = Image.open('./images/images/cheese_extra.png')
extraCheese.thumbnail((400, 400))
Cheese = Image.open('./images/images/cheese_normal.png')
Cheese.thumbnail((400, 400))
#cheese options

chicago = Image.open('./images/images/crust_chicago.png')
chicago.thumbnail((400, 400))

nyc = Image.open('./images/images/crust_nyc.png')
nyc.thumbnail((400, 400))
#crusts

#---
alfredo = Image.open('./images/images/sauce_alfredo.png')
alfredo.thumbnail((400, 400))

barbeque = Image.open('./images/images/sauce_barbeque.png')
barbeque.thumbnail((400, 400))

chipotle = Image.open('./images/images/sauce_chipotle.png')
chipotle.thumbnail((400, 400))

marinara = Image.open('./images/images/sauce_marinara.png')
marinara.thumbnail((400, 400))
#sauces

#----
chicken = Image.open('./images/images/topping_chicken.png')
chicken.thumbnail((400, 400))

ham = Image.open('./images/images/topping_ham.png')
ham.thumbnail((400, 400))

jalapeno = Image.open('./images/images/topping_jalapeno.png')
jalapeno.thumbnail((400, 400))

mushroom = Image.open('./images/images/topping_mushroom.png')
mushroom.thumbnail((400, 400))

olive = Image.open('./images/images/topping_olive.png')
olive.thumbnail((400, 400))

onion = Image.open('./images/images/topping_onion.png')
onion.thumbnail((400, 400))

pepper = Image.open('./images/images/topping_pepper.png')
pepper.thumbnail((400, 400))

pepperoni = Image.open('./images/images/topping_pepperoni.png')
pepperoni.thumbnail((400, 400))

tomato = Image.open('./images/images/topping_tomato.png')
tomato.thumbnail((400, 400))
#toppings


seasoning = Image.open('./images/images/seasoning.png')
seasoning.thumbnail((400, 400))
#seasoning