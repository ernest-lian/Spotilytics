import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import configureStore from './src/store';
import Application from './src/user-interfaces/application'
import 'bootstrap/dist/css/bootstrap.css';

ReactDOM.render(<Provider store={configureStore()}>
                    <Application/>
                </Provider>,
                document.getElementById('app')
)
