class Flow:
  def __init__(self, amount, prefix):
    self.amount = amount
    self.prefix = prefix

class FluidFlow(Flow):
  def __init__(self, amount, ftype):
    super.__init__(amount, 'ml')
    self.ftype = ftype

class ElectricCurrent(Flow):
  def __init__(self, amps, voltage):
    super.__init__(amps, 'amps')

class BulkFlow(Flow):
  def __init__(self, weight, itype):
    super.__init__(amount, 'pounds')
    self.itypes = items

class MixedFlow(Flow):
  def __init__(self, weight, items):
    super.__init__(amount, 'pounds'):
    self.items = items

class Attachment:
  def __init__(self, id):
    self.id = id

class Capacitor(Attachment):
  def __init__(self, id, cap, voltage, lpt):
    super.__init__(id)
    self.cap = cap
    self.voltage = voltage
    self.lpt = lpt

class Tank(Attachment):
  def __init__(self, id, cap, heat, gasses=False):
    super.__init__(id)
    self.cap = cap
    self.heat = heat
    self.gasses = gasses
    self.fill = 0
    self.fill_type = None
  def input(self, inp):
    if self.fill_type != None and self.fill_type != inp.ftype:
      print(f'cannot add {inp.ftype} to tank already filled with {self.fill_type}')
    else:
      fill += inp.amount
  def output(self, amount):
    o = FluidFlow()
    if amount > fill:
    
      t, f = fill_type, fill
      fill = 0
      fill_type = None
      return t, f
    else:
      fill -= amount
      return fill_type, fill
      
  
class Tile:
  def __init__(self, name, src, pos, grid):
    self.name = name
    self.src = src
    self.pos = pos
    self.grid = grid

class Block(Tile):
  def __init__(self, name, src, pos, grid):
    super.__init__(name, src, pos, grid)

class Single(Block):
  def __init__(self, name, src, pos, grid, attachments, voltage, connectors):
    super.__init__(name, src, pos, grid)
    self.attachments = attachments
    self.prime_capacitor = 0
    self.input_tanks = [1]
    self.output_tanks = [2]
    self.voltage = voltage
    self.connectors = connectors
    # [-1, -1, -1, -1]
    # (0, 1) = 0
    # (1, 0) = 1
    # (0, -1) = 2
    # (-1, 0) = 3
    # -1 = no connection
  def input(face, inp):
    id = connectors[face]
    attachments[id].input(inp)
  def get_connect(face):
    
  
      
    id = connectors[face]
    return self.attachments[id]
  def id_get(id):
    return self.attachments[id]
  def get_neighbor(face):
    

class Hatch:
  def __init__(self):
    pass

class Pump(Hatch):
  def __init__(self, host, draw, transfer_rate, face):
    self.host = host
    self.draw = draw
    self.tr = transfer_rate
    self.face = face
  def tick(self):
    