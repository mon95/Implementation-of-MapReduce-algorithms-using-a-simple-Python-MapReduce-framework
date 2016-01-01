import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier - string indicating the name of the book
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
      # emit_intermediate() generates the required inverted index
      mr.emit_intermediate(w, key)       


def reducer(key, list_of_values):
    # key: word 
    # value: each contains the list of docs containing the word(i.e. key)
    # No reducer function needed
    # But, convert to a set and back to list to remove duplicates
    mr.emit((key, list(set(list_of_values)) ))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
