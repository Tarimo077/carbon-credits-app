from ._anvil_designer import FirstTemplate
from anvil import *

class First(FirstTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.drop_down_1.items = ['Charcoal','Firewood', 'Gas']
    self.drop_down_1.selected_value = self.drop_down_1.items[0]
    self.slctList = []
    self.num = 1
    self.radio = False
    

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    x = self.drop_down_1.selected_value
    if x not in self.slctList:
      self.slctList.append(x)
      self.fuelItems.text += "\nFuel Source " + str(self.num) + ": " + str(x)
      self.num += 1

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.slctList = []
    self.fuelItems.text = ""
    self.num = 1

  def radio_button_2_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    self.radio = False
    self.efficiency.enabled = True
    self.efficiency.text = ''

  def radio_button_1_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    self.radio = True
    self.efficiency.enabled = False
    self.efficiency.text = 72

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.projectEmissions.text is None or self.efficiency.text is None or len(self.slctList) == 0:
      alert("Kindly fill in all fields")
    else:
      open_form('Second', self.slctList, self.projectEmissions.text, self.efficiency.text)


    


        
    

