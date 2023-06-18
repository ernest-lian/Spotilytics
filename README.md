# Spotilytics

# Introduction
Spotilytics is an analytic platform leveraging past streaming history on Spotify to provide valuable insights into listening habits and recommends new tracks based on the mood and energy to align with the user’s preferences. 

The purpose of this is to provide a deeper insight in regards to the process from design to development. I'm very intrigued by analytics of my past Spotify streaming history as I feel it is very reflective of the current mood that I am feeling. Being able to compare and contrast with how my preferences in music have changed overtime provides many insights into not only the change of my taste in music but also growth as an individual.

### Project Details
**Role** - Developer & Designer<br>
**Front-end Languages** - HTML5, CSS3, React<br>
**Backend Languages** - Python<br>
**Tools** - Figma

## Hypothesis
The tempo and energy of a song has correlation with their respective genre. We can use these two analytics in order to predict what kind of genre a user enjoys listening to. 

# Context
**Understanding what tempo is**<br>
Tempo is a fundamental element of music that can greatly influence the mood and energy of a piece of music. It is measured in beats per minute (BPM) and refers to the speed or pace at which a piece of music is performed.

A higher tempo indicates a faster pace, while a lower tempo suggests a slower pace. For example, a lively dance track might have a high tempo of around 120 BPM, creating an energetic and upbeat feel, whereas a ballad might have a lower tempo of around 60 BPM, evoking a relaxed and mellow atmosphere to envoke emotion.

**Understanding what energy is**<br>
The energy of a song refers to its perceived level of intensity, liveliness, and overall emotional impact. It represents the dynamic qualities that can evoke emotions and engage listeners. Energy is a subjective aspect of music, varying from songs and genres.

Several factors contribute to the energy of a song, including the tempo, instrumentation, vocal delivery, dynamics, rhythm, and overall production. A fast-paced tempo, aggressive or driving rhythms, and powerful instrumentation can often create high-energy, whereas a slower tempo, softer instrumentation, and soften vocal delivery can envoke a more emotional ambiance.

**Key Insights:**

- Significant correlation between the tempo of a song and its genre. Studies have shown that genres such as EDM, hip-hop, and pop tend to have higher tempos, while classical, jazz, and folk music tend to have lower tempos.
- Correlation between the energy of a song and its genre. Studies have concluded that high-energy genres such as metal, punk, and techno tend to have higher energy levels, while low-energy genres such as country and folk music tend to have lower energy levels.

Overall, while there is some evidence to support the hypothesis that the tempo and energy of a song are correlated with its associated genre, it is important to note that there may be exceptions and variations within each genre.

# **Users & Audiences**

**Target Users:**<br>
- Spotify users can analyze and have a better understanding of their streaming trends that can assist them to discover new songs and genres
- Music critics can analyze the correlation between tempo, energy, and genre to gain insights into the characteristics of different genres and subgenres, and better understand what makes a particular song or artist successful
- Musicians and producers can gain insights into user preferences and adjust their creative strategies accordingly
- Music researchers could be potential stakeholders who could use Spotilytics to conduct further studies and gain deeper insights into the relationship between tempo, energy, and genre. By using Spotilytics as a data source, music researchers can analyze trends and patterns in music consumption and create new theories about the way people listen to music.
- Record labels are another potential stakeholder who could use Spotilytics to gain insights into user preferences and adjust their marketing strategies accordingly

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

# Solution

**Receive analytics to develop better insights on past streaming history**<br>
Process the retrieved data to generate meaningful analytics and insights based on analyzing listening patterns, identifying favorite genres, artists, and tracks.<br>


<img src="/documentation/demo/spotilytics-gif.gif?raw=true" width="250" height="500"/>


**Discover new tracks and genres personalized your streaming history**<br>
Develop new personalized playlists that sync to your Spotify account to assist in discovering new subgenres or niche artists within your favorite genres.<br>

<img src="/documentation/demo/spotilytics-gif-two.gif?raw=true" width="250" height="500"/>


# Development
This section will highlight the development process of the application 
## Database 
My approach when creating the database was a normalized design as I didn't need to incorporate any expensive operations which ultimately prevented any redundancy of storage in the database.

![alt text](https://github.com/ernest-lian/Spotilytics/blob/master/documentation/diagrams/database.png?raw=true)

## Architecture
An overview of the application's architecture
![alt text](https://github.com/ernest-lian/Spotilytics/blob/master/documentation/diagrams/architecture.png?raw=true)


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

There is a correlation in regards to the tempo of a song and its genre. Certain genres such as EDM, hip-hop and pop have higher tempos while classical jazz, and folk music tend to have lower tempos. On the other hand, the energy of a song and its genre also has a correlation as metal, punk and techno tend to have higher energy levels while low-energy genres such as country and folk lean towards having lower energy.

Overall, it is important to recognize that there are exceptions and variations within each genre and the interpretation and classification of a piece of track can be completely subjective. The production styles have changed throughout the generations which lowers the accuracy of songs in the same genre having similar values for tempo and energy. Using a classifier like I did is difficult as genre shouldn't be represented as a numerical value. A better approach would be to find tracks listened by others with a similar streaming history to provide higher accuracy.

## Performance Bottlenecks
1. Making multiple HTTP requests resulted in having to block when switching pages
	- Made one single HTTP request at the beginning of connection with the server
		- High latency can cause many small requests to perform a lot worse than one large one
		- Less extra HTTP request and response headers to handle
		- Easy to define each request as a transaction that was applied or rolled back instead of having some requests that succeeded and some that failed which can cause inconsistency 
2. Having the Analytics table split into 4 respective tables that represent each respective analytic
	- Unnecessary as the schema was the same for all 4 tables
	- Resulted in extra calls to the database which can be expensive
	- This can result in eventually running out of memory but sharding can resolve this issue

## Ways to Scale
3. Deleting the database every single time 
	- Fetching the most up to date analytics when the user requests it but otherwise query the database to prevent having to do this
	- Schedule a cron job that periodically updates the analytics for users who are already registered and fetch analytics for new users or when it is requested
4. Initialized database connections every query
	- Single database dao entity could be solution but this can be a single point of failure as well concurrent connections will have to block
	- Implementing a database pooling strategy will allow me to reuse database connections
5. Many database accesses
	- Can have some sort of a queue for the clients as it is write heavy
6. Supports only a single client
	- Implement multithreading to allow concurrent access to the server by multiple clients
7. User has a one-to-many relationship with the other tables in the database which can result in not enough memory if hypothetically all 271 million Spotify users used this
	- Store specific subset of UUIDs on specific machines by sharding
	- Add a directory table that maps the specific range of UUIDs to the specific server that the data is on to make the query time faster

# Instructions
## Folder structure
Spotlytics
- src (stores the front end components)
	- backend (stores the backend and machine learning code)
		- machine_learning (stores the machine learning code)
		- src (stores the backend code)
	- package.json
	- index.js

## Execution instructions
### Front end
- Navigate to the directory Spotlytics and execute npm run dev to start up the front end
### Back end
- Add respective Spotify username, client ID and client secret to the login_spotify method in app.py 
- Navigate to the directory Spotilytics/backend/src and execute flask run to start up the back end

