#!/usr/bin/env python3
# use Google Cloud firebase

# prior to working this code, set up dev environment and initialize SDK:
# https://firebase.google.com/docs/admin/setup#initialize_the_sdk
# and generate the private key and save the JSON file
# For this specific script, use the .json file in the git and change the directory to where you stored it

privateKeyPATH = 'C:\\Users\\joysx\\Documents\\Technica2019/technica2019-firebase-adminsdk-ih38o-78386d1fc2.json'

# initialize on my own server
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# use a service account => need to figure out how to initialize using GCP
cred = credentials.Certificate(privateKeyPATH)
firebase_admin.initialize_app(cred)

db=firestore.client()

'''
# from the tutorial.. making references to data collection/documents 
# https://firebase.google.com/docs/firestore/quickstart
doc_ref = db.collection(u'users').document(u'alovelace')
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1815
})

doc_ref = db.collection(u'users').document(u'aturing')
doc_ref.set({
    u'first': u'Alan',
    u'middle': u'Mathison',
    u'last': u'Turing',
    u'born': 1912
})

users_ref = db.collection(u'users')
docs = users_ref.stream()

for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))
'''

