"""
Bite 109. Workout dictionary lookups

    In this Bite you learn how to lookup values from a dictionary or in Python: dict.

    You are presented with WORKOUT_SCHEDULE dict (constant) with keys = days and values = workouts (or rest up).
    Complete get_workout_motd that receives a day string, title case it so the function can receive case insensitive
    days, look it up in the dict and do two things:
        If the day (key) is not in the dictionary, return INVALID_DAY, we don't want this function to continue.
        If the key is in the dictionary, return CHILL_OUT or TRAIN depending if it's a REST day or not. The latter
        you will need to string-interpolate using format.

    Also check out the docstring and tests. Have fun and keep calm and code in Python!
    Update 25th of Nov 2019: previously this Bite required re-raising the KeyError, but as that's already the default
    behavior of a missing key in a dict, we changed the requirements to return a value instead.
"""

WORKOUT_SCHEDULE = {'Friday': 'Shoulders',
                    'Monday': 'Chest+biceps',
                    'Saturday': 'Rest',
                    'Sunday': 'Rest',
                    'Thursday': 'Legs',
                    'Tuesday': 'Back+triceps',
                    'Wednesday': 'Core'}
REST, CHILL_OUT, TRAIN = 'Rest', 'Chill out!', 'Go train {}'
INVALID_DAY = 'Not a valid day'


def get_workout_motd(day):
    """First title case the passed in day argument
       (so monday or MONDAY both result in Monday).

       If day is not in WORKOUT_SCHEDULE, return INVALID_DAY

       If day is in WORKOUT_SCHEDULE retrieve the value (workout)
       and return the following:
       - weekday, return TRAIN with the workout value interpolated
       - weekend day (value 'Rest'), return CHILL_OUT

       Examples:
       - if day is Monday -> function returns 'Go train Chest+biceps'
       - if day is Thursday -> function returns 'Go train Legs'
       - if day is Saturday -> function returns 'Chill out!'
       - if day is nonsense -> function returns 'Not a valid day'

       Trivia: /etc/motd is a file on Unix-like systems that contains
       a 'message of the day'
    """
    day_of_week = day.title()
    if day_of_week not in WORKOUT_SCHEDULE:
        return INVALID_DAY

    if day_of_week == 'Saturday' or day_of_week == 'Sunday':
        return CHILL_OUT

    for key, value in WORKOUT_SCHEDULE.items():
        if day_of_week == key:
            if value == 'Rest':
                return REST
            else:
                return TRAIN.format(value)


print(get_workout_motd("Monday"))
