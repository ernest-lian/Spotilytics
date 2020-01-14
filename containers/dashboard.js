import React, {Component} from 'react';
import {TopNavigationBar} from './topNavigationBar.js';

const element = (
    <h1>Dashboard screen</h1>
);

export default class Dashboard extends Component {
    render () {
        return (<TopNavigationBar />);
    }
}