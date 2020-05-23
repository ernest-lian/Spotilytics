import React from 'react';
import ReactDOM from 'react-dom';
import { createStore } from 'redux';
import { Provider } from 'react-redux';
import configureStore from './src/store';

import Application from './src/application'

ReactDOM.render(<Provider store={configureStore()}>
                    <Application/>
                </Provider>,
                document.getElementById('app')
)
