# Spotilytics

# Introduction
Hello! Here is documentation for my project Spotlytics to give you a deeper insight in regards to the process from design to development. The reason that I created this project is because I'm really into music, and a feature that Spotify provides for its users year end, is Spotify Wrapped. The reason why I love to see analytics of my previous Spotify streaming history is because for me personally I believe that the music I listen to is very reflective of the current mood that I am feeling. With this, it's very interesting for me to go back and see how my preferences in music have changed over the past year. While looking at the information that Spotify provides through it's API, I had come up with a hypothesis in regards to recommending new music for users to listen to.

## Hypothesis
The tempo and energy of a song has correlation with their respective genre. We can use these two analytics in order to predict what kind of genre a user enjoys listening to. 

# Design

This section will highlight the design process of the application 

## Elicitation of Requirements
Collected the requirements for the project to have a better scope prior to the development

2.1 View Analytics
- **2.1.1 Description:** An authorized user may receive their personalized analytics
  - 2.1.2 Functional Requirements
    - R-1: An authorized user will be able to see their top artists
    - R-2: An authorized user will be able to see their top tracks
    - R-3: An authorized user will be able to see their analytics (Fastest, most popular, longest, most energetic tracks)
    - R-4: An authorized user will be notified of any errors that occur while gathering their personal analytics

2.2 View Recommendations
- **2.2.1 Description**: An authorized user may view their recommended tracks
  - 2.2.2 Functional Requirements:
    - R-1: An authorized user will be able to see their recommended tracks based on their past streaming history

2.3 Creating Playlists
- **2.3.1 Description**: An authorized user may create a playlist using the recommendations based on their past streaming history
  - 2.3.2 Functional Requirements
    - R-1: An authorized user will be able to create a playlist on their Spotify account using the recommendations based on their past streaming history
    - R-2: An authorized user will receive an error if the playlist name is invalid (ex: empty string)

2.4 Login to Spotify
  - **2.4.1 Description**: A user may log into Spotify using OAuth 2.0
    - 2.4.2 Functional Requirements
      - R-1: Prompt the user to log onto their spotify account to have access to their account's information				 			

## User Interface
Initial low fidelity prototype designs for the application's user interface to provide a mockup for reference. The reason that I crated these is because it gave me a general idea as to how I wanted the UI to look like. This was extremely useful as I had realized after that the side navigation bar I had initially planned for created a lot of unecesscary space and was not providing a experience for the user which made me ultimately decide to switch up the layout.

Dashboard Page\
![alt text](https://github.com/ernest-lian/Spotilytics/blob/master/documentation/prototypes/dashboard.PNG?raw=true)

Analytics Page\
![alt text](https://github.com/ernest-lian/Spotilytics/blob/master/documentation/prototypes/analytics.PNG?raw=true)

Predictions Page\
![alt text](https://github.com/ernest-lian/Spotilytics/blob/master/documentation/prototypes/predictions.PNG?raw=true)


## Color Palettes

Background\
#A8E6CF
#B49FCC
#DCEDC1
#FFD3B6
#CADBC8

Text\
#FAFF00
#F4C3C2

# Development
This section will highlight the development process of the application 
## Database 
My approach when creating the database was a normalized design as I didn't need to incorporate any expensive operations which ultimately prevented any redundancy of storage in the database.




## Endpoints
/login
- Type: POST
- Purpose: Logs the user into Spotify using OAuth 2.0 and generates the analytics and recommendations respectively

/playlist
- Type: POST
- Payload:
  - playlist_name - Name of playlist to be created
- Purpose: Creates a playlist with the user's recommendations based on their past streaming history

# Takeaways

The genre of a song is a subjective opinion that cannot be determined by numerical values as it is based on the ambiance that it provides a user. The production styles have changed throughout the generations which lowers the accuracy of same styled songs to have similar values for the tempo and energy. Even if I had a dataset of 1,000,000 tracks there would be too much variation in the relationship between tempo and energy for a correlation to appear. Using a classifier like I did is difficult as genre shouldn't be represented as a numerical value. A better approach would be to find tracks listened by other individuals who share a similar streaming history as you do which is the approach that streaming platforms such as Apple Music and Spotify use which is why their recommendations have a lot higher accuracy.
Performance Bottlenecks
Making multiple HTTP requests resulted in having to block when switching pages
Made one single HTTP request at the beginning of connection with the server
High latency can cause many small requests to perform a lot worse than one large one
Less extra HTTP request and response headers to handle
Easy to define each request as a transaction that was applied or rolled back instead of having some requests that succeeded and some that failed which can cause inconsistency 
Having the Analytics table split into 4 respective tables that represent each respective analytic
Unnecessary as the schema was the same for all 4 tables
Resulted in extra calls to the database which can be expensive
This can result in eventually running out of memory but sharding can resolve this issue
Ways to Scale
Deleting the database every single time 
Fetching the most up to date analytics when the user requests it but otherwise query the database to prevent having to do this
Initialized database connections every query
Single database dao entity could be solution but this can be a single point of failure as well concurrent connections will have to block
Implementing a database pooling strategy will allow me to reuse database connections
Many database accesses
Can have some sort of a queue for the clients as it is write heavy
Supports only a single client
Implement multithreading to allow concurrent access to the server by multiple clients
User has a one-to-many relationship with the other tables in the database which can result in not enough memory if hypothetically all 271 million Spotify users used this
Store specific subset of UUIDs on specific machines by sharding
Add a directory table that maps the specific range of UUIDs to the specific server that the data is on to make the query time faster

# Instructions
## Folder structure
Spotlytics
------- src (stores the front end components)
	------- backend (stores the backend and machine learning code)
		------- machine_learning (stores the machine learning code)
		------- src (stores the backend code)
	------- package.json
	------- index.js

## Execution instructions
### Front end
Navigate to the directory Spotlytics and execute npm run dev to start up the front end
### Back end
Navigate to the directory Spotilytics/backend/src and execute flask run to start up the back end

