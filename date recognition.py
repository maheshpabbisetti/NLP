import re

class DateRecognizerFSM:
    def __init__(self):
        self.current_state = 'start'
    
    def recognize_date(self, text):
        day_regex = r'(0?[1-9]|[12][0-9]|3[01])'
        month_regex = r'(0?[1-9]|1[012])'
        year_regex = r'(19\d{2}|20\d{2})'
        
        date_regex = rf'{day_regex}/{month_regex}/{year_regex}'
        
        date_partial_regex = rf'({day_regex}/{month_regex}|{month_regex}/{year_regex})'
                
        full_regex = re.compile(f'({date_regex}|{date_partial_regex})')
        
        matches = full_regex.finditer(text)
        
        for match in matches:
            print("Date found:", match.group(0))
        
fsm = DateRecognizerFSM()
text = "I have an appointment on 25/02/2024, and another on 15/07/2024"
fsm.recognize_date(text)
