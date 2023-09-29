from ._anvil_designer import SecondTemplate
from anvil import *

class Second(SecondTemplate):
  def __init__(self, fuels, consumption, efficiency, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    fuelNum = len(fuels)
    self.fuelNum = fuelNum
    self.kwh = float(consumption)
    self.eff = float(efficiency)
    sorted_list = sorted(fuels, key=lambda x: x != 'Gas')
    fuels = sorted_list
    self.fuels = fuels
    haveGas = fuels.__contains__('Gas')
    self.haveGas = haveGas
    if(haveGas == True):
      pass
    else:
      self.radio_button_1.visible = False
      self.radio_button_2.visible = False
    if fuelNum == 1:
      if (haveGas == True):
        self.lblPrimary.text = "How long does a full cylinder of gas last you?(weeks)"
      else:
        self.lblPrimary.text = "How many kilos of " + str(fuels[0]) + " do you use in a week?"
      self.lblSecondary.visible = False
      self.lblTertiary.visible = False
      self.tertiary.visible = False
      self.secondary.visible = False
    elif fuelNum == 2:
      if (haveGas == True):
        self.lblPrimary.text = "How long does a full cylinder last you?(weeks)"
        self.lblSecondary.text = "How many kilos of " + str(fuels[1]) + " do you use in a week?"
      else:
        self.lblPrimary.text = "How many kilos of " + str(fuels[0]) + " do you use in a week?"
        self.lblSecondary.text = "How many kilos of " + str(fuels[1]) + " do you use in a week?"
      self.lblTertiary.visible = False
      self.tertiary.visible = False
    else:
     self.lblPrimary.text = "How long does a full cylinder last you?(weeks)"
     self.lblSecondary.text = "How many kilos of " + str(fuels[1]) + " do you use in a week?"
     self.lblTertiary.text = "How many kilos of " + str(fuels[2]) + " do you use in a week?"      

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('First')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.fuelNum == 1:
      if self.haveGas == True:
        if self.radio_button_1.selected == True:
          self.gasKilo = 6
        else:
          self.gasKilo = 13


