from django.shortcuts import render
import pyrebase

config = {
  "apiKey": "AIzaSyDapKpMKn9ngK0aicwldlDY3fjML_tL3N0",
  "authDomain": "smart-scale-e9019.firebaseapp.com",
  "databaseURL": "https://smart-scale-e9019-default-rtdb.firebaseio.com",
  "projectId": "smart-scale-e9019",
  "storageBucket": "smart-scale-e9019.appspot.com",
  "messagingSenderId": "607200793665",
  "appId": "1:607200793665:web:74d9b6ab62e2c497a022c0",
  "measurementId": "G-VWTQT9XR68"
};

firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

def scale(request):
    mass = database.child('Mass').get().val()
    
    return render(request, 'app/index.html', {'mass': mass})