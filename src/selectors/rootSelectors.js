
import { createSelector } from 'reselect';

export const nameState = state => state['simpleReducer'];

export const getName = createSelector(
    nameState,
    (state) => {
        console.log('state: ', state.get('name'));
        return state.get('name');
    }
);

export const getDisplayPicture = createSelector(
    nameState,
    (state) => {
        return state.get('displayPicture');
    }
);

export const getCurrentPage = createSelector(
    nameState,
    (state) => {
        return state.get('currentPage');
    }
);

export const getTopSongs = createSelector(
    nameState,
    (state) => {
        return state.get('topSongs');
    }
);

export const getTopArtists = createSelector(
    nameState,
    (state) => {
        return state.get('topArtists');
    }
);


export const getAnalytics = createSelector(
    nameState,
    (state) => {
        return state.get('analytics');
    }
);