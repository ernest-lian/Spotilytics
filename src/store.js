import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import rootReducer from './reducers/rootReducer';
import { composeWithDevTools } from 'redux-devtools-extension';
import Immutable from 'immutable';

export default function configureStore(initialState=Immutable.Map({})) {
 return createStore(
  rootReducer,
  composeWithDevTools(
   applyMiddleware(thunk)
 ));
}