
import { createSelector } from 'reselect';

export const baseState = state => state['simpleReducer'];

export const getName = createSelector(
    baseState,
    (state) => {
        return state.get('name');
    }
);

export const getDisplayPicture = createSelector(
    baseState,
    (state) => {
        return state.get('displayPicture');
    }
);

export const getCurrentPage = createSelector(
    baseState,
    (state) => {
        return state.get('currentPage');
    }
);

export const getTopSongs = createSelector(
    baseState,
    (state) => {
        return state.get('topSongs');
    }
);

export const getTopArtists = createSelector(
    baseState,
    (state) => {
        return state.get('topArtists');
    }
);

export const getAnalytics = createSelector(
    baseState,
    (state) => {
        return state.get('analytics');
    }
);

export const getRecommendations = createSelector(
    baseState,
    (state) => {
        return state.get('recommendations');
    }
);
