def get_connector(face):
  if face == 0:
    return (0, 1)
  if face == 1:
    return (1, 0)
  if face == 2:
    return (0, -1)
  if face == 3:
    return (-1, 0)
def get_op(face):
  if face <= 1:
    return face+2
  else:
    return face-2


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
    super.__init__(weight, 'pounds')
    self.itype = itype

class MixedFlow(Flow):
  def __init__(self, weight, items):
    super.__init__(weight, 'pounds')
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
    o = FluidFlow(0, self.fill_type)
    if amount > fill:
    
      o.amount = fill
      fill = 0
      fill_type = None
      return o
    else:
      fill -= amount
      o.amount = amount
      return o
  def tick(self):
    pass
      
  
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
  def __init__(self, name, src, pos, grid, attachments, hatches, voltage, connectors):
    super.__init__(name, src, pos, grid)
    self.attachments = attachments
    self.hatches = hatches
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
  def input(self, face, inp):
    id = self.connectors[face]
    self.attachments[id].input(inp)
  def get_connect(self, face):
    
  
      
    id = self.connectors[face]
    return self.attachments[id]
  def id_get(self, id):
    return self.attachments[id]
  def get_neighbor(self, face):
    fp = get_connector(face)
    x = self.pos[0]+fp[0]
    y = self.pos[1]+fp[1]
    return self.grid[x][y]
  def tick(self):
    for a in self.attachments:
      pass
    for h in self.hatches:
      movement, energy = h.tick()
      tokens = movement.split()
      t = int(tokens[1])
      o = None
      if tokens[0][0] == '%':
        o = self.attachments[int(tokens[0][1:])]
    

class Hatch:
  def __init__(self):
    pass

class Pump(Hatch):
  def __init__(self, draw, transfer_rate, face, apt, v):
    self.draw = draw
    self.tr = transfer_rate
    self.face = face
    self.current = ElectricCurrent(apt, v)
  def tick(self):
    return f"%{self.draw} {self.transfer_rate} [neighbor]", self.current