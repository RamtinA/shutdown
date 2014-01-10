#!/usr/bin/env python


from gi.repository import Gtk

class AppWindow(Gtk.Window):
	def __init__(self):
		#Window Properties
		Gtk.Window.__init__(self, title="Shutdown")
		self.set_border_width(10)

		#Box
		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		SpinBox = Gtk.Box(spacing=10)
		RBBox = Gtk.Box(spacing = 10)
		BBox = Gtk.Box(spacing = 10)

		#Label
		StatusLabel = Gtk.Label("Select One of the options")

		#SpinButtons
		HAdjustment = Gtk.Adjustment(0, 0, 23, 1, 10, 0)
		MAdjustment = Gtk.Adjustment(0, 0, 59, 1, 10, 0)	

		SBHours = Gtk.SpinButton()
		SBHours.set_adjustment(HAdjustment)

		SBMinutes = Gtk.SpinButton()
		SBMinutes.set_adjustment(MAdjustment)

		#RadioButtons
		ShutdownRB = Gtk.RadioButton.new_with_label_from_widget(None,"Shutdown")
		ShutdownRB.connect("toggled",self.on_button_toggled, "1")

		RestartRB = Gtk.RadioButton.new_from_widget(ShutdownRB)
		RestartRB.set_label("Restart")
		#RestartRB.connect("toggled",defchoice,"restart")

		HaltRB = Gtk.RadioButton.new_from_widget(ShutdownRB)
		HaltRB.set_label("Halt")
		#HaltRB.connect("toggled",defchoice,"halt")

		#Buttons
		DoneButton = Gtk.Button("Done")
		CancelButton =Gtk.Button("Cancel")

		#Boxes
		##Horizontal Boxes
		SpinBox.pack_start(SBHours,True,True,0)
		SpinBox.pack_start(SBMinutes,True,True,0)

		RBBox.pack_start(ShutdownRB,True,True,0)
		RBBox.pack_start(RestartRB,True,True,0)
		RBBox.pack_start(HaltRB,True,True,0)

		BBox.pack_start(DoneButton,True,True,0)
		BBox.pack_start(CancelButton,True,True,0)

		#Vertical Boxes
		vbox.pack_start(StatusLabel,False,False,2)
		vbox.pack_start(SpinBox,False,False,2)
		vbox.pack_start(RBBox,False,False,2)
		vbox.pack_start(BBox,False,False,2)

		#Add Box
		self.add(vbox)
		self.add(SpinBox)

	def on_button_toggled(self, button, name):
		if button.get_active():
			state = "on"
		else:
			state = "off"
		print("Button", name, "was turned", state)



win = AppWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
