# insert_data.py
if __name__ == '__main__':
    from .models import User, Pilot, Checker, Aircraft, FlightCategory, FlightLog

    # Insert a new user
    user = User.objects.create(
        id=101, 
        email="user@example.com", 
        name="John Doe", 
        is_active=True, 
        is_staff=False, 
        password="yourpassword"  # Make sure to hash the password, e.g., using set_password()
    )

    # You can create a user with a hashed password
    user.set_password('yourpassword')
    user.save()

    # Insert a pilot
    pilot = Pilot.objects.create(pilot_id=user)

    # Insert a checker
    checker = Checker.objects.create(user_id=user)

    # Insert an aircraft
    aircraft = Aircraft.objects.create(type="Type1")

    # Insert a flight category
    category = FlightCategory.objects.create(engine=1, role=3)

    # Insert a flight log
    flight_log = FlightLog.objects.create(
        date="2024-01-01", 
        route="123", 
        remarks="Sample", 
        duration=90, 
        pilot_id=pilot, 
        aircraft_id=aircraft, 
        category_id=category
    )
