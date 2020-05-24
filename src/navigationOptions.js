import React from 'react';
import { map } from 'lodash';
import {
    Link
} from "react-router-dom";

import { Box, Typography } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';

import { NAVIGATION_SELECTIONS } from './constants/sideNavigationConstants';

const styles = makeStyles({
    hoverNavigation: {
        "&:hover": {
            borderBottom: '#FF7E6B solid 3px'
        }
    },
    typographyStyle: {
        flex: 1,
        'padding-left': '50px',
        color: '#FF7E6B'
    },
    noFontWeight: {
        fontWeight: 100
    }
});

const NavigationOptions = ({

}) => {
    const classes = styles();

    return map(NAVIGATION_SELECTIONS, (option) => {
        return (
            <li className={classes.hoverNavigation}>
                <Link style={{'textDecoration': 'none'}} to={'/'+option} >
                    <Box component={Typography} variant="h6" color='primary' className={`${classes.typographyStyle} ${classes.noFontWeight}`} alignSelf='center'>
                        {option}
                    </Box>
                </Link>
            </li>
        );
    })
}

export default NavigationOptions;