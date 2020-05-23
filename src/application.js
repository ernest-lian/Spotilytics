import React, {Component, useEffect} from 'react';
import { connect } from 'react-redux'
import { createStructuredSelector } from 'reselect';
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
  } from "react-router-dom";

import { Box, Typography, Button, AppBar, Toolbar } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import MenuIcon from '@material-ui/icons/Menu';

import Dashboard from './dashboard.js';
import Analytics from './analytics.js';
import Predictions from './predictions.js';

import { setName, setDisplayPicture, setTopSongs, setTopArtists, setAnalytics } from './actions/rootAction';
import { getName, getDisplayPicture, getCurrentPage } from './selectors/rootSelectors';



const styles = makeStyles({
    appBarStyle: {
        backgroundColor: 'white'
    },
    hoverNavigation: {
        "&:hover": {
            borderBottom: '#FF7E6B solid 3px'
        }
    },
    selectedNavigation: {
        borderBottom: 'black solid 3px'
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

function loginUser(setName, setDisplayPicture, setTopSongs, setTopArtists, setAnalytics) {
    var xhr = new XMLHttpRequest()

    xhr.addEventListener('load', () => {
    })

    xhr.open('POST', 'http://localhost:5000/login', false)

    xhr.send()

    console.log(JSON.parse(xhr.response))
    const name = JSON.parse(xhr.response)['body']['name']
    const displayPicture = JSON.parse(xhr.response)['body']['display_picture']
    const topSongs = JSON.parse(xhr.response)['body']['top_tracks'].splice(0,5)
    const topArtists = JSON.parse(xhr.response)['body']['top_artists']
    const analytics = JSON.parse(xhr.response)['body']['analytics']

    setDisplayPicture(displayPicture)
    setName(name)
    setTopSongs(topSongs)
    setTopArtists(topArtists)
    setAnalytics(analytics)
}

const Application = ({
    setName,
    setDisplayPicture,
    setTopSongs,
    setAnalytics,
    setTopArtists,
    displayPicture
}) => {
    const classes = styles();
    loginUser(setName, setDisplayPicture, setTopSongs, setTopArtists, setAnalytics);

    return(
    <Box display='flex' flexDirection='column' height='100%' width='100%'>
        <Router>
            <Box>
                <AppBar position='fixed' className={classes.appBarStyle}>
                    <Box display='flex' justifyContent='space-around' id='hello'>
                        <Box alignSelf='center'>
                            <Box component={Typography} variant="h6" color='primary' className={classes.typographyStyle} alignSelf='center'>
                                Spotilytics
                            </Box>
                        </Box>
                        <Box display='flex' alignItems='center'>
                            <ul style={{'display':'flex', 'listStyleType': 'none', 'alignItems': 'center'}}>
                                <li className={classes.hoverNavigation}>
                                <Link style={{'textDecoration': 'none'}} to="/dashboard" >
                                    <Box component={Typography} variant="h6" color='primary' className={`${classes.typographyStyle} ${classes.noFontWeight}`} alignSelf='center'>
                                        Dashboard
                                    </Box>
                                </Link>
                                </li>
                                <li className={classes.hoverNavigation}>
                                <Link style={{'textDecoration': 'none'}}to="/analytics">
                                    <Box component={Typography} variant="h6" color='primary' className={`${classes.typographyStyle} ${classes.noFontWeight}`} alignSelf='center'>
                                        Analytics
                                    </Box>
                                </Link>
                                </li>
                                <li className={classes.hoverNavigation}>
                                <Link style={{'textDecoration': 'none'}}to="/predictions">
                                    <Box component={Typography} variant="h6" color='primary' className={`${classes.typographyStyle} ${classes.noFontWeight}`} alignSelf='center'>
                                        Predictions
                                    </Box>
                                </Link>
                                </li>
                                <li style={{'paddingLeft': '16px'}}>
                                    <Box component='img' style={{'objectFit': 'cover'}} src={displayPicture} display='flex' alignItems='center' borderRadius='50%' height='50px' width='50px'/>
                                </li>
                            </ul>
                        </Box>
                    </Box>
                </AppBar>
            </Box>

            <Box paddingTop='82px'>
                <Switch>
                    <Route path="/dashboard">
                        <Dashboard />
                    </Route>
                    <Route path="/analytics">
                        <Analytics />
                    </Route>
                    <Route path="/predictions">
                        <Predictions />
                    </Route>
                </Switch>
            </Box>
        </Router>
    </Box>);
}

const mapStateToProps = createStructuredSelector({
    displayPicture: getDisplayPicture
});

const mapDispatchToProps = {
    setName,
    setDisplayPicture,
    setTopSongs,
    setTopArtists,
    setAnalytics
};

export default connect(
    mapStateToProps,
    mapDispatchToProps,
)(Application);
