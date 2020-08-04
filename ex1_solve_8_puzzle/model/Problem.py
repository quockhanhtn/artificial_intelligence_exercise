from .Node import *

class Problem:
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def __init__(self, initial_state, goal_state=[0, 1, 2, 3, 4, 5, 6, 7, 8]):
        self.initial_node = Node(initial_state, None)
        self.goal_node = Node(goal_state, None)

    def goal_test(self, node_stage):
        '''
        Kiểm tra xem đã đạt trạng thái goal_stage chưa
        Input: node_stage là trạng thái của nút cần so sánh với goal_stage
        Output : true or false
        '''
        if (len(self.goal_node.stage) != len(node_stage)) : return False
        for i in range(0, len(self.goal_node.stage)) :
            if (self.goal_node.stage[i] != node_stage[i]) : return False
        return True
