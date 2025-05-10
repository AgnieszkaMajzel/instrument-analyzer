from datetime import datetime

class InstrumentData:
    def __init__(self, name):
        self.name = name
        self.data = []

        self.sum = 0.0
        self.count = 0

# only for Instrument2 - data from November 2014
        self.nov2014_sum = 0.0
        self.nov2014_count = 0

# only for Instrument3 - min value
        self.min_value = None
        
    def add_record(self, date_str, value_str):
        date = datetime.strptime(date_str, '%d-%b-%Y')
        value = float(value_str)
        
# check if this is a business day
        if date.weekday() >= 5:
            return
        
        self.data.append((date, value))
        self.sum += value
        self.count += 1
        
# only for Instrument2 - data from November 2014
        if self.name == "INSTRUMENT2" and date.month == 11 and date.year == 2014:
            self.nov2014_sum += value
            self.nov2014_count += 1

# only for Instrument3 - min value
        if self.name == "INSTRUMENT3":
            if self.min_value is None or value < self.min_value:
                self.min_value = value
                
    def get_results(self):
        if self.name == "INSTRUMENT1":
            return self.sum / self.count if self.count > 0 else 0 #mean for INSTRUMENT1
        elif self.name == "INSTRUMENT2":
            return self.nov2014_sum / self.nov2014_count if self.nov2014_count > 0 else 0 #mean for INSTRUMENT2
        elif self.name == "INSTRUMENT3":
            return self.min_value if self.min_value is not None else 0 #min for INSTRUMENT3
        else:
            sorted_values = sorted(self.data, key=lambda x: x[1], reverse=True)
            last_10 = sorted_values[:10]
            return sum(value for date, value in last_10) #sum of the newest 10 values (in terms of date)
        #although average of the newest 10 values would be more appropriate





