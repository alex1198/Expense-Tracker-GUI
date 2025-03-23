from database import connect_db
from gui import root

connect_db()  # Run the database file to create it.

root.mainloop() # Run the Tkinter loop
