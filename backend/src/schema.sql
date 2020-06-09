DROP TABLE IF EXISTS Analytics;
DROP TABLE IF EXISTS TopArtists;
DROP TABLE IF EXISTS TopTracks;
DROP TABLE IF EXISTS Recommendations;
DROP TABLE IF EXISTS Users;


CREATE TABLE IF NOT EXISTS TopArtists(
    user_id TEXT NOT NULL,
    name TEXT NOT NULL,
    profile TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users (user_id)
);

CREATE TABLE IF NOT EXISTS TopTracks (
    user_id TEXT NOT NULL,
    title TEXT NOT NULL,
    artist TEXT NOT NULL,
    cover TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users (user_id)
);

CREATE TABLE IF NOT EXISTS Analytics(
    user_id TEXT NOT NULL,
    analytic_type TEXT NOT NULL,
    title TEXT NOT NULL,
    artist TEXT NOT NULL,
    cover TEXT NOT NULL,
    greatest REAL NOT NULL,
    average REAL NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users (user_id)
);

CREATE TABLE IF NOT EXISTS Recommendations(
    user_id TEXT NOT NULL,
    title TEXT NOT NULL,
    artist TEXT NOT NULL,
    cover TEXT NOT NULL,
    uri TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users (user_id)
);

CREATE TABLE IF NOT EXISTS Users (
    id TEXT PRIMARY KEY,
    user_name TEXT NOT NULL,
    name TEXT NOT NULL,
    profile TEXT NOT NULL
);