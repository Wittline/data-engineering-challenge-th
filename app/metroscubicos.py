class metroscubicos:
    def __init__(self, **arguments):
        
         self.property_name = arguments.get('property_name', '') 
         self.url = arguments.get('url', '')
         self.price = arguments.get('price', 0.0)
         self.adress = arguments.get('adress', '')
         self.street = arguments.get('street', '')
         self.number = arguments.get('number', 0)
         self.settlement = arguments.get('settlement', '')
         self.town = arguments.get('town', '')
         self.state = arguments.get('state', '')
         self.county = arguments.get('county', '')                
         self.description = arguments.get('description', '') 
         self.amenities = arguments.get('amenities', '') 
         self.size = arguments.get('size', 0) 
         self.first_picture = arguments.get('first_picture', '')
