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

class tkinterApp(tkinter.Tk):
	
	# __init__ function for class tkinterApp
	def __init__(self, *args, **kwargs):
		
		# __init__ function for class Tk
		tkinter.Tk.__init__(self, *args, **kwargs)
		
		# creating a container
		container = tkinter.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		# initializing frames to an empty array
		self.frames = {}

		# iterating through a tuple consisting
		# of the different page layouts
		for F in (StartPage, Page1, Page2):

			frame = F(container, self)

			# initializing frame of that object from
			# startpage, page1, page2 respectively with
			# for loop
			self.frames[F] = frame

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(StartPage)

	# to display the current frame passed as
	# parameter
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

# first window frame startpage

class StartPage(tkinter.Frame):
	def __init__(self, parent, controller):
		tkinter.Frame.__init__(self, parent)
		
		# label of frame Layout 2
		label = ttk.Label(self, text ="Startpage", font = LARGEFONT)
		
		# putting the grid in its place by using
		# grid
		label.grid(row = 0, column = 1, padx = 10, pady = 10)

		prevButton = ttk.Button(self, text ="Page 1",
		command = lambda : controller.show_frame(Page1))
	
		# putting the button in its place by
		# using grid
		prevButton.grid(row = 4, column = 4, padx = 10, pady = 10)

		## button to show frame 2 with text layout2
		nextButton = ttk.Button(self, text ="Page 2",
		command = lambda : controller.show_frame(Page2))
	
		# putting the button in its place by
		# using grid
		nextButton.grid(row = 4, column = 5, padx = 10, pady = 10)


# second window frame page1
class Page1(tkinter.Frame):
	
	def __init__(self, parent, controller):
		tkinter.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Page 1", font = LARGEFONT)
		label.pack(side=tkinter.TOP, padx=10,pady=10)

		bottom_bar = tkinter.Frame(master=self)
		bottom_bar.pack(side=tkinter.BOTTOM)

		prevButton = ttk.Button(bottom_bar, text ="Start Page",
							command = lambda : controller.show_frame(StartPage))

		prevButton.grid(row = 0, column = 2, padx = 10, pady = 10)

		nextButton = ttk.Button(bottom_bar, text ="Page 2",
							command = lambda : controller.show_frame(Page2))
	
		nextButton.grid(row = 0, column = 3, padx = 10, pady = 10)

		fig = graphs.household_dwelling_bar_decade(household_type=household_type)
		print("displayed")
		print(fig)
		canvas = FigureCanvasTkAgg(fig, master=self)  # A tk.DrawingArea.
		canvas.draw()
		toolbar = NavigationToolbar2Tk(canvas, self, pack_toolbar=False)
		toolbar.update()
		canvas.mpl_connect(
            "key_press_event", lambda event: print(f"you pressed {event.key}"))
		canvas.mpl_connect("key_press_event", key_press_handler)
		
		def update_frequency(new_val):
			None
			
		slider_update = tkinter.Scale(bottom_bar, from_=1, to=5, orient=tkinter.HORIZONTAL,
                                    command=update_frequency, label="Frequency [Hz]")
		slider_update.grid(row = 0, column = 1, padx = 10, pady = 10)
		toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.X, padx=10,pady=10)
		canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=10,pady=10)



# third window frame page2
class Page2(tkinter.Frame):
	def __init__(self, parent, controller):
		tkinter.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Page 2", font = LARGEFONT)
		label.pack(side=tkinter.TOP, padx=10,pady=10)

		bottom_bar = tkinter.Frame(self)
		bottom_bar.pack(side=tkinter.BOTTOM)

		# button to show frame 2 with text
		# layout2
		prevButton = ttk.Button(bottom_bar, text ="Page 1",
							command = lambda : controller.show_frame(Page1))
		prevButton.grid(row = 0, column = 2, padx = 10, pady = 10)

		# button to show frame 3 with text
		# layout3
		nextButton = ttk.Button(bottom_bar, text ="Startpage",
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place by
		# using grid
		nextButton.grid(row = 0, column = 3, padx = 10, pady = 10)
		fig = graphs.household_dwelling_line(household_type=household_type)
		canvas = FigureCanvasTkAgg(fig, master=self)  # A tk.DrawingArea.
		canvas.draw()
		toolbar = NavigationToolbar2Tk(canvas, self, pack_toolbar=False)
		toolbar.update()
		canvas.mpl_connect(
            "key_press_event", lambda event: print(f"you pressed {event.key}"))
		canvas.mpl_connect("key_press_event", key_press_handler)
		
		def update_frequency(new_val):
			None
			
		slider_update = tkinter.Scale(bottom_bar, from_=1, to=5, orient=tkinter.HORIZONTAL,
                                    command=update_frequency, label="Frequency [Hz]")
		slider_update.grid(row = 0, column = 1, padx = 10, pady = 10)
		# slider_update.pack(side=tkinter.BOTTOM, padx=10,pady=10)
		toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.X, padx=10,pady=10)
		canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=10,pady=10)

# Driver Code
household_type, household_occupier_type, household_size, household_type_tenancy, household_child = graphs.initialize()
app = tkinterApp()
app.mainloop()