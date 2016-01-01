import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line
def mapper(record):
    # key: name of person
    # value: name of friend
    key = record[0]
    value = record[1]
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    for person in list_of_values:
      if person in mr.intermediate.keys():
        if key not in mr.intermediate[person]:
          mr.emit((key, person))
          mr.emit((person,key))
      else:
        mr.emit((key,person))
        mr.emit((person, key))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
