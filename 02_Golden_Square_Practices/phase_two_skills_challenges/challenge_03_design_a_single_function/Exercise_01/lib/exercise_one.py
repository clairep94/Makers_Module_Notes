#Step 1: User Story:
    # As a user
    # So that I can manage my time
    # I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

#Note: due to the way I wrote these tests (ie. testing string length already calculated, vs inputing a string), I had to write an
# additional function to encapsulate the original brief (text as string as param; time estimate as string as output.)

import math

def text_reading_time_estimate(text: str) -> str:
    '''
    Params: str: text to read
    Returns: str: amount of time needed to read a text in hours and minutes. Assume to read at 200 words per min.
        - Round the result to the nearest minute: "It will take __ minute(s) to read this."
        - If reading time is less than 1 min: "It will take less than 1 minute to read this."
        - If reading time is more than 60 min: "It will take __hour(s) and __ minute(s) to read this."
    '''
    length_text = len(text)
    return reading_time(length_text)

def reading_time(text_length: int) -> str: #change to -> text:str after.
    '''
    Params: length of a text as an integer
    Returns: str: amount of time needed to read a text in hours and minutes. Assume to read at 200 words per min.
        - Round the result to the nearest minute: "It will take __ minute(s) to read this."
        - If reading time is less than 1 min: "It will take less than 1 minute to read this."
        - If reading time is more than 60 min: "It will take __hour(s) and __ minute(s) to read this."
    '''
    
    # length_text = len(text)
    minutes_float = text_length/200

    if minutes_float < 0.5:
        return "It will take less than 1 minute to read this."
    elif 0.5 <= minutes_float < 50.5:
        minutes = round(minutes_float)
        return f"It will take {minutes} minute(s) to read this."
    elif 50.5 <= minutes_float:
        hours_float = minutes_float/60
        hours = math.floor(hours_float) #integer of hours
        remaining_mins_float = (hours_float-hours)*60
        minutes = round(remaining_mins_float)
        return f"It will take {hours} hour(s) and {minutes} minute(s) to read this."
