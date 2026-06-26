import os
import re

LESSON_DIR = os.path.dirname(__file__)
TARGET_CODE = os.path.join(LESSON_DIR, "incomplete_main.py")
user_code = open(TARGET_CODE, "r").read()

def test_minion_stats(capsys):
    exec(user_code)
    output = capsys.readouterr().out
    expected = ("Minion Health: 50.0\n" +
                "Minion Armor: 25.0\n" +
                "Minion Damage: 60.0\n")
    assert output == expected

def test_used_list_comprehension():
    # Solution where the user sets the list comprehension to a variable before returning
    expected_solution_a = (r"def\s*create_minion\s*\([a-zA-Z_][a-zA-Z_\d]*\)\s*:[\s\S]*" + 
                           r"[a-zA-Z_][a-zA-Z_\d]*\s*\=\s*\[[\s\S]*for\s+" + 
                           r"[a-zA-Z_][a-zA-Z_\d]*\s+in\s+[a-zA-Z_][a-zA-Z_\d]*\][\s\S]*" + 
                           r"return\s+[a-zA-Z_][a-zA-Z_\d]*")
    # Solution where the user immediately returns the result of the list comprehension
    expected_solution_b = (r"def\s*create_minion\s*\([a-zA-Z_][a-zA-Z_\d]*\)\s*:[\s\S]*" + 
                           r"return\s*\[[\s\S]*for\s+[a-zA-Z_][a-zA-Z_\d]*\s+" + 
                           r"in\s+[a-zA-Z_][a-zA-Z_\d]*\]")
    
    assert re.search(expected_solution_a, user_code) or re.search(expected_solution_b, user_code)
    