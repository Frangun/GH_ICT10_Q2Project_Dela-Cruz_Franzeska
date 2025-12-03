# Working with Dictionaries
from pyscript import display, document, HTML

subjects = ["sci", "math", "eng", "fil", "ss", "ict"] # lists
units = (5, 5, 5, 3, 3, 2) # tuples

def collecting_data(e):
    document.getElementById("div2").innerHTML=""

    #name
    first_name = document.getElementById("fname").value
    last_name = document.getElementById("lname").value

    names = first_name + " " + last_name

    # SUBJECT VALUES
    science = document.getElementById('sci').value
    math = document.getElementById('math').value
    english = document.getElementById('eng').value
    filipino = document.getElementById('fil').value
    social_studies = document.getElementById('ss').value
    ict_subj = document.getElementById('ict').value

    # FORMULA
    abg = round((float(science) + float(math) + float(english) + float(filipino) + float(social_studies) + float(ict_subj)) / 6, 2) # i want an abg and avg


    # DISPLAY RESULT
    message = f"""👤GWA:
        
        \tName   : "{names}\"
        
        
        
        \tScience: {science}
        \tMath: {math}
        \tEnglish: {english}
        \tFilipino: {filipino}
        \tSocial Studies: {social_studies}
        \tICT: {ict_subj}
        
        \tFinal: {abg}

        
        """

    display(message, target="div2")

def acad_clubs(e):
    clubs = {
        "Math Club": {
            "Description": "It procures analytical, mathematical questions and tasks that tests critical thinking and computation skills of qualified students",
            "Meeting Time": "Mondays, 2:30-4:00 PM",
            "Location": "Room 711",
            "Club Moderator": "Mrs. Aguilar",
            "Number of Members": 20
        },
        "Science Club": {
            "Description": "With practical experiments, organized workbooks, and sufficient equipment, Science Club is able to let students see the world's scientific origins and explanations",
            "Meeting Time": "Tuesdays, 3:00-5:30 PM",
            "Location": "Science Laboratory",
            "Club Moderator": "Mr. Castana",
            "Number of Members": 27
        },
        "Social Studies Club": {
            "Description": "Philosophy, Geography, History---all in one! It prepares particular students with hands-on activities and collects controversial opinions",
            "Meeting Time": "Wednesdays, 2:30–4:00 PM",
            "Location": "Room 714",
            "Club Moderator": "Mr. Danes",
            "Number of Members": 25
        }
    } # specifying dictionaries

    club_selected = document.getElementById("acad-select").value

    info = clubs[club_selected]
    output = f"""
        <h2><em>{club_selected}</em></h2>
        <p><b>Description:</b> {info['Description']}</p>
        <p><b>Meeting Time:</b> {info['Meeting Time']}</p>
        <p><b>Location:</b> {info['Location']}</p>
        <p><b>Club Moderator:</b> {info['Club Moderator']}</p>
        <p><b>Number of Members:</b> {info['Number of Members']}</p>
    """

    display(HTML(output), target="output", append=False)

