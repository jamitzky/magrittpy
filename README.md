# magrittpy
The package provides a pipe operator to stitch together workflows composed out of ordinary python functions.
It is inspired by the magrittR package from R.

Basic usage:

`sum_of_lists = forall(x=list1, y=list2) >> flatmap(lambda x,y: x+y) >> sum >> result`
  
It consists of the two basic classes (which are used as keywords here) forall and result. The right-shift operator is overloaded so that functions can be stitched together into a workflow. Additionally adverbs can be definied which act as decorators and provide monad like features like map-reduce.

The package also provides a fork-like syntax like in J for dyads:

`(sum |div| len) == lambda x:sum(x)/len(x)`

which can be used inside the workflow:

`forall(range(10)) >> (sum |op(lambda x,y:x/y)| len) >> result`
