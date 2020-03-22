# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 21:33:05 2020

@author: wazir
"""


class Tree: 
    def __init__(self, x):
        self.rt = x
        self.child = []
        #self.__child = []
    
    def add_child(self, a): 
        """for i in self.child:
            if i == a.root():
                return None
        self.__child.append(a)"""
        
        self.child.append(a)
    
    def root(self): 
        return self.rt
    
    def ith_child(self, child_id):
        return self.child[child_id] if (len(self.child)-1 >= child_id) else None
            

    def num_children(self):
        return len(self.child)
    

class PreTree(Tree):
    def __init__(self, x):
        super(PreTree, self).__init__(x)
    
    def preorder(self):
        return  sorted(self._recursive_check())

    def _recursive_check(self):
        for child in self.child:
            yield from child._recursive_check()
        yield self.rt

t = PreTree(2)
t.add_child(PreTree(3))
t.add_child(PreTree(4))
t.num_children()
t.ith_child(1).add_child(PreTree(5))
print(t.preorder())


     
