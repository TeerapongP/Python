import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('pythonproject-60334-firebase-adminsdk-uza3g-25b7046407.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://pythonproject-60334-default-rtdb.firebaseio.com/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('')

hopper_ref = ref.child('Users/title')
hopper_ref.delete()
print(ref.get())
