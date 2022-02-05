
class Task(object):
    def __init__(self, event, description, duration, weekly_recurrance, preferance_list, isFlexible, location, time_zone, start_time = None, end_time = None): 
        # string
        self.name = event 
        self.description = description
        # hour:minutes:secon
        self.duration = duration
        self.start_time = start_time
        self.end_time = end_time
        # Mo,TU, WE, TH, FR
        self.byDay = weekly_recurrance
        # list of day/time prefances...will figure out format...
        self.preferance_list = preferance_list
        # binary true false or 0/1
        self.isFlexible = isFlexible
        # string -> look at google to see what we need / what format we envision
        self.location = location
        self.time_zone = time_zone


class Veronica(object): 
    def __init__(self, max_block_length = 2, max_adj_block = 2): 
        self.max_block_length = max_block_length
        self.max_adj_block = max_adj_block
        self.task_list = []
        self.flexible_task_list = []
        self.inflexible_task_list = []
        # will need binary variable for seeing whether they want to update 
        #will add as needed. 

    def add_task(self, event, description, duration, weekly_recurrance, preferance_list, isFlexible, location, time_zone, start_time = None, end_time = None): 
        new_task = Task(event, description, duration, weekly_recurrance, preferance_list, isFlexible, location, time_zone, start_time, end_time)
        self.task_list.append(new_task)
        if isFlexible: 
            self.flexible_task_list.append(new_task)
        else: 
            self.inflexible_task_list.append(new_task)

