#####
#   This package recreates Thompson's Group F as a

#import networkx as nx

def findNth(input, target, n):
    start = input.find(target)
    while start >= 0 and n > 1:
        start = input.find(target, start+1)
        n -= 1
    return start

class ThompsonF():
  """|This is a class representation of Thompson's Group F, given the following presentation by generators and relations\:
  |
  |:math:`F = \\left\\langle x_0, x_1, x_2, \\ldots, x_n, \\ldots \\mid x_i^{-1}x_jx_i = x_{j+1} \\text{ for } i < j \\right\\rangle`.
  |
  |An element of the group is represented by an object of the ThompsonF class.

  :param subs: A list containing the subscripts of the generators that appear
    in the given element, from left to right in increasing index order. Entries
    must be nonnegative integers. For example, the element :math:`x_5^2x_3x_7^{-1}x_{11}^3x_0^{-7}`
    would be initialized with subs = [5, 3, 7, 11, 0].
  :type subs: list[int]
  :param exps: A list containing the exponents of the generators that appear
    in the given element, from left to right in increasing index order, including
    exponents of 1. Entries can be positive or negative nonzero integers. The length of
    this list must match the length of the above *subs* parameter. For example, the element :math:`x_5^2x_3x_7^{-1}x_{11}^3x_0^{-7}`
    would be initialized with exps = [2, 1, -1, 3, -7].
  :type exps: list[int]
  """

  # Lists to collect unicode codes for superscripts and subscripts, for printing purposes.
  unicode_subs = ["\u2080", "\u2081", "\u2082", "\u2083", "\u2084", "\u2085", "\u2086", "\u2087", "\u2088", "\u2089"]
  unicode_sups = ["\u2070", "\u00B9", "\u00B2", "\u00B3", "\u2074", "\u2075", "\u2076", "\u2077", "\u2078", "\u2079"]

  def __init__(self, subs = [0], exps = [0]):
    """Constructor method
    """
    if len(subs) == len(exps):
      self._subs = subs
      self._exps = exps
    else:
      raise Exception("Number of subscripts and exponents must be equal.")

  def __str__(self):
    if self._subs == [0] and self._exps == [0]:
      return "1"
    genstring = ""
    for i in range(len(self._subs)):
      genstring += "x"
      for digit in str(self._subs[i]):
        genstring += ThompsonF.unicode_subs[int(digit)]
      if self._exps[i] < 0:
        genstring += "\u207B"
        for digit in str(-1*self._exps[i]):
          genstring += ThompsonF.unicode_sups[int(digit)]
      elif self._exps[i] > 1:
        for digit in str(self._exps[i]):
          genstring += ThompsonF.unicode_sups[int(digit)]
    return genstring

  #####
  #
  #
  def forestDiagram(self):

    # Place each individual positive element in one list,
    # and each individual negative elements in another.
    # Both are in descending order.
    norm = self.normalForm()

    top_elements = []
    bot_elements = []
    for i in range(len(norm._subs)-1, -1, -1):
      if norm._exps[i] > 0:
        top_elements += [norm._subs[i]] * norm._exps[i]
      else:
        bot_elements += [norm._subs[i]] * abs(norm._exps[i])

    # Begin with a trivial tree (empty string).
    # Each tree is represented by a string of brackets.
    # Each set of brackets represents the left and right
    # child of the current node.

    top_forest = ["."]
    top_pointer = 0
    bot_forest = ["."]
    bot_pointer = 0

    # Each x0 moves the top pointer right, each x0^(-1) moves it left.
    # Each xi for i > 0 connects trees i-1 and i with a caret on top.

    for elem in bot_elements:
      if elem == 0:
        top_forest.insert(0,".")
        bot_forest.insert(0,".")
        bot_pointer += 1
      else:
        num_leaves = " ".join(bot_forest).count(".")
        if num_leaves < elem:
          top_forest += ["."] * (elem - num_leaves)
          bot_forest += ["."] * (elem - num_leaves)
        top_forest.insert(top_pointer + elem, ".")
        temp_join = " ".join(bot_forest)
        #leaf_to_replace = findNth(temp_join, ".", elem)
        start = temp_join.find(".")
        n = elem
        while start >= 0 and n > 1:
          start = temp_join.find(".", start+1)
          n -= 1
        leaf_to_replace = start
        new_forest = temp_join[:leaf_to_replace] + "(.)(.)" + temp_join[leaf_to_replace+1:]
        bot_forest = new_forest.split(" ")

    for elem in top_elements:
      if elem == 0:
        if top_pointer == len(top_forest) - 1:
          bot_forest += ["."]
          top_forest += ["."]
        top_pointer += 1
      else:
        if len(top_forest) < top_pointer + elem + 1:
          bot_forest += ["."] * (top_pointer + elem + 1 - len(top_forest))
          top_forest += ["."] * (top_pointer + elem + 1 - len(top_forest))
        right_tree = top_forest.pop(top_pointer + elem)
        left_tree = top_forest.pop(top_pointer + elem - 1)
        new_tree = "(" + left_tree + ")(" + right_tree + ")"
        top_forest.insert(top_pointer + elem - 1, new_tree)

    top_forest = " ".join(top_forest)
    bot_forest = " ".join(bot_forest)

    # Pad the lists at the end so they are the same size.

    if ".".count(top_forest) < ".".count(bot_forest):
      top_forest += [" ."] * (".".count(bot_forest) - ".".count(top_forest))
    elif ".".count(bot_forest) < ".".count(top_forest):
      bot_forest += [" ."] * (".".count(top_forest) - ".".count(bot_forest))
    top_forest = " " + top_forest + " "
    bot_forest = " " + bot_forest + " "

    return (top_forest, top_pointer, bot_forest, bot_pointer)

  #####
  # Takes an arbitrary element of F and returns the same element in normal form.
  #
  def normalForm(self):

    # Create a list with single elements listed one by one,
    # with exponent +/-1.

    elements = []
    signs = []
    for entry in range(len(self._subs)):
      elements += [self._subs[entry]] * abs(self._exps[entry])
      if self._exps[entry] < 0:
        signs += [-1] * abs(self._exps[entry])
      else:
        signs += [1] * self._exps[entry]

    if elements == []:
      return ThompsonF([0],[0])

    elem = 0
    while elem <= max(elements):
      curr = 0

      # Start at x0. Move left-to-right through the elements,
      # moving any instance of x0 to the left. Then we move any
      # instance of x0^(-1) to the right.

      while curr <= len(elements) - 1:

        # Case 1: If we see two adjacent elements with the same subscript
        # and opposing signs, cancel them. Move backwards one element.
        if curr < len(elements) - 1 and elements[curr] == elements[curr + 1] and signs[curr] == signs[curr + 1] * (-1):
          elements.pop(curr+1)
          elements.pop(curr)
          signs.pop(curr+1)
          signs.pop(curr)
          if elements == []:
            return ThompsonF([0],[0])
          if curr > 0:
            curr -= 1
          #print(Thompson(elements,signs))

        # Case 2: If we see a positive element where the element to the left has
        # a higher subscript, move the positive element left and increase the
        # higher element by one. Move backwards one element.
        elif curr > 0 and elements[curr] == elem and elements[curr-1] > elem and signs[curr] == 1:
          elements[curr-1], elements[curr] = elements[curr], elements[curr-1]+1
          signs[curr-1], signs[curr] = signs[curr], signs[curr-1]
          if curr > 0:
            curr -= 1
          #print(Thompson(elements,signs))

        # Case 3: If we see a negative element where the element to the right has
        # a higher subscript, move the negative element right and increase
        # the higher element by one. Move backwards one element.
        elif curr < len(elements) - 1 and elements[curr] == elem and elements[curr+1] > elem and signs[curr] == -1:
          elements[curr+1], elements[curr] = elements[curr], elements[curr+1]+1
          signs[curr+1], signs[curr] = signs[curr], signs[curr+1]
          if curr > 0:
            curr -= 1

        # Case 4: None of the above hold. In this case, the elements are in the
        # proper order, and we can move forward.
        else:
          curr += 1
      elem += 1

    # Now we are in seminormal form. We must re-combine the elements and
    # finish by simplifying into normal form.

    new_subs = [elements.pop(0)]
    new_exps = [signs.pop(0)]

    while elements != []:
      if elements[0] == new_subs[-1]:
        new_exps[-1] = new_exps[-1] + signs.pop(0)
        elements.pop(0)
      else:
        new_subs.append(elements.pop(0))
        new_exps.append(signs.pop(0))

    # To go from seminormal form to normal form, we check if any element i
    # appears twice. If so, if i+1 does not appear in any element, we decrease
    # all of the subscripts between them by 1, and cancel 1 from the exponents
    # on each of the occurrences of i. If this makes one 0, delete it.

    m = max(new_subs)
    for i in range(m+1):
      occurrences = [x for x in range(len(new_subs)) if new_subs[x] == i]
      if len(occurrences) == 2 and i+1 not in new_subs:
        for j in range(occurrences[0]+1,occurrences[1]):
          new_subs[j] = new_subs[j] - 1

        for occ in occurrences[::-1]:
          if new_exps[occ] in [-1,1]:
            new_exps.pop(occ)
            new_subs.pop(occ)
          elif new_exps[occ] < -1:
            new_exps[occ] = new_exps[occ] + 1
          elif new_exps[occ] > 1:
            new_exps[occ] = new_exps[occ] - 1

    return ThompsonF(new_subs, new_exps)

  def __mul__(self, other):
    return ThompsonF(self._subs + other._subs, self._exps + other._exps).normalForm()

  def __eq__(self, other):
    norm1 = self.normalForm()
    norm2 = other.normalForm()
    return norm1._subs == norm2._subs and norm1._exps == norm2._exps

  def __len__(self):

    if self._subs == [0] and self._exps == [0]:
      return 0

    full_diagram = self.forestDiagram()
    top_forest = full_diagram[0]

    # Run through and label the top forest.
    top_labels = []
    top_pointer = full_diagram[1]
    leaf_indices = [x for x in range(len(top_forest)) if top_forest[x] == "."]
    num_leaves = len(leaf_indices)
    for leaf in range(num_leaves - 1):
      last_index = 0 if leaf == 0 else leaf_indices[leaf - 1]
      index = leaf_indices[leaf]
      next_index = leaf_indices[leaf + 1]
      prev_level = top_forest[last_index:index+1].count("(")
      curr_level = top_forest[index:next_index+1].count("(")
      # If the current space is exterior and left of the pointer, label it
      # "L". We check that the leaf is not part of a caret and that it is
      # less than the top pointer.
      if " " in top_forest[index:next_index] and top_labels.count("L") < top_pointer:
        top_labels.append("L")
      # Otherwise, if it is immediately to the left of some caret, label
      # it "N". We check that there are at least two more leaves in the
      # diagram, and that the next two are part of a caret.
      elif curr_level > prev_level or " (" in top_forest[index:next_index]:
        top_labels.append("N")
      # Otherwise, if it is exterior and to the right of the pointer,
      # label it "R". Same as case for "L" with right instead of left.
      elif " " in top_forest[index:next_index] and index >= top_pointer:
        top_labels.append("R")
      # Otherwise, if it is interior, label it "I".
      elif top_forest[index+1] == ")":
        top_labels.append("I")

    bot_forest = full_diagram[2]

    # Run through and label the bottom forest.
    bot_labels = []
    bot_pointer = full_diagram[3]
    leaf_indices = [x for x in range(len(bot_forest)) if bot_forest[x] == "."]
    num_leaves = len(leaf_indices)
    for leaf in range(num_leaves - 1):
      last_index = 0 if leaf == 0 else leaf_indices[leaf - 1]
      index = leaf_indices[leaf]
      next_index = leaf_indices[leaf + 1]
      prev_level = bot_forest[last_index:index+1].count("(")
      curr_level = bot_forest[index:next_index+1].count("(")

      # If the current space is exterior and left of the pointer, label it
      # "L". We check that the leaf is not part of a caret and that it is
      # less than the top pointer.
      if " " in bot_forest[index:next_index] and bot_labels.count("L") < bot_pointer:
        bot_labels.append("L")
      # Otherwise, if it is immediately to the left of some caret, label
      # it "N". We check that there are at least two more leaves in the
      # diagram, and that the next two are part of a caret.
      elif curr_level > prev_level or " (" in bot_forest[index:next_index]:
        bot_labels.append("N")
      # Otherwise, if it is exterior and to the right of the pointer,
      # label it "R". Same as case for "L" with right instead of left.
      elif " " in bot_forest[index:next_index]:
        bot_labels.append("R")
      # Otherwise, if it is interior, label it "I".
      elif bot_forest[index+1] == ")":
        bot_labels.append("I")

    #print(top_labels)
    #print(bot_labels)

    # Make sure both label sets are the correct length.
    if len(bot_labels) != num_leaves - 1 or len(top_labels) != len(bot_labels):
      raise Exception("Error in index labeling.")

    weight = 0

    # Now we find the number of carets in the forests.
    weight += (top_forest.count("(") + bot_forest.count("(")) // 2

    # Finally, count up the weights of the spaces.
    for label_index in range(len(top_labels)):
      if top_labels[label_index] == "L":
        if bot_labels[label_index] == "L":
          weight += 2
        elif bot_labels[label_index] == "N":
          weight += 1
        elif bot_labels[label_index] == "R":
          weight += 1
        else:
          weight += 1
      if top_labels[label_index] == "N":
        if bot_labels[label_index] == "L":
          weight += 1
        elif bot_labels[label_index] == "N":
          weight += 2
        elif bot_labels[label_index] == "R":
          weight += 2
        else:
          weight += 2
      if top_labels[label_index] == "R":
        if bot_labels[label_index] == "L":
          weight += 1
        elif bot_labels[label_index] == "N":
          weight += 2
        elif bot_labels[label_index] == "R":
          weight += 2
        else:
          weight += 0
      if top_labels[label_index] == "I":
        if bot_labels[label_index] == "L":
          weight += 1
        elif bot_labels[label_index] == "N":
          weight += 2
        elif bot_labels[label_index] == "R":
          weight += 0
        else:
          weight += 0
    return weight

  #####
  #
  def inverse(self):
      norm = self.normalForm()
      new_exps = [(-1)*x for x in norm._exps[::-1]]
      new_subs = norm._subs[::-1]
      return ThompsonF(new_subs, new_exps).normalForm()
