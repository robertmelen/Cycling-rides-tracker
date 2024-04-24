import sqlite3


conn = sqlite3.connect('cycling.db')
c = conn.cursor()


def add_cyclist_to_schema(**kwargs):
    '''
    Adds a cyclist to the database if not already existing.
        Paramaters:
        a(str): Cyclist Name
        b(str): Cyclist DoB
        c(int): Cyclist age
        d(str): Cyclist skill_level
    '''

   
    c.execute("SELECT id FROM cyclist WHERE name=? AND dob=? AND age=?",
              (kwargs.get('name'), kwargs.get('dob'), kwargs.get('age')))
    existing_cyclist = c.fetchone()

    if existing_cyclist:
        print("Cyclist already exists.")
        return  
    else:
        try:
            c.execute("INSERT INTO cyclist (name, dob, age, skill_level) VALUES (?, ?, ?, ?)",
                      (kwargs.get('name'), kwargs.get('dob'), kwargs.get('age'), kwargs.get('skill_level')))
            conn.commit()
            print("Cyclist added successfully.")
        except Exception as e:
            print("Error:", e)



def delete_ride_by_id(ride_id):
    '''Utility to delete a ride by table ID'''
    c.execute("DELETE FROM ride WHERE id=?", (ride_id,))
    conn.commit()
    print("Ride deleted successfully.")



def add_cyclist_to_ride(ride_id, cyclists_names):
    '''Iterates through cyclists and selects them from cyclist table, fetching their ID
    and inserting into ride_cyclist table'''
    for name in cyclists_names:
        c.execute("SELECT id FROM cyclist WHERE name=?", (name,))
        row = c.fetchone()
        if row:
            cyclist_id = row[0]
            c.execute("INSERT INTO ride_cyclist (ride_id, cyclist_id) VALUES (?, ?)", (ride_id, cyclist_id))
            conn.commit()
        else:
            print(f"No cyclist found with the name '{name}'")


def add_ride_with_cyclists(ride, cyclists):
    c.execute("INSERT INTO ride (name, date, length, location, start, finish, start_time) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (ride.name, ride.date, ride.length, ride.location, ride.start, ride.finish, ride.start_time))
    ride_id = c.lastrowid
    add_cyclist_to_ride(ride_id, cyclists)



def get_rides_for_cyclist(cyclist_name):
    '''Get all rides a cyclist has been on'''
    c.execute("""SELECT ride.name 
                FROM ride 
                JOIN ride_cyclist ON ride.id = ride_cyclist.ride_id 
                JOIN cyclist ON ride_cyclist.cyclist_id = cyclist.id 
                WHERE cyclist.name=?
                """, (cyclist_name,))
    rides = c.fetchall()
    if rides:
        print(f"Rides for {cyclist_name}:")
        for ride in rides:
            print(ride[0])
    else:
        print(f"No rides found for {cyclist_name}")

