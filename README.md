# Problem 

Given a list of patients which contains Blood Glucose details. Create a Hashing data structure that is used to store a large amount of data, which can be accessed in O(1) time by operations such as search, insert and delete.

**Write the following declarations and implementations:**</br>
1. display_hash(hashtable) method displays the hashtable.
2. insert(Hashtable, keyvalue, value) method that inserts a value onto a Hashtable, where Hashtable is a list of lists and keyvlaue is used to find the hash function using Hashing(keyvalue) method.

# Constraints
The data of every patient details is a list of integer and string.

**Input Format**</br>
First line contains integer which represents the size of hashtable.</br>
Second line contains a collection of lists, where each list conatins the blood glucose level and name of patient.

## Sample Input - 1
```
3
[150, 'Tom'], [150, 'Jerry'], [131, 'Mickey'], [122, 'Donald'], [123, 'Ben'], [130, 'Scooby'].
```
## Sample Output - 1
```
0 --> 'Tom' --> 'Jerry' --> 'Ben' 
1 --> 'Scooby' 
2 --> 'Mickey' --> 'Donald'
```
*Explaination*</br>
0, 1 and 2 are indices.</br>
Tom's blood glucose level is 150. The Hashing(150) returns 0 (150 % 3 = 0). So it is stored in 0<sup>th</sup> index.</br>
Jerry's blood glucose level is 150. The Hashing(150) returns 0 (150 % 3 = 0). It is chained on 0<sup>th</sup> index.</br>
Mickey's blood glucose level is 131. The Hashing(131) returns 2 (131 % 3 = 2). So it is stored in 2<sup>nd</sup> index.</br>
Donald's blood glucose level is 122. The Hashing(122) returns 2 (122 % 3 = 2). So it is chained on 2<sup>nd</sup> index.</br>
Ben's blood glucose level is 123. The Hashing(123) returns 0 (150 % 3 = 0). It is chained on 0<sup>th</sup> index.</br>
Scooby's blood glucose level is 130. The Hashing(130) returns 2 (130 % 3 = 1). So it is stored in 1<sup>st</sup> index.</br>

## Sample Input - 2
```
10
[80, 'John'], [79, 'Shiney'], [101, 'Jincy'], [91, 'Sunitha'], [95, 'Binu'], [122, 'Betty'], [123, 'Yogi'], [94, 'Motu'], [96, 'Patlu'], [97, 'Nicky'], [98, 'Ricky'], [99, 'Aidan'].
```
## Sample Output - 2
```
0 --> 'John' 
1 --> 'Jincy' --> 'Sunitha' 
2 --> 'Betty' 
3 --> 'Yogi' 
4 --> 'Motu' 
5 --> 'Binu' 
6 --> 'Patlu' 
7 --> 'Nicky' 
8 --> 'Ricky' 
9 --> 'Shiney' --> 'Aidan'
```
