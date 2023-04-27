from tkinter import ttk

import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
import graphs

household_type, household_occupier_type, household_size, household_type_tenancy, household_child = None, None, None, None, None

LARGEFONT =("Verdana", 24)
CONTENTFONT = ("Verdana",16)

class tkinterApp(tkinter.Tk):
	
	# __init__ function for class tkinterApp
	def __init__(self, *args, **kwargs):
		
		tkinter.Tk.__init__(self, *args, **kwargs)
		
		container = tkinter.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		self.frames = {}

		for F in (HomePage, Page1, Page2, Page3, Page4, Page5, Page6, Page7, Page8, Page9, Page10, Page11):

			frame = F(container, self)

			self.frames[F] = frame

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(HomePage)

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

class HomePage(tkinter.Frame):
	def __init__(self, parent, controller):
		tkinter.Frame.__init__(self, parent)

		label = ttk.Label(self, text ="Home Page", font = LARGEFONT)
		
		label.grid(row = 0, column = 1, padx = 10, pady = 10, sticky=tkinter.W)

		label = ttk.Label(self, text ="Click start browsing to view visualisations of Singapore household demographics!", font = CONTENTFONT)
		
		label.grid(row = 1, column = 1, columnspan=4, padx = 10, pady = 10, sticky=tkinter.W)

		label = ttk.Label(self, text ="Enter full screen for the best experience!", font = CONTENTFONT)
		
		label.grid(row = 2, column = 1, columnspan=4, padx = 10, pady = 10, sticky=tkinter.W)


		startButton = ttk.Button(self, text="Start Browsing!",
		command = lambda : controller.show_frame(Page1))
	
		startButton.grid(row = 4, column = 1, padx = 10, pady = 10, sticky=tkinter.W)

class Page1(tkinter.Frame):
	
	def __init__(self, parent, controller):
		tkinter.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Household Dwelling Distribution over Decades", font = LARGEFONT)
		label.pack(side=tkinter.TOP, padx=10,pady=10)

		bottom_bar = tkinter.Frame(master=self)
		bottom_bar.pack(side=tkinter.BOTTOM)

		nextButton = ttk.Button(bottom_bar, text ="Next",
							command = lambda : controller.show_frame(Page2))

		nextButton.grid(row = 0, column = 2, padx = 10, pady = 10)

		homeButton = ttk.Button(bottom_bar, text ="Back to Home",
							command = lambda : controller.show_frame(HomePage))
	
		homeButton.grid(row = 0, column = 3, padx = 10, pady = 10)

		fig = graphs.household_dwelling_bar_decade(household_type=household_type)
		canvas = FigureCanvasTkAgg(fig, master=self)  # A tk.DrawingArea.
		canvas.draw()
		toolbar = NavigationToolbar2Tk(canvas, self, pack_toolbar=False)
		toolbar.update()
		canvas.mpl_connect(
            "key_press_event", lambda event: print(f"you pressed {event.key}"))
		canvas.mpl_connect("key_press_event", key_press_handler)

		toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.X, padx=10,pady=10)
		canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=10,pady=10)

class Page2(tkinter.Frame):
	def __init__(self, parent, controller):
		tkinter.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Residential Households by Dwellings over the years", font = LARGEFONT)
		label.pack(side=tkinter.TOP, padx=10,pady=10)

		bottom_bar = tkinter.Frame(self)
		bottom_bar.pack(side=tkinter.BOTTOM)

		prevButton = ttk.Button(bottom_bar, text ="Previous",
							command = lambda : controller.show_frame(Page1))
		prevButton.grid(row = 0, column = 2, padx = 10, pady = 10)

		nextButton = ttk.Button(bottom_bar, text ="Next",
							command = lambda : controller.show_frame(Page3))
		nextButton.grid(row = 0, column = 3, padx = 10, pady = 10)
		
		homeButton = ttk.Button(bottom_bar, text ="Back to Home",
					command = lambda : controller.show_frame(HomePage))
	
		homeButton.grid(row = 0, column = 4, padx = 10, pady = 10)
	
		
		fig = graphs.household_dwelling_line(household_type=household_type)
		canvas = FigureCanvasTkAgg(fig, master=self)  # A tk.DrawingArea.
		canvas.draw()
		toolbar = NavigationToolbar2Tk(canvas, self, pack_toolbar=False)
		toolbar.update()
		canvas.mpl_connect(
            "key_press_event", lambda event: print(f"you pressed {event.key}"))
		canvas.mpl_connect("key_press_event", key_press_handler)

		toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.X, padx=10,pady=10)
		canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=10,pady=10)

class Page3(tkinter.Frame):
	def __init__(self, parent, controller):
		tkinter.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Household Properties by Dwelling", font = LARGEFONT)
		label.pack(side=tkinter.TOP, padx=10,pady=10)

		bottom_bar = tkinter.Frame(self)
		bottom_bar.pack(side=tkinter.BOTTOM)

		prevButton = ttk.Button(bottom_bar, text ="Previous",
							command = lambda : controller.show_frame(Page2))
		prevButton.grid(row = 0, column = 2, padx = 10, pady = 10)

		nextButton = ttk.Button(bottom_bar, text ="Next",
							command = lambda : controller.show_frame(Page4))
		nextButton.grid(row = 0, column = 3, padx = 10, pady = 10)
		
		homeButton = ttk.Button(bottom_bar, text ="Back to Home",
					command = lambda : controller.show_frame(HomePage))
	
		homeButton.grid(row = 0, column = 4, padx = 10, pady = 10)
	
		str_year = str(1983)
		labels = household_type['Data Series']
		sizes = household_type[str_year]

		fig = Figure(dpi=60)
		ax = fig.subplots()
		ax.pie(sizes,labels=labels,autopct='%1.1f%%')
		ax.set_title("Proportion of household properties in "+str_year)
		canvas = FigureCanvasTkAgg(fig, master=self)  # A tk.DrawingArea.
		canvas.draw()
		toolbar = NavigationToolbar2Tk(canvas, self, pack_toolbar=False)
		toolbar.update()
		canvas.mpl_connect(
            "key_press_event", lambda event: print(f"you pressed {event.key}"))
		canvas.mpl_connect("key_press_event", key_press_handler)
		
		def update_year(new_val):
			str_year = str(new_val)
			sizes = household_type[str_year]
			ax.clear()
			ax.pie(sizes,labels=labels,autopct='%1.1f%%')
			ax.set_title("Proportion of household properties in "+str_year)
			canvas.draw()
			
		slider_update = tkinter.Scale(bottom_bar, from_=1983, to=2022, orient=tkinter.HORIZONTAL,
                                    command=update_year, label="Year")
		slider_update.grid(row = 0, column = 1, padx = 10, pady = 10)
		toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.X, padx=10,pady=10)
		canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=10,pady=10)

class Page4(tkinter.Frame):
	def __init__(self, parent, controller):
		tkinter.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Household Demographics over the years", font = LARGEFONT)
		label.pack(side=tkinter.TOP, padx=10,pady=10)

		bottom_bar = tkinter.Frame(self)
		bottom_bar.pack(side=tkinter.BOTTOM)

		prevButton = ttk.Button(bottom_bar, text ="Previous",
							command = lambda : controller.show_frame(Page3))
		prevButton.grid(row = 0, column = 2, padx = 10, pady = 10)

		nextButton = ttk.Button(bottom_bar, text ="Next",
							command = lambda : controller.show_frame(Page5))
		nextButton.grid(row = 0, column = 3, padx = 10, pady = 10)
		
		homeButton = ttk.Button(bottom_bar, text ="Back to Home",
					command = lambda : controller.show_frame(HomePage))
	
		homeButton.grid(row = 0, column = 4, padx = 10, pady = 10)
	
		
		fig = graphs.household_demographics(household_occupier_type=household_occupier_type)
		canvas = FigureCanvasTkAgg(fig, master=self)  # A tk.DrawingArea.
		canvas.draw()
		toolbar = NavigationToolbar2Tk(canvas, self, pack_toolbar=False)
		toolbar.update()
		canvas.mpl_connect(
            "key_press_event", lambda event: print(f"you pressed {event.key}"))
		canvas.mpl_connect("key_press_event", key_press_handler)
		
		toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.X, padx=10,pady=10)
		canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=10,pady=10)

class Page5(tkinter.Frame):
	def __init__(self, parent, controller):
		tkinter.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Household Properties by Reference Person's Age", font = LARGEFONT)
		label.pack(side=tkinter.TOP, padx=10,pady=10)

		bottom_bar = tkinter.Frame(self)
		bottom_bar.pack(side=tkinter.BOTTOM)

		prevButton = ttk.Button(bottom_bar, text ="Previous",
							command = lambda : controller.show_frame(Page4))
		prevButton.grid(row = 0, column = 2, padx = 10, pady = 10)

		nextButton = ttk.Button(bottom_bar, text ="Next",
							command = lambda : controller.show_frame(Page6))
		nextButton.grid(row = 0, column = 3, padx = 10, pady = 10)
		
		homeButton = ttk.Button(bottom_bar, text ="Back to Home",
					command = lambda : controller.show_frame(HomePage))
	
		homeButton.grid(row = 0, column = 4, padx = 10, pady = 10)
	
		fig = graphs.household_reference(household_occupier_type=household_occupier_type)
		canvas = FigureCanvasTkAgg(fig, master=self)  # A tk.DrawingArea.
		canvas.draw()
		toolbar = NavigationToolbar2Tk(canvas, self, pack_toolbar=False)
		toolbar.update()
		canvas.mpl_connect(
            "key_press_event", lambda event: print(f"you pressed {event.key}"))
		canvas.mpl_connect("key_press_event", key_press_handler)
		
		toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.X, padx=10,pady=10)
		canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=10,pady=10)

class Page6(tkinter.Frame):
	def __init__(self, parent, controller):
		tkinter.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Household Properties by Demographics", font = LARGEFONT)
		label.pack(side=tkinter.TOP, padx=10,pady=10)

		bottom_bar = tkinter.Frame(self)
		bottom_bar.pack(side=tkinter.BOTTOM)

		prevButton = ttk.Button(bottom_bar, text ="Previous",
							command = lambda : controller.show_frame(Page5))
		prevButton.grid(row = 0, column = 2, padx = 10, pady = 10)

		nextButton = ttk.Button(bottom_bar, text ="Next",
							command = lambda : controller.show_frame(Page7))
		nextButton.grid(row = 0, column = 3, padx = 10, pady = 10)
		
		homeButton = ttk.Button(bottom_bar, text ="Back to Home",
					command = lambda : controller.show_frame(HomePage))
	
		homeButton.grid(row = 0, column = 4, padx = 10, pady = 10)
	
		household_occupier_type_demographics = household_occupier_type[household_occupier_type["Type"]!="Resident Households"]
		household_occupier_type_demographics = household_occupier_type_demographics.groupby(by="Data Series").sum()
		household_occupier_type_demographics = household_occupier_type_demographics.reset_index()
		labels = household_occupier_type_demographics['Data Series']
		str_year = str(2000)
		fig = Figure(dpi=60)
		ax = fig.subplots()
		sizes = household_occupier_type_demographics[str_year]
		ax.pie(sizes,labels=labels,autopct='%1.1f%%')
		ax.set_title("Households by demographics distribution in "+str_year)
		canvas = FigureCanvasTkAgg(fig, master=self)  # A tk.DrawingArea.
		canvas.draw()
		toolbar = NavigationToolbar2Tk(canvas, self, pack_toolbar=False)
		toolbar.update()
		canvas.mpl_connect(
            "key_press_event", lambda event: print(f"you pressed {event.key}"))
		canvas.mpl_connect("key_press_event", key_press_handler)
		
		def update_year(new_val):
			str_year = str(new_val)		
			sizes = household_occupier_type_demographics[str_year]
			ax.clear()
			ax.pie(sizes,labels=labels,autopct='%1.1f%%')
			ax.set_title("Households by demographics distribution in "+str_year)
			canvas.draw()
			
		slider_update = tkinter.Scale(bottom_bar, from_=2000, to=2022, orient=tkinter.HORIZONTAL,
                                    command=update_year, label="Year")
		slider_update.grid(row = 0, column = 1, padx = 10, pady = 10)
		toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.X, padx=10,pady=10)
		canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=10,pady=10)

class Page7(tkinter.Frame):
	def __init__(self, parent, controller):
		tkinter.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Household Properties by Reference Person's Age in Particular Year", font = LARGEFONT)
		label.pack(side=tkinter.TOP, padx=10,pady=10)

		bottom_bar = tkinter.Frame(self)
		bottom_bar.pack(side=tkinter.BOTTOM)

		prevButton = ttk.Button(bottom_bar, text ="Previous",
							command = lambda : controller.show_frame(Page6))
		prevButton.grid(row = 0, column = 2, padx = 10, pady = 10)

		nextButton = ttk.Button(bottom_bar, text ="Next",
							command = lambda : controller.show_frame(Page8))
		nextButton.grid(row = 0, column = 3, padx = 10, pady = 10)
		
		homeButton = ttk.Button(bottom_bar, text ="Back to Home",
					command = lambda : controller.show_frame(HomePage))
	
		homeButton.grid(row = 0, column = 4, padx = 10, pady = 10)
	
		household_occupier_age = household_occupier_type.groupby(by="Type").sum()
		household_occupier_age = household_occupier_age.rename(index=
			{"Household Reference Persons Aged 35-49 Years":"35 - 45 years","Household Reference Persons Aged 50-64 Years": "50 - 64 years",
			"Household Reference Persons Aged 65 Years & Over":">=65 years","Household Reference Persons Aged Below 35 Years":"<35 years"})
		household_occupier_age = household_occupier_age.reset_index()
		household_occupier_age = household_occupier_age[household_occupier_age["Type"]!="Resident Households"]
		labels = household_occupier_age['Type']

		fig = Figure(dpi=60)
		ax = fig.subplots()
		str_year = str(2000)
		sizes = household_occupier_age[str_year]
		ax.pie(sizes,labels=labels,autopct='%1.1f%%')
		ax.set_title("Households based on household reference person's age in "+str_year)
		
		canvas = FigureCanvasTkAgg(fig, master=self)  # A tk.DrawingArea.
		canvas.draw()
		toolbar = NavigationToolbar2Tk(canvas, self, pack_toolbar=False)
		toolbar.update()
		canvas.mpl_connect(
            "key_press_event", lambda event: print(f"you pressed {event.key}"))
		canvas.mpl_connect("key_press_event", key_press_handler)
		
		def update_year(new_val):
			str_year = str(new_val)		
			sizes = household_occupier_age[str_year]
			ax.clear()
			ax.pie(sizes,labels=labels,autopct='%1.1f%%')
			ax.set_title("Households based on household reference person's age in "+str_year)
			canvas.draw()
			
		slider_update = tkinter.Scale(bottom_bar, from_=2000, to=2022, orient=tkinter.HORIZONTAL,
                                    command=update_year, label="Year")
		slider_update.grid(row = 0, column = 1, padx = 10, pady = 10)
		toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.X, padx=10,pady=10)
		canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=10,pady=10)

class Page8(tkinter.Frame):
	
	def __init__(self, parent, controller):
		tkinter.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Household Dwelling Distribution over Decades", font = LARGEFONT)
		label.pack(side=tkinter.TOP, padx=10,pady=10)

		bottom_bar = tkinter.Frame(master=self)
		bottom_bar.pack(side=tkinter.BOTTOM)

		prevButton = ttk.Button(bottom_bar, text ="Next",
							command = lambda : controller.show_frame(Page7))

		prevButton.grid(row = 0, column = 2, padx = 10, pady = 10)

		nextButton = ttk.Button(bottom_bar, text ="Next",
							command = lambda : controller.show_frame(Page9))

		nextButton.grid(row = 0, column = 3, padx = 10, pady = 10)

		homeButton = ttk.Button(bottom_bar, text ="Back to Home",
							command = lambda : controller.show_frame(HomePage))
	
		homeButton.grid(row = 0, column = 4, padx = 10, pady = 10)

		fig = graphs.household_persons(household_size=household_size)
		canvas = FigureCanvasTkAgg(fig, master=self)  # A tk.DrawingArea.
		canvas.draw()
		toolbar = NavigationToolbar2Tk(canvas, self, pack_toolbar=False)
		toolbar.update()
		canvas.mpl_connect(
            "key_press_event", lambda event: print(f"you pressed {event.key}"))
		canvas.mpl_connect("key_press_event", key_press_handler)

		toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.X, padx=10,pady=10)
		canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=10,pady=10)

class Page9(tkinter.Frame):
	def __init__(self, parent, controller):
		tkinter.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Households by Tenancy by Dwelling", font = LARGEFONT)
		label.pack(side=tkinter.TOP, padx=10,pady=10)

		bottom_bar = tkinter.Frame(self)
		bottom_bar.pack(side=tkinter.BOTTOM)

		prevButton = ttk.Button(bottom_bar, text ="Previous",
							command = lambda : controller.show_frame(Page8))
		prevButton.grid(row = 0, column = 2, padx = 10, pady = 10)

		nextButton = ttk.Button(bottom_bar, text ="Next",
							command = lambda : controller.show_frame(Page10))
		nextButton.grid(row = 0, column = 3, padx = 10, pady = 10)
		
		homeButton = ttk.Button(bottom_bar, text ="Back to Home",
					command = lambda : controller.show_frame(HomePage))
	
		homeButton.grid(row = 0, column = 4, padx = 10, pady = 10)

		household_type_tenancy_selected = household_type_tenancy.drop(index=[0,1,2,3,4])
		labels = household_type_tenancy_selected['Data Series']
		fig = Figure(dpi=60)
		ax = fig.subplots()
		
		str_year = str(2000)
		sizes = household_type_tenancy_selected[str_year]
		ax.pie(sizes,labels=labels,autopct='%1.1f%%')
		ax.set_title("Resident Households by Tenancy in "+str_year)
		canvas = FigureCanvasTkAgg(fig, master=self)  # A tk.DrawingArea.
		canvas.draw()
		toolbar = NavigationToolbar2Tk(canvas, self, pack_toolbar=False)
		toolbar.update()
		canvas.mpl_connect(
            "key_press_event", lambda event: print(f"you pressed {event.key}"))
		canvas.mpl_connect("key_press_event", key_press_handler)
		
		def update_year(new_val):
			str_year = str(new_val)
			sizes = household_type_tenancy_selected[str_year]
			ax.clear()
			ax.pie(sizes,labels=labels,autopct='%1.1f%%')
			ax.set_title("Resident Households by Tenancy in "+str_year)
			canvas.draw()
			
		slider_update = tkinter.Scale(bottom_bar, from_=2000, to=2022, orient=tkinter.HORIZONTAL,
                                    command=update_year, label="Year")
		slider_update.grid(row = 0, column = 1, padx = 10, pady = 10)
		toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.X, padx=10,pady=10)
		canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=10,pady=10)

class Page10(tkinter.Frame):
	def __init__(self, parent, controller):
		tkinter.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Residential Households by Living Arrangement over the years", font = LARGEFONT)
		label.pack(side=tkinter.TOP, padx=10,pady=10)

		bottom_bar = tkinter.Frame(self)
		bottom_bar.pack(side=tkinter.BOTTOM)

		prevButton = ttk.Button(bottom_bar, text ="Previous",
							command = lambda : controller.show_frame(Page9))
		prevButton.grid(row = 0, column = 2, padx = 10, pady = 10)

		nextButton = ttk.Button(bottom_bar, text ="Next",
							command = lambda : controller.show_frame(Page11))
		nextButton.grid(row = 0, column = 3, padx = 10, pady = 10)
		
		homeButton = ttk.Button(bottom_bar, text ="Back to Home",
					command = lambda : controller.show_frame(HomePage))
	
		homeButton.grid(row = 0, column = 4, padx = 10, pady = 10)
	
		
		fig = graphs.household_living_arrangement(household_child=household_child)
		canvas = FigureCanvasTkAgg(fig, master=self)  # A tk.DrawingArea.
		canvas.draw()
		toolbar = NavigationToolbar2Tk(canvas, self, pack_toolbar=False)
		toolbar.update()
		canvas.mpl_connect(
            "key_press_event", lambda event: print(f"you pressed {event.key}"))
		canvas.mpl_connect("key_press_event", key_press_handler)

		toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.X, padx=10,pady=10)
		canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=10,pady=10)

class Page11(tkinter.Frame):
	def __init__(self, parent, controller):
		tkinter.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Households by Age of Youngest Child in a particular year", font = LARGEFONT)
		label.pack(side=tkinter.TOP, padx=10,pady=10)

		bottom_bar = tkinter.Frame(self)
		bottom_bar.pack(side=tkinter.BOTTOM)

		prevButton = ttk.Button(bottom_bar, text ="Previous",
							command = lambda : controller.show_frame(Page10))
		prevButton.grid(row = 0, column = 2, padx = 10, pady = 10)
		
		homeButton = ttk.Button(bottom_bar, text ="Back to Home",
					command = lambda : controller.show_frame(HomePage))
	
		homeButton.grid(row = 0, column = 3, padx = 10, pady = 10)

		household_child_with_child_married = household_child[household_child["Type"]=="  Married Couple-Based With Children"]
		household_child_with_child_married = household_child_with_child_married.set_index("Data Series")
		household_child_with_child_married = household_child_with_child_married.rename(
			index={"    With Youngest Child Aged Below 6 Years":"<6 years","    With Youngest Child Aged 6 - 11 Years":"6 - 11 years",
				"    With Youngest Child Aged 12 - 15 Years":"12 - 15 years","    With Youngest Child Aged 16 Years And Over":">=16 years"})
		household_child_with_child_married = household_child_with_child_married.reset_index()
		labels = household_child_with_child_married['Data Series']

		fig = Figure(dpi=60)
		ax = fig.subplots()
		str_year = str(2000)
		sizes = household_child_with_child_married[str_year]
		ax.pie(sizes,labels=labels,autopct='%1.1f%%')
		ax.set_title("Resident Households by Age of Youngest Child for Married Households with Children "+str_year)
		
		canvas = FigureCanvasTkAgg(fig, master=self)  # A tk.DrawingArea.
		canvas.draw()
		toolbar = NavigationToolbar2Tk(canvas, self, pack_toolbar=False)
		toolbar.update()
		canvas.mpl_connect(
            "key_press_event", lambda event: print(f"you pressed {event.key}"))
		canvas.mpl_connect("key_press_event", key_press_handler)
		
		def update_year(new_val):
			str_year = str(new_val)
			sizes = household_child_with_child_married[str_year]
			ax.clear()
			ax.pie(sizes,labels=labels,autopct='%1.1f%%')
			ax.set_title("Resident Households by Age of Youngest Child for Married Households with Children "+str_year)
			canvas.draw()
			
		slider_update = tkinter.Scale(bottom_bar, from_=2000, to=2022, orient=tkinter.HORIZONTAL,
                                    command=update_year, label="Year")
		slider_update.grid(row = 0, column = 1, padx = 10, pady = 10)
		toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.X, padx=10,pady=10)
		canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=10,pady=10)

# Driver Code
household_type, household_occupier_type, household_size, household_type_tenancy, household_child = graphs.initialize()
app = tkinterApp()
app.mainloop()