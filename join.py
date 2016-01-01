import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: order_id (The attribute we are joining on)
    # value: The entire record
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)
    
def reducer(key, list_of_values):
    # key: order_id (The attribute we are joining on)
    # list_of_values: A list of lists containing entire record
    for record in list_of_values:
      if record[0]=='order':
        for otherrecords in list_of_values:
          if otherrecords[0] == 'line_item':
            mr.emit(record+otherrecords)      # The final result should contain both the records as we are performing a join
            

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
