houseDict = {'color' : 'blue',
             'style' : 'colonial',
             'numberOfBedrooms' : 4,
             'garage' : True,
             'burglarAlarm' : False,
             'streetNumber' : 123,
             'streetName' : 'Any Street',
             'city' : 'Anytown',
             'state' : 'CA',
             'price' : 625000}

print houseDict['color']
print houseDict['state']
print houseDict['numberOfBedrooms']

houseDict['price'] = 700000
print houseDict['price']

houseDict['numberOfBathrooms'] = 2.5
print houseDict

print
print
print houseDict.keys()
print houseDict.values()

if 'color' in houseDict:
    print 'Mein Dict enthaelt COLOR'

if 'color2' not in houseDict:
    print 'Mein Dict enthaelt COLOR2 nicht'


statesDict = {'California':38802000,
              'Texas':26956000,
              'Florida':19893000,
              'New York':19746000,
              'Illinois': 12880000,
              'Pennsylvania': 12787000,
              'Ohio':11594000,
              'Georgia': 10097000,
              'North Carolina': 9943964,
              'Michigan':9909000,
              'New Jersey': 8938000}

print
for state in statesDict:
    print state


print
carsList = [
    {'make':'Toyota', 'model':'Prius', 'year': 2006, 'color':'gold', 'doors':4,'leather':False, 'license': 'ABC123', 'mileage': 777777},
    {'make':'Honda', 'model':'Civic', 'year': 2010, 'color':'red', 'doors':2,'leather':False, 'license': 'DEF444', 'mileage': 54321},
    {'make':'Ford', 'model':'Fusion', 'year': 2012, 'color':'blue', 'doors':4,'leather':True, 'license': 'GHI999', 'mileage': 24680},
    {'make':'Chevy', 'model':'Volt', 'year': 2015, 'color':'black', 'doors':4,'leather':False, 'license': 'JKL444', 'mileage': 7890}
]    

for carDict in carsList:
    if (carDict['doors'] == 4) and (carDict['mileage'] < 50000):
        print carDict['make'], carDict['model'], carDict['license']


print
personalDataDict = {
    'Joe': {'height':73, 'weight': 200, 'sex':'M', 'age':35, 'allergies':['tree pollen','carrots', 'onions']},
    'Sally': {'height':58, 'weight': 100, 'sex':'F', 'age':32, 'allergies':['bee stings']},
    'John': {'height':36, 'weight': 75, 'sex':'M', 'age':8, 'allergies':['peanuts']},
    'Mary': {'height':35, 'weight': 60, 'sex':'F', 'age':7, 'allergies':[]}
}

joesData = personalDataDict['Joe']
joesAllergies = joesData['allergies']
print joesAllergies

marysData = personalDataDict['Mary']
marysAllergies = marysData['allergies']
print marysAllergies


for personName in personalDataDict:
    onePersonDict = personalDataDict[personName]
    allergyList = onePersonDict['allergies']
    if allergyList == []:
        print personName, 'is not allergic to anything'
    else:
        print personName, 'is allergic to the following:'
        for allergy in allergyList:
            print ' ', allergy



        
