#!/usr/bin/env python


from gi.repository import Gtk

class AppWindow(Gtk.Window):
	def __init__(self):
		#Window Properties
		Gtk.Window.__init__(self, title="Shutdown")
		self.set_border_width(10)
		self.set_position(Gtk.WindowPosition.CENTER)

		#Box
		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		SpinBox = Gtk.Box(spacing=10)
		RBBox = Gtk.Box(spacing = 10)
		BBox = Gtk.Box(spacing = 10)

		#Label
		self.StatusLabel = Gtk.Label("Select One of the options")

		#SpinButtons
		HAdjustment = Gtk.Adjustment(0, 0, 23, 1, 10, 0)
		MAdjustment = Gtk.Adjustment(0, 0, 59, 1, 10, 0)	

		self.SBHours = Gtk.SpinButton()
		self.SBHours.set_adjustment(HAdjustment)

		self.SBMinutes = Gtk.SpinButton()
		self.SBMinutes.set_adjustment(MAdjustment)

		#RadioButtons
		self.ShutdownRB = Gtk.RadioButton.new_with_label_from_widget(None,"Shutdown")
		self.ShutdownRB.connect("toggled",self.on_button_toggled, "shutdown")

		self.RestartRB = Gtk.RadioButton.new_from_widget(self.ShutdownRB)
		self.RestartRB.set_label("Restart")
		self.RestartRB.connect("toggled",self.on_button_toggled, "restart")

		self.HaltRB = Gtk.RadioButton.new_from_widget(self.ShutdownRB)
		self.HaltRB.set_label("Halt")
		self.HaltRB.connect("toggled",self.on_button_toggled, "halt")

		#Buttons
		self.DoneButton = Gtk.Button("Done")
		self.DoneButton.connect("clicked",self.Done_Clicked)

		self.CancelButton = Gtk.Button("Cancel")
		self.CancelButton.connect("clicked",self.Cancel_Clicked)

		#Boxes
		##Horizontal Boxes
		SpinBox.pack_start(self.SBHours,True,True,0)
		SpinBox.pack_start(self.SBMinutes,True,True,0)

		RBBox.pack_start(self.ShutdownRB,True,True,0)
		RBBox.pack_start(self.RestartRB,True,True,0)
		RBBox.pack_start(self.HaltRB,True,True,0)

		BBox.pack_start(self.DoneButton,True,True,0)
		BBox.pack_start(self.CancelButton,True,True,0)

		#Vertical Boxes
		vbox.pack_start(self.StatusLabel,False,False,2)
		vbox.pack_start(SpinBox,False,False,2)
		vbox.pack_start(RBBox,False,False,2)
		vbox.pack_start(BBox,False,False,2)

		#Add Box
		self.add(vbox)
		self.add(SpinBox)

	def on_button_toggled(self, button, name):
		if button.get_active():
			state = "on"
			labeltext = "You want",name,"your pc at"
			self.StatusLabel.set_text("You Want "+name +" at")
		else:
			state = "off"



	def Done_Clicked(self,button):
		print "Done Clicked"
		self.SBHours.set_sensitive(False)
		self.SBMinutes.set_sensitive(False)
		self.DoneButton.set_sensitive(False)
		self.ShutdownRB.set_sensitive(False)
		self.RestartRB.set_sensitive(False)
		self.HaltRB.set_sensitive(False)

	def Cancel_Clicked(self,button):
		print "Done Clicked"
		self.SBHours.set_sensitive(True)
		self.SBMinutes.set_sensitive(True)
		self.DoneButton.set_sensitive(True)
		self.ShutdownRB.set_sensitive(True)
		self.RestartRB.set_sensitive(True)
		self.HaltRB.set_sensitive(True)


win = AppWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
