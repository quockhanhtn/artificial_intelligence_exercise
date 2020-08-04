from .Problem import *
import queue
import sys

def breadth_first_search(_problem) :
    '''
    Tìm kiếm theo tìm rộng
    Input: problem
    Output : string ('failure', or list actions seperated by '-' to slove problen)
    '''
    _node = _problem.initial_node

    if (_problem.goal_test(_node.stage)) : return _node.get_solution()
    frontier = queue.Queue()
    frontier.put(_node)
    explored = []

    while (not frontier.empty()) :
        _node = frontier.get()
        explored.append(_node.stage)

        for child in _node.get_child_node():
            if ((child.stage not in explored) and (child not in list(frontier.queue))) :
                if (_problem.goal_test(child.stage)) : return child.get_solution()
                frontier.put(child)

    return 'failure'

def depth_first_search(_problem) :
    '''
    Tìm kiếm theo tìm sâu
    Input: problem
    Output : string ('failure', or list actions seperated by '-' to slove problen)
    '''
    _node = _problem.initial_node

    if (_problem.goal_test(_node.stage)) : return _node.get_solution()
    frontier = queue.LifoQueue()
    frontier.put(_node)
    explored = []

    while (not frontier.empty()) :
        _node = frontier.get()
        explored.append(_node.stage)

        for child in _node.get_child_node():
            if ((child.stage not in explored) and (child not in list(frontier.queue))) :
                if (_problem.goal_test(child.stage)) : return child.get_solution()
                frontier.put(child)

    return 'failure'

def depth_limited_search(_problem, limit):
    return recursive_depth_limited_search(_problem.initial_node, _problem, limit)

def recursive_depth_limited_search(_node, _problem, limit) :
    if (_problem.goal_test(_node.stage)) : return _node.get_solution()
    elif (limit == 0) : return 'cutoff'
    else :
        cutoff_occurred = False
        for child in _node.get_child_node():
            result = recursive_depth_limited_search(child, _problem, limit - 1)
            if (result == 'cutoff') :  
                cutoff_occurred = True
            elif (result != 'failure') : 
                return result
        if (cutoff_occurred == True): 
            return 'cutoff'
        else : 
            return 'failure'

def iterative_deepening_search(_problem) :
    '''
    iterative deepening search one thread
    Input: problem
    Output : string ('failure', or list actions seperated by '-' to slove problen)
    '''
    for depth in range(0, sys.maxsize):
        result = depth_limited_search(_problem, depth)
        if (result != 'cutoff') : return result

import concurrent.futures

def iterative_deepening_search_multi_thread(_problem):
    '''
    iterative deepening search eight thread
    Input: problem
    Output : string ('failure', or list actions seperated by '-' to slove problen)
    '''
    result = ''
    for depth in range(0, sys.maxsize, 8):
        
        # Tham khảo code của Ramarao Amara để chạy đa luồnng 
        # link https://stackoverflow.com/questions/6893968/how-to-get-the-return-value-from-a-thread-in-python
        with concurrent.futures.ThreadPoolExecutor() as executor1:
            future = executor1.submit(depth_limited_search, _problem, depth)
            result = future.result()
            if (result != 'cutoff') : return result

        with concurrent.futures.ThreadPoolExecutor() as executor2:
            future = executor2.submit(depth_limited_search, _problem, depth + 1)
            result = future.result()
            if (result != 'cutoff') : return result

        with concurrent.futures.ThreadPoolExecutor() as executor3:
            future = executor3.submit(depth_limited_search, _problem, depth + 2)
            result = future.result()
            if (result != 'cutoff') : return result

        with concurrent.futures.ThreadPoolExecutor() as executor4:
            future = executor4.submit(depth_limited_search, _problem, depth + 3)
            result = future.result()
            if (result != 'cutoff') : return result

        with concurrent.futures.ThreadPoolExecutor() as executor5:
            future = executor5.submit(depth_limited_search, _problem, depth + 4)
            result = future.result()
            if (result != 'cutoff') : return result

        with concurrent.futures.ThreadPoolExecutor() as executor6:
            future = executor6.submit(depth_limited_search, _problem, depth + 5)
            result = future.result()
            if (result != 'cutoff') : return result

        with concurrent.futures.ThreadPoolExecutor() as executor7:
            future = executor7.submit(depth_limited_search, _problem, depth + 6)
            result = future.result()
            if (result != 'cutoff') : return result

        with concurrent.futures.ThreadPoolExecutor() as executor8:
            future = executor8.submit(depth_limited_search, _problem, depth + 7)
            result = future.result()
            if (result != 'cutoff') : return result

