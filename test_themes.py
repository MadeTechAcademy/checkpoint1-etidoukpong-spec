from themes import list_of_duties, Duty
from requests_html import HTML
import re

"""
Finished product: write a program that would display on the screen all the duties in this apprenticeship. 
"""

# TODO: Use RE groups and Match to check that the number group for each duty contans a unique number.

def test_correct_number_of_duties_are_listed():
    number_of_duties = 13
    assert len(list_of_duties) == number_of_duties

def test_list_items_are_duties():
    for duty in list_of_duties:
        assert isinstance(duty, Duty)

def test_unique_duties_are_listed():
    hashes = []
    for duty in list_of_duties:
        hashes.append(duty.__hash__())
    assert len(list_of_duties) == len(set(hashes))

def test_html_file_is_created():
    try:
        open("duties.html")
    except FileNotFoundError:
        assert False

def test_html_file_displays_duties():
    with open("duties.html") as page:
        source = page.read()
        html = HTML(html=source)
    for duty in list_of_duties:
        assert duty.text in html.text