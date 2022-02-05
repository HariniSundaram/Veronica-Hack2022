#hours:minute:seconds
# HOURS ARE IN 24 HOURS FORMAT
def to_minute(time): 
    # print(time)
    time_list = time.split(':')
    new_num = int(time_list[0]) * 60 + int(time_list[1])
    return new_num

def calc_priority_index(byDay, duration, isFlexible): 
    return len(byDay) * duration * int(isFlexible)
class Task(object):
    def __init__(self, event, description, duration, weekly_recurrance, 
        recurrance_per_day, preferance_list, isFlexible, location, time_zone, 
        start_time = None, end_time = None): 
        # string
        self.name = event 
        self.description = description
        # hour:minutes:second -> minute sum
        self.duration = to_minute(str(duration))
        self.start_time = start_time
        self.end_time = end_time
        # [Mo,TU, WE, TH, FR]
        self.byDay = weekly_recurrance

        self.recurrance_per_day = recurrance_per_day
        # list of time prefances...will figure out format...
        self.preferance_list = preferance_list
        # binary true false or 0/1
        self.isFlexible = isFlexible
        # string -> look at google to see what we need / what format we envision
        self.location = location
        self.time_zone = time_zone

        self.priority_index = calc_priority_index(self.byDay, self.duration, self.isFlexible)

        #default settings for interleave rules
    
    def __repr__(self):
        # need to add more and formalize
        new_str = str(self.name) + ', priority_index ' + str(self.priority_index)
        return new_str


class Veronica(object): 
    def __init__(self, day_start, day_end, max_block_length = 2, max_adj_block = 2): 
        self.day_start = day_start
        self.day_end = day_end
        self.max_block_length = max_block_length
        self.max_adj_block = max_adj_block
        self.task_list = []
        self.flexible_task_list = []
        self.inflexible_task_list = []
        # will need binary variable for seeing whether they want to update 
        #will add as needed. 

    def add_task(self, event, description, duration, weekly_recurrance, recurrance_per_day, preferance_list, isFlexible, location, time_zone, start_time = None, end_time = None): 
        new_task = Task(event, description, duration, weekly_recurrance, recurrance_per_day, preferance_list, isFlexible, location, time_zone, start_time, end_time)
        self.task_list.append(new_task)
        if isFlexible: 
            self.flexible_task_list.append(new_task)
        else: 
            self.inflexible_task_list.append(new_task)
        if recurrance_per_day > 1: 
            return self.add_task (event, description, duration, weekly_recurrance, recurrance_per_day - 1, preferance_list, isFlexible, location, time_zone, start_time, end_time = None)
        

    def get_task(self, spec = None): 
        if spec == "flex": return self.flexible_task_list
        if spec == "inflex" : return self.inflexible_task_list
        else: return self.task_list

    def sort_tasks(self): 
        new_sorted = sorted(self.task_list, key = lambda x: x.priority_index)
        return new_sorted

    def get_len_tasks(self, spec = None): 
        if spec == "flex": return len(self.flexible_task_list)
        if spec == "inflex" : return len(self.inflexible_task_list)
        else: return len(self.task_list)