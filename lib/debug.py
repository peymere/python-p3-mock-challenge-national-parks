#!/usr/bin/env python3
import ipdb


from classes.many_to_many import NationalPark
from classes.many_to_many import Visitor
from classes.many_to_many import Trip

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    park1 = NationalPark("Grand Canyon")
    park2 = NationalPark("Redwoods")

    v1 = Visitor("Peyton")
    v2 = Visitor("james")

    trip1 = Trip(v1, park1, "October 3rd", "October 12th")
    trip2 = Trip(v1, park1, "April 15th", "October 12th")
    trip3 = Trip(v2, park1, "May 3rd", "October 12th")
    # trip4 = Trip(v1, park1, "Cat 12th", "October 12th")
    # trip5 = Trip(v1, park1, "October 35th", "October 12th")
    # trip6 = Trip(v1, park1, "June", "October 12th")
   

    ipdb.set_trace()
