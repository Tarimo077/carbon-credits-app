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
    sorted_list = sorted(my_list, key=lambda x: (x != 'Gas', x != 'Charcoal', x))
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
        self.primaryFuel = (self.kwh * 0.499) * 0.43
        self.emissions = self.primaryFuel
      else: 
        if self.fuels[0] == 'Charcoal':
          self.primaryFuel = (self.kwh * 0.499) * 0.73
          self.emissions = self.primaryFuel
        else:
          self.primaryFuel = (self.kwh * 0.499) * 0.85
          self.emissions = self.primaryFuel
    elif self.fuelNum == 2:
      if self.haveGas == True:
        if self.radio_button_1.selected == True:
          self.primaryProportion = 6/float(self.primary.text)
          self.secondaryProportion = float(self.secondary.text)
          self.totalProportion = self.primaryProportion + self.secondaryProportion
          self.primaryProportion = (self.primaryProportion/self.totalProportion) * 100
          self.secondaryProportion = (self.secondaryProportion/self.totalProportion) * 100
          self.primaryEmissions = (self.kwh * (self.primaryProportion/100) * 0.499) * 0.43
          self.secondaryEmissions = (self.kwh * (self.secondaryProportion/100) * 0.499) * 0.73
          self.emissions = self.primaryEmissions + self.secondaryEmissions
        else:
          self.primaryProportion = 13/float(self.primary.text)
          self.secondaryProportion = float(self.secondary.text)
          self.totalProportion = self.primaryProportion + self.secondaryProportion
          self.primaryProportion = (self.primaryProportion/self.totalProportion) * 100
          self.secondaryProportion = (self.secondaryProportion/self.totalProportion) * 100
          self.primaryEmissions = (self.kwh * (self.primaryProportion/100) * 0.499) * 0.43
          self.secondaryEmissions = (self.kwh * (self.secondaryProportion/100) * 0.499) * 0.73
          self.emissions = self.primaryEmissions + self.secondaryEmissions
      else:
        self.primaryProportion = float(self.primary.text)
        self.secondaryProportion = float(self.secondary.text)
        self.totalProportion = self.primaryProportion + self.secondaryProportion
        self.primaryProportion = (self.primaryProportion/self.totalProportion) * 100
        self.secondaryProportion = (self.secondaryProportion/self.totalProportion) * 100
        self.primaryEmissions = (self.kwh * (self.primaryProportion/100) * 0.499) * 0.73
        self.secondaryEmissions = (self.kwh * (self.secondaryProportion/100) * 0.499) * 0.85
        self.emissions = self.primaryEmissions + self.secondaryEmissions
    else:
      if self.radio_button_1.selected == True:
        self.primaryProportion = 6/float(self.primary.text)
        self.secondaryProportion = float(self.secondary.text)
        self.tertiaryProportion = float(self.tertiary.text)
        self.totalProportion = self.primaryProportion + self.secondaryProportion + self.tertiaryProportion
        self.primaryProportion = (self.primaryProportion/self.totalProportion) * 100
        self.secondaryProportion = (self.secondaryProportion/self.totalProportion) * 100
        self.tertiaryProportion = (self.tertiaryProportion/self.totalProportion) * 100
        self.primaryEmissions = (self.kwh * (self.primaryProportion/100) * 0.499) * 0.43
        self.secondaryEmissions = (self.kwh * (self.secondaryProportion/100) * 0.499) * 0.73
        self.tertiaryEmissions = (self.kwh * (self.tertiaryProportion/100) * 0.499) * 0.85
        self.emissions = self.primaryEmissions + self.secondaryEmissions + self.tertiaryEmissions
      else:
        self.primaryProportion = 13/float(self.primary.text)
        self.secondaryProportion = float(self.secondary.text)
        self.tertiaryProportion = float(self.tertiary.text)
        self.totalProportion = self.primaryProportion + self.secondaryProportion + self.tertiaryProportion
        self.primaryProportion = (self.primaryProportion/self.totalProportion) * 100
        self.secondaryProportion = (self.secondaryProportion/self.totalProportion) * 100
        self.tertiaryProportion = (self.tertiaryProportion/self.totalProportion) * 100
        self.primaryEmissions = (self.kwh * (self.primaryProportion/100) * 0.499) * 0.43
        self.secondaryEmissions = (self.kwh * (self.secondaryProportion/100) * 0.499) * 0.73
        self.tertiaryEmissions = (self.kwh * (self.tertiaryProportion/100) * 0.499) * 0.85
        self.emissions = self.primaryEmissions + self.secondaryEmissions + self.tertiaryEmissions
    self.n_emissions = (self.kwh * 0.499) * ((100 - self.eff)/100)
    self.credits = self.emissions - self.n_emissions
    self.credits = round(self.credits)
    creds = self.credits/1000
    alert("After switching to your new method you were able to reduce emissions by approximately " + str(self.credits) + " KGS representing around " + str(creds) + " carbon credits" )
      
        


