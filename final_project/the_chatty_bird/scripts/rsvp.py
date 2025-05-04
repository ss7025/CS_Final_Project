meetups = []

def create_meetup(name, date, location): 
    meetup = {
    'name' : name, 
    'date' : date, 
    'location' : location, 
    'attendees' : [] #Stores a list of dictionaries with RSVP info
    }