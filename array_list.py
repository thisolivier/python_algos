class ArrayList:
  def __init__(self):
    capacity = 6
    self.__capacity = capacity
    self.__underlyingList = [0] * capacity
    self.__count = 0

  def size(self):
    return self.__count

  def debug(self):
    return """
      Capacity: {}
      Count: {}
      Undelying List: {}
    """.format(self.__capacity, self.__count, self.__underlyingList)

  def replaceValue(self, index, newValue):
    if index < self.__count:
      self.__underlyingList[index] = newValue
    else:
      raise Exception('replaceValue: index out of range')
  
  def getValue(self, index):
    if index < self.__count:
      return self.__underlyingList[index]
    else:
      raise Exception('getValue: index out of range')
  
  def append(self, value):
    self.__ensureCanAppend()
    self.__underlyingList[self.__count] = value
    self.__count += 1
    return self

  def __ensureCanAppend(self):
    if self.__count == self.__capacity:
      self.__capacity = self.__capacity * 2
      newList = [0] * self.__capacity
      for index, value in enumerate(self.__underlyingList):
        newList[index] = value
      self.__underlyingList = newList

myList = ArrayList()
myList.append(3).append(4).append(1).append(2).append(7).append(9).append(2).append(7)
print(myList.debug())
myList.replaceValue(20, 4)
print(myList.getValue(2))
print(myList.debug())