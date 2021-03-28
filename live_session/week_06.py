"""Do this now: Hey Siri, will it rain?
Given a list: [10, 0, 20, 50, 90]
If any of the chances are 50% or more then the answer is True.
"""
PRECIPITATION_CHANCES = [10, 0, 20, 50, 90]
MINIMUM_VALUE = 50  # 50% or higher == True


def main():
    if is_going_to_rain(PRECIPITATION_CHANCES):
        print("Yes, rainy day")
    else:
        print("Nah, all good")


def is_going_to_rain(rain_chances):
    # for rain_chance in rain_chances:
    #     if rain_chance >= MINIMUM_VALUE:
    #         return True
    #     return False
    will_rain = [rain_chance for rain_chance in rain_chances if rain_chance >= MINIMUM_VALUE]
    return will_rain


main()
