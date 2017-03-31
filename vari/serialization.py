import pickle

# mylist = ['a','b','c','d']

# with open('datafile.txt','w') as fh:
#     pickle.dump(mylist,fh)

# with open('datafile.txt') as fh:
#     unpickedlist = pickle.load(fh)
#
# print unpickedlist

this_int = 555
this_string = 'oh my goodness'
mydict_of_lists = {
    'a':[1,2,3],
    'b':[4,5,6]
}
query_results = [('joe',22,'clerk'),('pete',34,'salesman')]

with open('datafile_complex.txt','w') as fhcom:
    pickle.dump((this_int,this_string,mydict_of_lists,query_results),fhcom)

with open('datafile_complex.txt') as fhcom_read:
    tup = pickle.load(fhcom_read)

print tup[0]
print tup[1]
print tup[2]
print tup[3]
