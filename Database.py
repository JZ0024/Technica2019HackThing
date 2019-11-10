#!/usr/bin/env python3
# use Google Cloud firebase

# prior to working this code, set up dev environment and initialize SDK:
# https://firebase.google.com/docs/admin/setup#initialize_the_sdk
# and generate the private key and save the JSON file
# For this specific script, use the .json file in the git and change the directory to where you stored it
from Tools.scripts import google

# initialize on my own server
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

privateKeyPATH = 'C:\\Users\\joysx\\Documents\\Technica2019/technica2019-firebase-adminsdk-vwttx-a9a3002e60.json'

# use a service account => need to figure out how to initialize using GCP
cred = credentials.Certificate(privateKeyPATH)
firebase_admin.initialize_app(cred)

db = firestore.client()

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


class SpaceJacked(object):
    def __init__(self, identifier, name, ownership, location):
        self.identifier = identifier
        self.name = name
        self.ownership = ownership
        self.location = location

    @staticmethod
    def from_dict(source):
        # code snippet from
        # https://github.com/GoogleCloudPlatform/python-docs-samples/blob/70c3595237e390628d377df9e87402e01af15066/
        # firestore/cloud-client/snippets.py#L103-L154

        # [START_EXCLUDE]
        data = SpaceJacked(source[u'identifier'], source[u'name'], source[u'ownership'], source[u'location'])

        return data
        # [END_EXCLUDE]

    def to_dict(self):
        # [START_EXCLUDE]
        data = {
            u'identifier': self.identifier,
            u'name': self.name,
            u'ownership': self.ownership,
            u'location': self.location
        }
        return data

    def __repr__(self):
        return (
            u'SpaceJacked(identifier={}, name={}, ownership={}, location={})'.format(
                self.identifier, self.name, self.ownership, self.location))


# add in the objects
satellite1 = SpaceJacked(identifier=u'11102019', name=u'satCOM1', ownership=u'SSL', location=u'collegePark')
satellite2 = SpaceJacked(identifier=u'06031998', name=u'satCOM2', ownership=u'CHO', location=u'Seoul')

satellite_ref = db.collection(u'Satellites')
satellite_ref.document('satellite1').set(satellite1.to_dict())
satellite_ref.document('satellite2').set(satellite2.to_dict())
# db.collection(u'Satellites').document('satellite1').set(satellite1.to_dict())
# db.collection(u'Satellites').document('satellite2').set(satellite2.to_dict())

'''
# for printing out a single object
doc_ref = db.collection(u'Satellites').document('satellite1')
doc = doc_ref.get()
satellite = SpaceJacked.from_dict(doc.to_dict())
print(satellite)
'''
# for printing out multiple objects
satellite_ref = db.collection(u'Satellites').stream()
for doc in satellite_ref:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))
