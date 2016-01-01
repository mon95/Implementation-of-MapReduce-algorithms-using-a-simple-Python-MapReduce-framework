<span>Here, we design and implement MapReduce algorithms for a variety of common data processing tasks.  </span>
<span>This assignment was done as part of the "Data Manipulation at Scale: Systems and Algorithms" course (Part of the data science specialization certificate) offered by the University of Washington on Coursera.

The links and explanations and some sample code for the assignment is used as is from the course website.

As a side note, I would recommend this course to anyone interested in working on data science problems and looking for some cool work to enhance their skills.

Link to the same: https://www.coursera.org/learn/data-manipulation/home/welcome  </span>

# Python MapReduce Framework

Here, we use a python library called MapReduce.py that implements the MapReduce programming model. The framework faithfully implements the MapReduce programming model, but it executes entirely on a single machine, and it does not involve parallel computation.

Note: Ensure that MapReduce.py is in the same directory as the other scripts being used.

The expected output for running each script on the corresponding data in the *data* directory, is present in the *solutions* directory (with appropriate names for each file).

# Creating an Inverted Index

Given a set of documents, an inverted index is a dictionary where each word is associated with a list of the document identifiers in which that word appears. An inverted index is extremely important while building an efficient information retrieval system

## Mapper Input

<span>The input is a 2 element list: `[document_id, text]`, where `document_id` is a string representing a document identifier and `text` is a string representing the text of the document. The document text may have words in upper or lower case and may contain punctuation. Here, we treat each token as a valid word, for simplicity.</span>

## Reducer Output

<span>The output is a (word, document ID list) tuple where word is a String and document ID list is a list of Strings.</span>

<span></span>

<span>        python inverted_index.py books.json</span>

<span></span>

<span>Verify this  against inverted_index.json.</span>


<span>Implementing a relational join as a MapReduce query</span>

<span>Consider the following query:</span>

<pre>SELECT * 
FROM Orders, LineItem 
WHERE Order.order_id = LineItem.order_id
</pre>

The MapReduce query produces the same result as this SQL query executed against an appropriate database.

The two input tables - Order and LineItem - are considered as one big concatenated bag of records that will be processed by the map function record by record.

## Map Input

<span>Each input record is a list of strings representing a tuple in the database. Each list element corresponds to a different attribute of the table</span>

<span>The first item (index 0) in each record is a string that identifies the table the record originates from. This field has two possible values:</span>

*   "line_item" indicates that the record is a line item.
*   "order" indicates that the record is an order.

The second element (index 1) in each record is the order_id.

<span>LineItem records have 17 attributes including the identifier string.</span>

<span>Order records have 10 elements including the identifier string.</span>

<span>Reduce Output</span>

<span>The output is a joined record: a single list of length 27 that contains the attributes from the order record followed by the fields from the line item record. Each list element should be a string.</span>

<pre>$ python join.py records.json
</pre>

<span>Verify using join.json.</span>

# Counting the number of friends per person in a social network

<span>Consider a simple social network dataset consisting of a set of key-value pairs `(person, friend)` representing a friend relationship between two people. Describe a MapReduce algorithm to count the number of friends for each person.</span>

<span>Map Input</span>

Each input record is a 2 element list `[personA, personB]` where personA is a string representing the name of a person and personB is a string representing the name of one of personA's friends. 

</a><span>Reduce Output</span>

<span>The output is a pair `(person, friend_count)` where person is a string and friend_count is an integer indicating the number of friends associated with person.</span>

<pre>$ python friend_count.py friends.json
</pre>

<span>Verify this with the file friend_count.json.</span>

# Finding asymmetric friendships from social network data

<span>The relationship "friend" is often symmetric, meaning that if I am your friend, you are my friend. We use a MapReduce algorithm to check whether this property holds and generate a list of all non-symmetric friend relationships.</span>

</a><span>Map Input</span>

Each input record is a 2 element list `[personA, personB]` where personA is a string representing the name of a person and personB is a string representing the name of one of personA's friends. It may or may not be the case that the personA is a friend of personB.

</a><span>Reduce Output</span>

<span>The output is all pairs (friend, person) such that (person, friend) appears in the dataset but (friend, person) does not.</span>

<pre>$ python asymmetric_friendships.py friends.json
</pre>

<span>Verify this with the file asymmetric_friendships.json.</span>

# DNA Sequence trimming

<span>Consider a set of key-value pairs where each key is sequence id and each value is a string of nucleotides, e.g., GCTTCCGAAATGCTCGAA....</span>

<span>The MapReduce query removes the last 10 characters from each string of nucleotides, then removes any duplicates generated.</span>

## Map Input

<span>Each input record is a 2 element list `[sequence id, nucleotides]` where sequence id is a string representing a unique identifier for the sequence and nucleotides is a string representing a sequence of nucleotides</span>

## Reduce Output

<span>The output from the reduce function is the unique trimmed nucleotide strings.</span>

<pre>$ python unique_trims.py dna.json
</pre>

<span>Verify this with the file unique_trims.json.</span>

# Matrix multiplication

<span>Assume you have two matrices A and B in a sparse matrix format, where each record is of the form i, j, value. The MapReduce algorithm computes the matrix multiplication A x B</span>

</a><span>Map Input</span>

<span>The input to the map function will be a row of a matrix represented as a list. Each list will be of the form `[matrix, i, j, value]` where matrix is a string and i, j, and value are integers.</span>

<span>The first item, matrix, is a string that identifies which matrix the record originates from. This field has two possible values: "a" indicates that the record is from matrix A and "b" indicates that the record is from matrix B</span>

## Reduce Output

<span>The output from the reduce function is also a row of the result matrix represented as a tuple. Each tuple will be of the form (i, j, value) where each element is an integer.</span>

<pre>$ python multiply.py matrix.json</pre>

<span>Verify this with the file multiply.json.</span>