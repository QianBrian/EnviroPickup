# EnviroPickup
GIS implementation providing the City of London Ontario a way for residences and the city to communicate to dispose of non-collectable items.

##########################
Through Twilio sms services, EnviroPickup offers an easy way to notify the City of London to pick-up non-collectable garbage from the curb. 
Items such as fridges, furniture, or harmful chemicals must be brought to EnviroDepots to be disposed of instead of being left out on the curb or thrown away normally.

To help the city of London and to prevent further damage to the environment with potentially harmful chemical waste, EnviroPickup can solve this issue through GIS technology.

Open data on London's garbage collection zones and addresses were used. Through point and polygon detection from lat/long coordinates provided, an address was considered to be within a Zone if it's point coordinate was within a zone polygon. Once a threshold of residence within an area is reached, specialized garbage trucks would be dispatched to pick up the non-collectable garbage—only after sending an automatic notification that lets the users be aware of the pickup day.

Twilio, shapely, pandas, and fiona libraries, as well as the City of London's recent open database was used for building this project.

City of London Address database: https://opendata.london.ca/datasets/24b16712d14c42d7ac1e679c8c89bf47_0

City of London Garbage Zone database: https://opendata.london.ca/datasets/8a697b324156438f952c47d495c129af_13



HackWestern6
##########################
