import matplotlib.pyplot as plt
import numpy

class Functions:
    def swap_list(list, first_index, second_index):
        '''
        Trả về một list mới hoán đổi hai phần tử ở vị trí first_index và second_index trong list
        Input : list, first_index, second_index
        Output: list mới có list[first_index] và list[second_index] đổi chỗ trong list
        '''
        new_list = list.copy()
        temp = new_list[first_index]
        new_list[first_index] = new_list[second_index]
        new_list[second_index] = temp
        return new_list

    # Tham khảo code của James Burke
    # link https://stackoverflow.com/questions/23482748/how-to-create-a-hyperlink-with-a-label-in-tkinter
    def open_web(url):
        '''
        Mở địa chỉ website
        Input : url (địa chỉ trang web)
        Output : none
        '''
        import webbrowser
        webbrowser.open_new(url)
 
    def show_graph(list_act) :
        '''
        hiển thị biểu đồ các bước đi
        input : list_action
        output : show graph
        '''
        x = numpy.arange(1, len(list_act))
        y = []

        action = ['UP', 'RIGHT', 'DOWN', 'LEFT']
        for act in list_act:
            for i in range(0, 4):
                if(act == action[i]) : y.append(i + 1)

        plt.plot(x, y, color = 'red', linewidth = 2)

        plt.xticks(x)
        plt.yticks(y)

        plt.yticks(numpy.arange(1, 5), action)

        plt.xlabel('Step')
        plt.ylabel('Action')
        plt.grid() # vẽ đường kẻ

        plt.show()
