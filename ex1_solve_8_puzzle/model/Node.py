from .Functions import *

class Node:
    def __init__(self, para_stage, para_parent, para_action_from_parent = "NONE"):
        self.stage = para_stage
        self.parent = para_parent
        self.path_cost = 0 if para_parent is None else para_parent.path_cost + 1
        #action_from_parent là hành động mà nút cha thự hiện thì ra nút này
        self.action_from_parent = para_action_from_parent

    def get_child_node(self):
        '''
        Tìm tất các các nút con của node
        Input : None
        Output: List các nút con của node
        '''
        zero_index = self.stage.index(0)
        child_node = []

        if (zero_index % 3 > 0) :
            new_stage = Functions.swap_list(self.stage, zero_index, zero_index - 1)
            child_node.append(Node(new_stage, self, "LEFT"))

        if (zero_index > 2) :
            new_stage = Functions.swap_list(self.stage, zero_index, zero_index - 3)
            child_node.append(Node(new_stage, self, "UP"))

        if (zero_index % 3 < 2) :
            new_stage = Functions.swap_list(self.stage, zero_index, zero_index + 1)
            child_node.append(Node(new_stage, self, "RIGHT"))

        if (zero_index < len(self.stage) - 3) :
            new_stage = Functions.swap_list(self.stage, zero_index, zero_index + 3)
            child_node.append(Node(new_stage, self, "DOWN"))

        return child_node

    def get_solution(self):
        '''
        Tìm soulution từ node
        '''
        node = self
        solution = ''
        while not (node.parent is None) :
            solution = node.action_from_parent + '-' + solution
            node = node.parent
        return solution
