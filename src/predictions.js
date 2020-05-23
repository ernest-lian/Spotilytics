import React, {Component} from 'react';


import { Box, Typography } from '@material-ui/core';

import TopNavigationBar from './topNavigationBar.js';

/* Side Navigation Bar */
import SideNavigationBar from './sideNavigationBar.js';

import {Graph} from './graph.js';


import { makeStyles } from '@material-ui/core/styles';


const styles = makeStyles({
});

const Predictions = ({


}) => {
    // console.log('inside dashbaord');
    const classes = styles();
    return (
        <Box>
            <p>Predictions</p>
        </Box>
    );
}

export default Predictions;
