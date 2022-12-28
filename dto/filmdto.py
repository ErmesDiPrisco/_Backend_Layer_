class Filmdto:
    def __init__(self, film_id,title,description,release_year, language_id, original_lanid, rental_duration, rental_rate, lenght, replacement_cost, rating, special_feature, last_update):
        self.film_id=film_id
        self.title=title
        self.description=description      
        self.release_year=release_year
        self.language_id=language_id
        self.original_lanid=original_lanid
        self.rental_duration=rental_duration
        self.rental_rate=rental_rate
        self.lenght=lenght
        self.replacement_cost=replacement_cost
        self.rating=rating
        self.special_feature=special_feature
        self.last_update=last_update

    def __str__(self):
        return '{},{},{},{},{},{},{},{},{},{},{},{}'.format(self.film_id,self.title,self.description,self.release_year, self.language_id, self.original_lanid, self.rental_duration, self.rental_rate, self.lenght, self.replacement_cost, self.rating, self.special_feature, self.last_update)
        
    @property
    def film_id(self):
        return self._film_id 
    
    @film_id.setter    
    def film_id(self, film_id):
        self._film_id = film_id
    
    @property
    def description(self):
        return self._description 
    
    @description.setter    
    def description(self, description):
        self._description = description
        
    @property
    def title(self):
        return self._title 
    
    @title.setter    
    def title(self, title):
        self._title = title
        
    @property
    def release_year(self):
        return self._release_year 
    
    @release_year.setter    
    def release_year(self, release_year):
        self._release_year = release_year
    
    @property
    def language_id(self):
        return self._language_id 
    
    @language_id.setter    
    def language_id(self, language_id):
        self._language_id = language_id
    
    @property
    def original_lanid(self):
        return self._original_lanid 
    
    @original_lanid.setter    
    def original_lanid(self, original_lanid):
        self._original_lanid = original_lanid
    
    @property
    def rental_duration(self):
        return self._rental_duration 
    
    @rental_duration.setter    
    def rental_duration(self, rental_duration):
        self._rental_duration = rental_duration

    @property
    def rental_rate(self):
        return self._rental_rate 
    
    @rental_rate.setter    
    def rental_rate(self, rental_rate):
        self._rental_rate = rental_rate

    @property
    def lenght(self):
        return self._lenght 
    
    @lenght.setter    
    def lenght(self, lenght):
        self._lenght = lenght

    @property
    def replacement_cost(self):
        return self._replacement_cost 
    
    @replacement_cost.setter    
    def replacement_cost(self, replacement_cost):
        self._replacement_cost = replacement_cost

    @property
    def rating(self):
        return self._rating 
    
    @rating.setter    
    def rating(self, rating):
        self._rating = rating

    @property
    def special_feature(self):
        return self._special_feature 
    
    @special_feature.setter    
    def special_feature(self, special_feature):
        self._special_feature = special_feature

    @property
    def last_update(self):
        return self._last_update 
    
    @last_update.setter    
    def last_update(self, last_update):
        self._last_update = last_update                        