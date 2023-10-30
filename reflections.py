def flatten_list(list):
  flatten_list = []
  for subl in list:
    for item in subl:
      flatten_list.append(item)

  sorted_list=sorted(flatten_list)
  return sorted_list


print(flatten_list([[7, 9], [2, 3]]))

# How does this solution ensure data immutability?
#   Answer: sorted_list is a new variable name for a new list that is a copy of the original flatten_list. 
#   This means that the original flatten_list is not mutated. sorted() makes a copy.
#   so flatten_list remains unchanged
# Is this solution a pure function? Why or why not?
#   Answer: Yes because all variables are contained within the function.
# Is this solution a higher order function? Why or why not?
#   Answer: No, not using functions as arguments or returning functions although does use sort which is 
#   not high order,
# Would it have been easier to solve this problem using a different programming style?
#   Answer: This works
# Why in particular is functional programming a helpful paradigm when solving this problem?
#   Answer: because it is a pure function, no side effects,  simple to read and efficient


class Podracer():

  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

  def repaired(self):
    self.condition = "repaired"


class AnakinsPod(Podracer):

  def __init__(self, max_speed, condition, price):
    super().__init__(max_speed, condition, price)

  def boost(self):
    self.max_speed = self.max_speed * 2


class SebulbasPod(Podracer):

  def __init__(self, max_speed, condition, price):
    super().__init__(max_speed, condition, price)

  def flame_jet(self, other):
    other.condition = "trashed"


podracer1 = Podracer(200, "new", 5000)
podracer1.repaired()
print(podracer1.condition)

podracer2 = AnakinsPod(2, "new", 10000)
podracer2.boost()
print(podracer2.max_speed)

third_pod = SebulbasPod(300, "new", 20000)
third_pod.flame_jet(third_pod)
print(third_pod.condition)
