import React, {Component} from 'react';


import { Box, Typography } from '@material-ui/core';

import {TopNavigationBar} from './topNavigationBar.js';

/* Side Navigation Bar */
import {SideNavigationBar} from './sideNavigationBar.js';

import { Login } from './login.js';

import { makeStyles } from '@material-ui/core/styles';


const styles = makeStyles({
    listItemStyle: {
        'z-index': 'auto'
    },
    sideNavigationBarStyle: {
        'padding': '60px',
        backgroundColor: 'black'
    }
});

// function RenderDashboard(){
//     const classes = styles();
//     return (
//         <div>
//             <div>
//                 "testing"
//                 <TopNavigationBar />  
//             </div>
//             <div style={{'padding-top': '60px'}}>
//                 "123"
//                 <SideNavigationBar/>
//             </div>
//         </div>);
// }

function RenderDashboard(){
    return (
        <Login/>);
}

export default class Dashboard extends Component {
    render () {
        return <RenderDashboard />
    }
}