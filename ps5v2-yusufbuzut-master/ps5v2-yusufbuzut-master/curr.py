import numpy as np

class Currency:

  def __init__(self, code, total_days):

    self.code = code
    self.BUY = np.zeros(total_days)
    self.SELL = np.zeros(total_days)

  def get_data_fragment(self, idx_1, idx_2, param):

    data = self.__getattribute__(param)

    return data[int(idx_1):int(idx_2)]

  def calc_change(self, idx_1, idx_2, prop):

    """
    :param idx_1: first date index
    :param idx_2: second date index
    :param prop: property to be measured
    :return:
    """
    data = self.get_data_fragment(idx_1, (idx_2)+1, prop)
    value = ((data[len(data)-1] - data[0])/data[0])*100  
    # TODO

    return value

  def calc_mean(self,idx_1, idx_2, prop):

    """
    Calculates mean of a property given date indices
    :param idx_1: first date index
    :param idx_2: second date index
    :param prop: property to be measured
    :return:
    """

    value = np.mean(self.get_data_fragment(idx_1, idx_2, prop))#TODO

    return value

  def calc_volatility(self, idx_1, idx_2,prop):

    """
    Calculates volatility value given date indices
    :param idx_1: first date index
    :param idx_2: second date index
    :param prop: property to be measured
    :return:
    """


    value = np.var(self.get_data_fragment(idx_1, idx_2, prop)) 
    # TODO

    return value


  def calc_max(self, idx_1, idx_2, prop):

    """
    Desc
    :param idx_1: first date index
    :param idx_2: second date index
    :param prop: property to be measured
    :return: float
    """

    value = np.max(self.get_data_fragment(idx_1, idx_2, prop)) # TODO

    return value

  def calc_min(self, idx_1, idx_2, prop):

    """
    Desc
    :param idx_1: first date index
    :param idx_2: second date index
    :param prop: property to be measured
    :return: float
    """

    value =  np.min(self.get_data_fragment(idx_1, idx_2, prop))# TODO

    return value


if __name__ == "__main__":

  # DON'T MODIFY THIS!  
  total_days = 10
  c = Currency("EUR", total_days)
  np.random.seed(42)
  c.BUY = 5.0*np.ones(total_days) + np.random.rand(total_days)
  c.SELL = c.BUY + 0.1

  print("Change: ", c.calc_change(0, 7, "BUY"))
  print("Vol: ", c.calc_volatility(2, 9, "SELL"))
  print("Max: ",c.calc_max(4, 9, "SELL"))
  print("Mean: ",c.calc_mean(4, 9, "SELL"))
  print("Min: ",c.calc_min(0, 3, "BUY"))








