from themes import list_of_duties
"""
Finished product: write a program that would display on the screen all the duties in this apprenticeship. 
"""

# check that the full list is displayed
def test_full_list_is_displayed():
    number_of_duties = 13
    assert len(list_of_duties) == number_of_duties

# check all items are duties
def test_list_items_are_duties():
    monitor = 0
    for duty in list_of_duties:
        monitor += duty.rfind("Duty")
    assert monitor == 0

# check all duties are there
def test_all_duties_are_listed():
    number = 1
    monitor = 0
    for duty in list_of_duties:
        if str(number) not in duty[5:7]:
            monitor += 1 
        number += 1
        continue
    assert monitor == 0