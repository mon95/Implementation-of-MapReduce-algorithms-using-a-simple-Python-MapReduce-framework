import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line
    
def mapper(record):     # Here we are using a 5x5 Matrix
    if record[0]=='a':
      for k in range(5):  # Here, here '5' refers to the number of columns in matrix B 
        key = (record[1],k)
        value = (0, record[2], record[3]) 
        mr.emit_intermediate(key, value)
    else:
      for i in range(5):  # Here, 5 refers to the number of rows in matrix A
        key = (i,record[2])
        value = (1, record[1], record[3])
        mr.emit_intermediate(key,value)

def reducer(key, list_of_values):
    print list(key), list_of_values

    # key: (i,k)
    # value: list of (0_or_1_indicating_matrix, j, matrix[i,j])

    hashA = {}
    hashB = {}

    for item in list_of_values:
      if item[0]==0:  # Matrix A
        hashA[item[1]] = item[2]
      else:
        hashB[item[1]] = item[2]
    print "B: ",hashB
    print "A: ",hashA
    result = 0

    for j in range(5):    # refers to no of rows of A (same as no of cols of B)
      try:
        result += hashA[j]*hashB[j]
      except:
        pass
    mr.emit(tuple(list(key)+[result]))



# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
