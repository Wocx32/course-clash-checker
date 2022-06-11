import pickle

try:
    with open('course-data.pickle', 'rb') as file:
        data = pickle.load(file)
except:
    from database import create_database

    print('Creating database please wait... (This may take a minute or two)')

    create_database('2022FA')

    print('Database created!')
    
    with open('course-data.pickle', 'rb') as file:
        data = pickle.load(file)

input_courses = input('Enter courses: ').split(',')
input_courses = [x.strip().upper() for x in input_courses]

courses = []



for i in data:
    if i['name'] in input_courses:
        if i['lab']:
            i['name'] = i['name'] + ' Lab'
            courses.append(i)
            continue
        courses.append(i)


def check_clash(course1, course2):
    course1_days = ''.join(course1['days'])
    course2_days = ''.join(course2['days'])

    if course1_days in course2_days or course2_days in course1_days:
        if course1['start_time'] <= course2['start_time'] <= course1['end_time'] or course1['start_time'] <= course2['end_time'] <= course1['end_time']:
            return True
    return False

detected = []

track_detected = False

for i in courses:
    for j in courses:
        if i['name'] != j['name'] and check_clash(i, j):
            for k in detected:
                if i['name'] in k and j['name'] in k:
                    track_detected = True
                    break
                track_detected = False
            
            if not track_detected:
                detected.append((i['name'], j['name']))
                print(i['name'], 'clashes with', j['name'])
            track_detected = False