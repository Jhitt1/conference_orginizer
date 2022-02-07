import requests
partner_data_unfilt = requests.get('https://ct-mock-tech-assessment.herokuapp.com/').json()
#print(partner_data_unfilt)
for i in partner_data_unfilt['partners']:
    print(i['firstName'], i['lastName'], i['availableDates'], i['email'], i['country'])

new_dict = {}
for i in partner_data_unfilt['partners']:
    new_dict[i['country']] = [x for x in partner_data_unfilt['partners']]
#print(new_dict)


class United_States:['firstName', 'lastName', 'email', 'United_States']
attendees_1 = [i['firstName'], i['lastName'], i['availableDates'], i['email'], i['United_States']]
num_of_participants = 0
united_states_meet = {
    'location': 'United_States',
    'start_date': '2017-06-02',
    'attendee_count': 0,
    }

for i in attendees_1 ['country']:
    if '2017-06-02' in i['availableDates']:
        united_states_meet['attendee_count'] += 1
        united_states_meet['attendees_1'] = [x['email'] for x in attendees_1]
    #print('email')


class Ireland:['firstName', 'lastName', 'email', 'Ireland']
attendees_2 = [i['firstName'], i['lastName'],i['availableDates'], i['email'], i['Ireland']]
num_of_participants = 0
ireland_meet = {
    'location': 'Ireland',
    'start_date': '2017-05-30',
    'attendee_count': 0,
}

for i in attendees_2['Ireland']:
    if '2017-05-30' in i['availableDates']:
        ireland_meet['attendee_count'] += 1
        ireland_meet['attendees_2'] = [x['email'] for x in attendees_2]
    #print('email')


class Spain:['firstName', 'lastName', 'email', 'Spain']
attendees_3 = [i['firstName'], i['lastName'],i['availableDates'], i['email'], i['Spain']]
num_of_participants = 0
spain_meet = {
    'location': 'Spain',
    'start_date': '2017-05-03',
    'attendee_count': 0,
}

for i in attendees_3['Spain']:
    if '2017-05-03' in i['availableDates']:
        spain_meet['attendee_count'] += 1
        spain_meet['attendees_3'] = [x['email'] for x in attendees_3]
        

class Mexico:['firstName', 'lastName', 'email', 'Mexico']
attendees_4 = [i['firstName'], i['lastName'],i['availableDates'], i['email'], i['Mexico']]
num_of_participants = 0
mexico_meet = {
    'location': 'Mexico',
    'start_date': '2017-05-05',
    'attendee_count': 0,
}

for i in attendees_4['Mexico']:
    if '2017-05-05' in i['availableDates']:
        mexico_meet['attendee_count'] += 1
        mexico_meet['attendees_4'] = [x['email'] for x in attendees_4]


class Canada:['firstName', 'lastName', 'email', 'Canada']
attendees_5 = [i['firstName'], i['lastName'],i['availableDates'], i['email'], i['Canada']]
num_of_participants = 0
canada_meet = {
    'location': 'Canada',
    'start_date': '2017-06-24',
    'attendee_count': 0,
}

for i in attendees_5['Canada']:
    if '2017-06-24' in i['availableDates']:
        canada_meet['attendee_count'] += 1
        canada_meet['attendees_5'] = [x['email'] for x in attendees_5]


class Singapore:['firstName', 'lastName', 'email', 'Singapore']
attendees_6 = [i['firstName'], i['lastName'],i['availableDates'], i['email'], i['Singapore']]
num_of_participants = 0
singapore_meet = {
    'location': 'Singapore',
    'start_date': '2017-06-08',
    'attendee_count': 0,
}

for i in attendees_6['Singapore']:
    if '2017-06-08' in i['availableDates']:
        singapore_meet['attendee_count'] += 1
        singapore_meet['attendees_6'] = [x['email'] for x in attendees_6]
        

class Japan:['firstName', 'lastName', 'email', 'Japan']
attendees_7 = [i['firstName'], i['lastName'],i['availableDates'], i['email'], i['Japan']]
num_of_participants = 0
japan_meet = {
    'location': 'Japan',
    'start_date': '2017-06-15',
    'attendee_count': 0,
}

for i in attendees_7['Japan']:
    if '2017-06-15' in i['availableDates']:
        japan_meet['attendee_count'] += 1
        japan_meet['attendees_7'] = [x['email'] for x in attendees_7]


class United_Kingdom:['firstName', 'lastName', 'email', 'United_Kingdom']
attendees_8 = [i['firstName'], i['lastName'],i['availableDates'], i['email'], i['United_Kingdom']]
num_of_participants = 0
united_kingdom_meet = {
    'location': 'United_Kingdom',
    'start_date': '2017-06-05',
    'attendee_count': 0,
}

for i in attendees_8['United_Kingdom']:
    if '2017-06-05' in i['availableDates']:
        united_kingdom_meet['attendee_count'] += 1
        united_kingdom_meet['attendees_8'] = [x['email'] for x in attendees_8]


class France:['firstName', 'lastName', 'email', 'France']
attendees_9 = [i['firstName'], i['lastName'],i['availableDates'], i['email'], i['France']]
num_of_participants = 0
france_meet = {
    'location': 'France',
    'start_date': '2017-06-09',
    'attendee_count': 0,
}

for i in attendees_9['France']:
    if '2017-06-09' in i['availableDates']:
        france_meet['attendee_count'] += 1
        france_meet['attendees_9'] = [x['email'] for x in attendees_9]

    pass

