def list_duplicates(seq):
  seen = set()
  seen_add = seen.add
  seen_twice = set( x for x in seq if x in seen or seen_add(x) )
  return list( seen_twice )


alist = ['a','b','c','d','e','f','g','b','f','r','c','z','n','r'] 
print(alist)

alist_repeat = list_duplicates(alist)
print(alist_repeat)

