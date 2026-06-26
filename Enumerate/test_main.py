import os
import re

from incomplete_main import show_party

LESSON_DIR = os.path.dirname(__file__)
TARGET_CODE = os.path.join(LESSON_DIR, "incomplete_main.py")
user_code = open(TARGET_CODE, "r").read()

def test_show_party(capsys):
    exec(user_code)
    output = capsys.readouterr().out
    expected = ("Member 0: Bob\n" + 
                "Member 1: Jill\n" + 
                "Member 2: Dan\n")
    assert output == expected

def test_new_data(capsys):
    bills_party = ["Bill", "Josh", "Jane", "Mary"]
    show_party(bills_party)
    output = capsys.readouterr().out
    expected = ("Member 0: Bill\n" + 
                "Member 1: Josh\n" + 
                "Member 2: Jane\n" + 
                "Member 3: Mary\n")
    assert output == expected
    
def test_used_enumerate():
    # matches (almost) all valid variation of an enumerate statement
    # and also a lot of invalid variations that don't really matter
    assert re.search(r"for\s*[a-zA-Z_][a-zA-Z_\d]*\s*,\s*" + 
                     r"[a-zA-Z_][a-zA-Z_\d]*\s*in\s*enumerate\s*" + 
                     r"\(\s*[a-zA-Z_][a-zA-Z_\d]*\s*\)\s*:", user_code)
    