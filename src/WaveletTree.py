'''
Based on code from https://github.com/nectarios-ef/Wavelet-Tree in 2024
'''

from Node import Node

class WaveletTree(object):
    
    def __init__(self, data=None):
        if data == None:
            print("Please give correct parameters")
            return
        self.__root = Node(data)  #Create the parent node
        
    def rank(self,character=None, position=None):
        return self.__root.get_rank_query(position,character)
    
    def select(self,character=None, position=None):
        return self.__root.get_select_query(position + 1, character) - 1
    
    def access(self,position=None):
        return self.__root.get_track_symbol(position + 1)
