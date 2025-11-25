from themes import list_of_duties

"""
Finished product: write a program that would display on the screen all the duties in this apprenticeship. 
"""
def test_full_list_is_displayed():
    number_of_duties = 13
    assert len(list_of_duties) == number_of_duties

def test_list_items_are_duties():
    monitor = 0
    for duty in list_of_duties:
        monitor += duty.rfind("Duty")
    assert monitor == 0

def test_all_duties_are_listed():
    duty_number = 1
    monitor = 0
    for duty in list_of_duties:
        duty_number_index = duty[5:7]
        if str(duty_number) not in duty_number_index:
            monitor += 1 
        duty_number += 1
    assert monitor == 0

def test_html_file_is_created():
    try:
        open("duties.html")
    except FileNotFoundError:
        assert False

# TODO: test html file displays duties