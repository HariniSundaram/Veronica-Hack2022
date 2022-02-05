
class Task(object):
    def __init__(self, event, summary, duration, frequency, by_day, until, preferance_list, isFlexible, location, start_time = None, end_time = None): 
        # string
        self.name = event 
        self.summary = summary
        
        # time in minutes? Will figure out
        self.duration = duration
        self.start_time = start_time
        self.end_time = end_time
        
        self.frequency = frequency
        self.by_day = weekly_recurrance
        self.until = until
        
        # list of day/time prefances...will figure out format...
        self.preferance_list = preferance_list
        # binary true false or 0/1
        self.isFlexible = isFlexible
        # string -> look at google to see what we need / what format we envision
        self.location = location


class Veronica(object): 
    def __init__(self, max_block_length = 2, max_adj_block = 2): 
        self.max_block_length = max_block_length
        self.max_adj_block = max_adj_block
        self.task_list = []
        # will need binary variable for seeing whether they want to update 
        #will add as needed. 

    def add_task(self, event, summary, duration, frequency, by_day, until, preferance_list, isFlexible, location, start_time, end_time): 
        new_task = Task(event, duration, weekly_recurrance, preferance_list, isFlexible, location)
        self.task_list.append(new_task)

