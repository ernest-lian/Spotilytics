import Immutable from 'immutable';

const initialState = Immutable.Map({
  'name': '',
  'currentPage': 'Dashboard'
});

const simpleReducer = (state = initialState, action) => {
    switch (action.type) {
      case 'SET_NAME':
        state = state.set('name', action.payload);
        return state
      case 'SET_DISPLAY_PICTURE':
        console.log('set display picture');
        state = state.set('displayPicture', action.payload);
        return state
      case 'UPDATE_CURRENT_PAGE':
        console.log('setting the current page');
        state = state.set('currentPage', action.payload);
        return state
      case 'SET_TOP_SONGS':
        console.log('set history case');
        console.log('history payload: ', action.payload);
        state = state.set('topSongs', action.payload);
        return state
      case 'SET_TOP_ARTISTS':
        state = state.set('topArtists', action.payload);
        return state
      case 'SET_ANALYTICS':
        state = state.set('analytics', action.payload);
        return state
    default:
      return state
    }
   }

export default simpleReducer