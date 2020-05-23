export const setName = name => ({
     type: 'SET_NAME',
     payload: name
});

export const setDisplayPicture = displayPicture => ({
     type: 'SET_DISPLAY_PICTURE',
     payload: displayPicture
});

export const updateCurrentPage = currentPage => ({
     type: 'UPDATE_CURRENT_PAGE',
     payload: currentPage
});

export const setTopSongs = topSongs => ({
     type: 'SET_TOP_SONGS',
     payload: topSongs
});

export const setTopArtists = topArtists => ({
     type: 'SET_TOP_ARTISTS',
     payload: topArtists
});

export const setAnalytics = analytics => ({
     type: 'SET_ANALYTICS',
     payload: analytics
});