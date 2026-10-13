# Candidate Verification System

from pyscript import display, document

def name_finder(e):
    document.getElementById('output').innerHTML = ' '
    first_name = document.getElementById('first').value
    last_name = document.getElementById('surname').value
    full_name = first_name + ', ' + last_name
    club_member = ['Adrianna, Allas', 'Katharine, Penas', 'Margaretha, Magsino', 'Zoe, Reyes', 'Alexandra, Bueno', 'Jaena, Ambata']
    student_checker = full_name in club_member

    display_message = (f'Sorry {full_name}, your name is not on the list', f'Congratulations {full_name}! You are now part of the Cosmic Writers Guild.')
    display(display_message[student_checker], target="output")
