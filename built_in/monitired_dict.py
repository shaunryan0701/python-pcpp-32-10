from datetime import datetime

class MonitoredDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log = list()
        self.log_timestamp('Monitored Dict created')

    def __getitem__(self, __key):
        self.log_timestamp(f'Value for [{__key}] retrieved')
        return super().__getitem__(__key)
    
    def __setitem__(self, __key,  __value):
        self.log_timestamp(f'Value for [{__key}] set to {__value}')
        return super().__setitem__(__key, __value)

    def log_timestamp(self, message):
        timestamp_string = datetime.now().strftime("%Y-%m-%d (%H:%M:%S.%f)")
        self.log.append(f'{timestamp_string} {message}')

_dict = MonitoredDict()
_dict[10] = 'Bollox'
_dict[11] = 'Still Bollox'

var = _dict[10]
print('Whole dictionary:', _dict)
print('Our log book:\n')
print('\n'.join(_dict.log))