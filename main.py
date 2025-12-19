from pyscript import display, document

# Define club information using dictionaries
club_info = {
            "creatives": {
                "name": "Creatives Club",
                "description": "A club for artsy and wild kids that refuse limitations",
                "meeting_time": "Every Wednesday 3:30-5:00 PM",
                "location": "Room 405",
                "advisor": "Mrs. Lopez",
                "members": 20,
                "category": "Arts"
            },
            "theater": {
                "name": "Theater Club",
                "description": "For students interested in theater, and belting into song e every 6 minutes.",
                "meeting_time": "Every Monday and Thursday 4:00-6:00 PM",
                "location": "Oakwood Hall",
                "advisor": "Ms. Sorbet",
                "members": 22,
                "category": "Arts"
            },
            "writing": {
                "name": "Writers Club",
                "description": "Write a poem, sonet, and story to your hearts content.",
                "meeting_time": "Every Tuesday 3:45-5:30 PM",
                "location": "Room 203",
                "advisor": "Mr. Shakespear",
                "members": 18,
                "category": "Academic"
            },
            "debate": {
                "name": "Debate Club",
                "description": "Learn how to argue.",
                "meeting_time": "Every Friday 3:30-5:00 PM",
                "location": "Room 507",
                "advisor": "Mr. Malachi",
                "members": 26,
                "category": "Academic"
            },
            "baking": {
                "name": "Baking Club",
                "description": "Explore various recipes for your very sweet tooth.",
                "meeting_time": "Every Wednesday 3:45-5:15 PM",
                "location": "Kitchen Lab",
                "advisor": "Ms. Aguinaldo",
                "members": 15,
                "category": "Culinary"
            },
            "": {
                "name": "",
                "description": "",
                "meeting_time": "",
                "location": "",
                "advisor": "",
                "members": "",
                "category": ""
            }
        }
        
def show_club_info(e):
    document.getElementById('club-info').innerHTML = " "
    selected_club = document.getElementById("club-select").value
    info = club_info.get(selected_club, club_info[""])
            
    output = f"""
            {info['name']}
            Description:{info['description']}
            Meeting Time: {info['meeting_time']}
            Location: {info['location']}
            Advisor: {info['advisor']}
            Number of Members: {info['members']}
            Category: {info['category']}
            """
    display(output, target="club-info")