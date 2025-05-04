meetups = []

def create_meetup(name, date, location): 
    meetup = {
    'name' : name, 
    'date' : date, 
    'location' : location, 
    'attendees' : [] #Stores a list of dictionaries with RSVP info
    }


    meetups.append(meetup)
    print(f"Meetup '{name}' created for {date} at {location}.\n")

def rsvp(meetup_name):
    for meetup in meetups:
        if meetup['name'].lower() == meetup_name.lower():
            print(f"\nRSVP for: {meetup_name}")
            name = input("What is your name? ")
            availability = input("Are you available on this date? (yes/no): ")
            reason = input("Why do you want to attend? ")

            # Check if this person already RSVP'd
            for attendee in meetup['attendees']:
                if attendee['name'].lower() == name.lower():
                    print(f"\n{name} has already RSVP'd for this meetup.\n")
                    return

            # Add RSVP data
            attendee_info = {
                'name': name,
                'available': availability.lower() == 'yes',
                'reason': reason
            }
            meetup['attendees'].append(attendee_info)
            print(f"\nThank you {name}, your RSVP for '{meetup_name}' has been recorded!\n")
            return

    print(f"\nNo meetup found with the name '{meetup_name}'.\n")

# Example usage
create_meetup("AI Study Group", "2025-05-10", "Library Room B")
rsvp("AI Study Group")