import sqlite3
from objects import *
from functions import *
from schema import *


# HOW TO USE.
# First create a 'ride' by using the Ride object
# Then 'add a cyclist' to the ride by using the Ride obj's, add_cyclist method.
# You will now have a ride and riders going on it
# call add_ride_with_cyclists, passing the ride and ride.cyslist to 'create' the ride in the schema.

#To add a cyclist to database use add_cyclist_to_schema function


add_cyclist_to_schema(name="FooBaR", dob="1982/2/23", age=42, skill_level="advanced" )

ride = Ride("Baglan", "2024/4/29", 20, "Swansea", "House", "House", 8)
ride.add_cyclist("FooBaR")

add_ride_with_cyclists(ride, ride.cyclists)


conn.commit()
conn.close()

