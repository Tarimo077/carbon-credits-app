from ._anvil_designer import SecondTemplate
from anvil import *

class Second(SecondTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
