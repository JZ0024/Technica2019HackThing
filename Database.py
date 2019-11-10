#!/usr/bin/env python3
# use Google Cloud firebase

# prior to working this code, set up dev environment and initialize SDK:
# https://firebase.google.com/docs/admin/setup#initialize_the_sdk
# and generate the private key and save the JSON file
# For this specific script, use the .json file in the git and change the directory to where you stored it


def collect_data(self, dp, dict_apriltag, dict_cmdln):
    # initialize variable
    for key in dict_apriltag.keys():
        name = (key[0] + key[1])
        tup1 = dict_apriltag[key]

        if dict_cmdln:
            tup2 = dict_cmdln[key]
            data = {u'location': tup1[0], u'name': tup2[0], u'owner': tup2[1]}
            dp.collection(u'space_objects').document(name).set(data)
        else:
            dp.collection(u'space_objects').document(name).update({u'location': tup1[0]})


'''
# add in the objects manually
satellite1 = SpaceJacked(identifier=u'11102019', name=u'satCOM1', ownership=u'SSL', location=u'collegePark')
satellite2 = SpaceJacked(identifier=u'06031998', name=u'satCOM2', ownership=u'CHO', location=u'Seoul')

satellite_ref = db.collection(u'Satellites')
satellite_ref.document('satellite1').set(satellite1.to_dict())
satellite_ref.document('satellite2').set(satellite2.to_dict())
# db.collection(u'Satellites').document('satellite1').set(satellite1.to_dict())
# db.collection(u'Satellites').document('satellite2').set(satellite2.to_dict())


# for printing out a single object
doc_ref = db.collection(u'Satellites').document('satellite1')
doc = doc_ref.get()
satellite = SpaceJacked.from_dict(doc.to_dict())
print(satellite)

# for printing out multiple objects
satellite_ref = db.collection(u'Satellites').stream()
for doc in satellite_ref:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))
'''
