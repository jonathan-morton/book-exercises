#creates a mapping of state to abbreviation
states = {
          'Oregon': 'OR',
          'Florida': 'FL',
          'California': 'CA',
          'New York': 'NY',
          'Virginia': 'VA'
          }

#creates a basic set of states and some cities in them
cities = {
          'CA': 'San Francisco',
          'VA': 'Richmond',
          'FL': 'Jacksonville',
          }

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

#print some states
print '-'*10
print "Virginia's abbreviation is: ", states['Virginia']
print "Florida's abbreviation is: ", states['Florida']

#prints every state's abbreviation
print "-" * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

#print every city in state
print "-" * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state,
                                                          abbrev,
                                                          cities[abbrev])
print '-' * 10
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas"

city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city