class NationalPark:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) < 1 or len(name) > 15:
            raise ValueError(
                "Name must be between 1-15 characters"
            )
        if hasattr(self, "_name"):
            raise AttributeError("Name can not be changed")
        self._name = name

    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        return list({trip.visitor for trip in self.trips() if isinstance(trip.national_park == self)})
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        trips = self.trips()
        best_visitor = None
        max_trip_count = 0

        for trip in trips:
            visitor = trip.visitor
            visitor_trip_count = sum(1 for t in trips if t.visitor == visitor)
            if visitor_trip_count > max_trip_count:
                max_trip_count = visitor_trip_count
                best_visitor = visitor
        
        return best_visitor



class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor
        else:
            raise ValueError("visitor must be an instance of Visitor")
        
    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        else:
            raise ValueError("national_park must be an instance of NationalPark")

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        if not isinstance(start_date, str):
            raise TypeError("start_date must be a string")
        
        date_parts = start_date.split()
        
        if len(date_parts) != 2:
            raise ValueError("start_date must be in the format 'Month Day'")
        
        month, day = date_parts

        valid_months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
        if month.lower() not in valid_months:
            raise ValueError("Invalid month in start_date")
        
        day_num = day[:-2]
        day_suffix = day[-2:]
        if day_suffix not in ['st', 'nd', 'rd', 'th']:
            raise ValueError("Day must be an ordinal number")
        if not day_num.isdigit() or int(day_num) < 1 or int(day_num) > 31:
            raise ValueError("Day must be a number between 1 through 31")
        
        
        self._start_date = f"{month.capitalize()} {day}"

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        if not isinstance(end_date, str):
            raise TypeError("end_date must be a string")
        
        date_parts = end_date.split()
        
        if len(date_parts) != 2:
            raise ValueError("end_date must be in the format 'Month Day'")
        
        month, day = date_parts

        valid_months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
        if month.lower() not in valid_months:
            raise ValueError("Invalid month in end_date")
        
        day_num = day[:-2]
        day_suffix = day[-2:]
        if day_suffix not in ['st', 'nd', 'rd', 'th']:
            raise ValueError("Day must be an ordinal number")
        if not day_num.isdigit() or int(day_num) < 1 or int(day_num) > 31:
            raise ValueError("Day must be a number between 1 through 31")
        
        self._end_date = f"{month.capitalize()} {day}"

class Visitor:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) < 1 or len(name) > 15:
            raise ValueError(
                "Name must be between 1-15 characters"
            )
        self._name = name

    def trips(self):
        return [trips for trips in Trip.all if trips.visitor == self]
    
    def national_parks(self):
        return list({trip.national_park for trip in self.trips() if isinstance(trip.visitor == self)})
    
    def total_visits_at_park(self, park):
        visit_count = 0
        for trip in self.trips():
            if isinstance(trip.national_park, NationalPark) and trip.national_park == park:
                visit_count += 1
        return visit_count