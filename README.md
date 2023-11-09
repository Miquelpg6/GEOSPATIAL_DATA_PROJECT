# PROJECT 3 - GEOSPATIAL DATA

## Overview
The aim of this project is to select an office location for a new gaming business. The company has the following number of workers for each department:

- 20 Designers
- 5 UI/UX Engineers
- 10 Frontend Developers
- 15 Data Engineers
- 5 Backend Developers
- 20 Account Managers
- 1 Maintenance guy that loves basketball
- 10 Executives
- 1 CEO/President.

Each department has some requisites that have to be taken into account at the moment of the location decision. The requisites are the following:

- Designers like to go to design talks and share knowledge. There must be some nearby companies that also do design. 30% of the company staff have at least 1 child.
- Developers like to be near successful tech startups that have raised at least 1 Million dollars.
- Executives like Starbucks A LOT. Ensure there's a Starbucks not too far.
- Account managers need to travel a lot.
- Everyone in the company is between 25 and 40, give them some place to go party.
- The CEO is vegan.
- If you want to make the maintenance guy happy, a basketball stadium must be around 10 Km.
- The office dog—"Dobby" needs a hairdresser every month. Ensure there's one not too far away.


## Libraries/Tools Used:

This code was written in Python/Jupyter Notebook, using the following libraries:

- Jupyter Notebook
- Foursquare API
- Google Maps API
- MongoDB Geospatial Queries
- Python
- Pandas
- NumPy
- Folium

## FIRST PART - FILTERING BUSINESS & CITIES

Using the document companies.csv, filtered technological companies per country. We found that most companies were settled in the USA, the second country with higher number of tech companies was Great Britain and third place was Canada. We decided that Canada was a Country where we could place our office as it has a higher amount of technological companies but not that much as the USA and Great Britain where the competition is fierce. Furthermore, we selected the cities of Montreal, Toronto and Ottawa, with 48, 131 and 24 tech related companies for each city. The three are perfect cities as they are very close to New York and the East Coast where there are a lot of tech companies.

Having chosen 3 cities that meet our requirements, we also would like to take into consideration the workers requirements in order to create a good working environment and try to make all them happy.

### MONTREAL

![image](https://github.com/Miquelpg6/project_3/blob/main/IMAGES/MONTREAL_COMPANIES.png?raw=true)

![image](https://github.com/Miquelpg6/project_3/blob/main/IMAGES/MONTREAL_HEATMAP.png?raw=true)

### TORONTO

![image](https://github.com/Miquelpg6/project_3/blob/main/IMAGES/TORONTO_COMPANIES.png?raw=true)

![image](https://github.com/Miquelpg6/project_3/blob/main/IMAGES/TORONTO_HEATMAP.png?raw=true)

### OTTAWA

![image](https://github.com/Miquelpg6/project_3/blob/main/IMAGES/OTTAWA_COMPANIES.png?raw=true)

![image](https://github.com/Miquelpg6/project_3/blob/main/IMAGES/OTTAWA_HEATMAP.png?raw=true)


## SECOND PART - COMPARING DISTANCES AND VENUES FOR EVERY CITY

### 1. BARS - NIGHT CLUBS

Compared the category bars/nightclubs in order to see the best city with this item. It's an important aspect because as we know, all the workers are young, and they would like to have some night-life around the office. The analysis was made with 1km around the selected point from each city. After analyzing it, we found the following results.

### Montreal
I have found that they are 28 bars, pubs and nightclubs in the area of Montreal.

### Toronto
Toronto has a total of 27 bars, pubs and nightclubs in the area. 

### Ottawa
In Ottawa there are a total of 41 bars, pubs and nightclubs around the area.


In this category we cannot make any decisions, as in all the cities there is a diverse range of places.


### 2. SCHOOLS 

As 30% of the workers have children, is it crucial to analyze the number of schools present in the city area, near the company. As we know, a lot of workers would like to leave their children in the morning and pick them up in the afternoon. For this category, we set a radius of 2km around the possible office. We found the following results.

### Montreal

In Montreal, there are 18 different schools within a 2km radius. It is a wide range of schools from where the parents could choose their children education. There are also high schools and University for the older ones. 

### Toronto

In Toronto, we find 20 different schools in the 2km radius. The offer is similar to Montreal. Workers can be satisfied with the options. There are also present High Schools and Universities. We have to say that in Toronto is present the best university of Canada, University of Toronto, that is a plus point for the city. 

### Ottawa

In Ottawa, we can find only 10 schools in a 2km radius, Schools in Ottawa are spread out the business center, so workers would have to find solutions like driving them to school. That can be an inconvenient for some workers.


### 3. AIRPORT

### Montreal
In Montreal there is the Montréal-Pierre Elliott Trudeau International Airport at 15.323km from the chosen location, it's not far away and within 15-20 minutes workers could be in the airport. 

### Toronto

In Toronto, there are two important airports. The Toronto Pearson International Airport, known for being the airport with more flights/year, so it's the most important airport in Canada. The positive thing from Toronto is that it also has another important airport, the Billy Bishop Toronto City Airport, this airport also operates internationally, and it's only 2,5km from the chosen office location. 

### Ottawa
In Ottawa is present the Canada's capital airport, the Ottawa Macdonald-Cartier International Airport, at only 10km from the office chosen location. 

In this section the most efficient location is Toronto as it has 2 airports and one of them is super close to the offices. That is an advantage for the 20 Account managers that have to travel a lot. 


### 4. STARBUCKS

Starbucks are present in all the cities, and it's not a major difference between cities as all of them have multiple Starbucks within 1km radius, so the 10 executives can enjoy their morning coffee from Starbucks. 


### 5. DESIGN COMPANIES

Design companies is a crucial point as there are 20 developers who need inspiration and like to go to design talks, so there must be design companies in the location surroundings. The search has been made within 1 km distance, so workers can go walking to the talks


### Montreal
In Montreal there are 4 Design companies within 1km. 

### Toronto
In Toronto, there are present 19 design companies. There are multiple options from where designers could get the inspiration and knowledge.

### Ottawa
In Ottawa, we only find 3 companies in the design field within 1km, is not enough for our designers.


### 6. VEGAN RESTAURANTS

Everybody knows that our beloved CEO is vegan, so we would like to give him some options to choose from. It would be necessary to have some vegan restaurants in the area.

### Montreal
In Montreal, there are present 8 vegan restaurants in 1km radius. More than enough for our CEO to chose between. 

### Toronto
In Toronto, we again find the wider range of vegan restaurants, with more than 40 places with vegan dishes on its menu the CEO would be delighted with them. 

### Ottawa
In Ottawa despite being the capital, we can find 10 vegan restaurants o restaurants with vegan options in its menu. 

### 7. BONUS - STADIUMS

In each city there are present basketball stadiums but in Toronto there is the Toronto Raptors basketball stadium, Toronto Raptor play in the NBA. The what would make our maintenance guy very happy.


## PART THREE - VISUALIZATION & DECISION

In this part, we make the final maps for each city, visualizing the total number of venues per city.

### Montreal Final Map

![image](https://github.com/Miquelpg6/project_3/blob/main/IMAGES/MONTREAL_FINAL.png?raw=true)


### Toronto Final Map

![image](https://github.com/Miquelpg6/project_3/blob/main/IMAGES/TORONTO_FINAL.png?raw=true)


# Ottawa Final Map

![image](https://github.com/Miquelpg6/project_3/blob/main/IMAGES/OTTAWA_FINAL.png?raw=true)


After taking into account the number of options present on every city for each radius, we can say that the best city to place our new office is Toronto. Exactly in the coordinates (latitude = 43.654770, longitude = -79.392346).

