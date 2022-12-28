class Actordto:
    def __init__(self, actor_id,firstname,lastname,last_update):
        self.actor_id=actor_id
        self.FirstName=firstname
        self.LastName=lastname      
        self.last_update=last_update
    
    def __str__(self):
        return f'{self.actor_id}, {self.FirstName}, {self.LastName}, {self.last_update}'
        
    @property
    def actor_id(self):
        return self._actor_id 
    
    @actor_id.setter    
    def actor_id(self, actor_id):
        self._actor_id = actor_id
    
    @property
    def LastName(self):
        return self._LastName 
    
    @LastName.setter    
    def LastName(self, LastName):
        self._LastName = LastName
        
    @property
    def FirstName(self):
        return self._FirstName 
    
    @FirstName.setter    
    def FirstName(self, FirstName):
        self._FirstName = FirstName
        
    @property
    def last_update(self):
        return self._last_update 
    
    @last_update.setter    
    def last_update(self, last_update):
        self._last_update = last_update
1