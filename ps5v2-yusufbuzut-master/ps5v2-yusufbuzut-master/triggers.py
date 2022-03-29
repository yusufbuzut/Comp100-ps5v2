from curr import Currency
import numpy as np

class Trigger(object):

  def __init__(self, func, prop, threshold, date_start_idx,
                date_end_idx, date_start_str,  date_end_str):

    self.func = func
    self.prop = prop

    self.date_start_str = date_start_str
    self.date_end_str = date_end_str

    self.date_start_idx = date_start_idx
    self.date_end_idx = date_end_idx
    
    self.threshold = threshold

  def calc_value(self, curr):
    if self.func== 'MIN':
      value = Currency.calc_min(curr,self.date_start_idx,self.date_end_idx,self.prop)

    elif self.func== 'MAX':
      value = Currency.calc_max(curr,self.date_start_idx,self.date_end_idx,self.prop)
    elif self.func== 'VOL':
      value = Currency.calc_volatility(curr,self.date_start_idx,self.date_end_idx,self.prop)
    elif self.func== 'CHG':
      value = Currency.calc_change(curr,self.date_start_idx,self.date_end_idx,self.prop)
    elif self.func== 'MEAN':



      value = curr.calc_mean(self.date_start_idx, self.date_end_idx, self.prop)

    # TODO


    return value

  def evaluate(self, value):
    """
    Returns True if an alert should be generated
    for the given news item, or False otherwise.
    """
    # DO NOT CHANGE THIS!
    raise NotImplementedError

  def __repr__(self):

    return f'{self.func}, {self.prop}, {self.threshold}) in between ({self.date_start_str} - {self.date_end_str}'


class HighTrigger(Trigger):
  def __init__(self, func, prop, threshold, date_start_idx,
                date_end_idx, date_start_str,  date_end_str):
    super().__init__(func, prop, threshold, date_start_idx,
              date_end_idx, date_start_str,  date_end_str)

  def evaluate(self, curr):

    x = False
    if  self.calc_value( curr) > self.threshold:
      x = True
    # TODO

    return x

      
  def __repr__(self):
    """
    :return: Printable representation of the object.
    """

    return f'HighTrigger({super().__repr__()})'

class LowTrigger(Trigger):

  def __init__(self, func, prop, threshold, date_start_idx,
                date_end_idx, date_start_str,  date_end_str):
    super().__init__(func, prop, threshold, date_start_idx,
              date_end_idx, date_start_str,  date_end_str)

  def evaluate(self, curr):
    x = False
    if  self.calc_value(curr) < self.threshold:
      x = True
    # TODO


    return x

  def __repr__(self):
    """
    :return: Printable representation of the object.
    """

    return f'LowTrigger({super().__repr__()})'

class NotTrigger(Trigger):

  def __init__(self, trigger):
    self.trigger = trigger

  def evaluate(self, curr):
    x = self.trigger.evaluate(curr) 

    # TODO
    
    return  not x

  def __repr__(self):
    """
    :return: Printable representation of the object.
    """
    return f'NotTrigger({self.trigger})'


class AndTrigger(Trigger):
  def __init__(self, trigger1, trigger2):
    self.trigger1 = trigger1
    self.trigger2 = trigger2

  def evaluate(self, curr):
    x = self.trigger1.evaluate(curr) 
    y = self.trigger2.evaluate(curr) 
    

    return x and y

  def __repr__(self):
    """
    :return: Printable representation of the object.
    """
    return f'AndTrigger({self.trigger1}, {self.trigger2})'


class OrTrigger(Trigger):
  def __init__(self, trigger1, trigger2):

    self.trigger1 = trigger1
    self.trigger2 = trigger2

  def evaluate(self, curr):
    x = self.trigger1.evaluate(curr) 
    y = self.trigger2.evaluate(curr) 
    # TODO

    return x or y

  def __repr__(self):
    """
    :return: Printable representation of the object.
    """
    return f'OrTrigger({self.trigger1}, {self.trigger2})'

  
if __name__ == "__main__":

  # DON'T MODIFY THIS!
  total_days = 30
  c = Currency("EUR", 30)
  np.random.seed(42)
  c.BUY = 5.0 * np.ones(total_days) + np.random.rand(total_days)
  c.SELL = c.BUY + 0.1

  t1 = LowTrigger('MIN', 'SELL', 5.1, 2, 5, "",  "")
  t2 = HighTrigger('VOL', 'BUY', 0.01, 0, 7, "",  "")
  t3 = HighTrigger('MEAN', 'BUY', 5.0, 2, 5, "",  "")
  t4 = NotTrigger(t1)
  t5 = OrTrigger(t1,t2)
  t6 = AndTrigger(t4,t3)

  print("t1 - ", t1.evaluate(c))
  print("t2 - ", t2.evaluate(c))
  print("t3 - ", t3.evaluate(c))
  print("t4 - ", t4.evaluate(c))
  print("t5 - ", t5.evaluate(c))
  print("t6 - ", t5.evaluate(c))
