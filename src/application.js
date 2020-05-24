import React, {useEffect} from 'react';
import { connect } from 'react-redux'
import { createStructuredSelector } from 'reselect';
import {
    BrowserRouter as Router,
    Switch,
    Route
  } from "react-router-dom";

import { Box, Typography, AppBar } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';

import Dashboard from './dashboard.js';
import Analytics from './analytics.js';
import Recommendations from './recommendations.js';
import NavigationOptions from './navigationOptions.js';

import { setName, setDisplayPicture, setTopSongs, setTopArtists, setAnalytics, setRecommendations } from './actions/rootAction';
import { getDisplayPicture } from './selectors/rootSelectors';


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

function loginUser(setName, setDisplayPicture, setTopSongs, setTopArtists, setAnalytics, setRecommendations) {
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
    const recommendations = JSON.parse(xhr.response)['body']['recommendations']

    setDisplayPicture(displayPicture)
    setName(name)
    setTopSongs(topSongs)
    setTopArtists(topArtists)
    setAnalytics(analytics)
    setRecommendations(recommendations)
}

const Application = ({
    setName,
    setDisplayPicture,
    setTopSongs,
    setAnalytics,
    setTopArtists,
    setRecommendations
}) => {
    const classes = styles();

    useEffect(() => {
        loginUser(setName, setDisplayPicture, setTopSongs, setTopArtists, setAnalytics, setRecommendations);
    }, []);

    return(
    <Box display='flex' flexDirection='column' height='100%' width='100%'>
        <Router>
            <Box pb={8}>
                <AppBar position='fixed' className={classes.appBarStyle}>
                    <Box display='flex' justifyContent='space-around' id='hello'>
                        <Box alignSelf='center'>
                            <Box component={Typography} variant="h6" color='primary' className={classes.typographyStyle} alignSelf='center'>
                                Spotilytics
                            </Box>
                        </Box>
                        <Box display='flex' alignItems='center'>
                            <ul style={{'display':'flex', 'listStyleType': 'none', 'alignItems': 'center'}}>
                                <NavigationOptions/>
                            </ul>
                        </Box>
                    </Box>
                </AppBar>
            </Box>

            <Box>
                <Switch>
                    <Route path="/Dashboard">
                        <Dashboard />
                    </Route>
                    <Route path="/Analytics">
                        <Analytics />
                    </Route>
                    <Route path="/Recommendations">
                        <Recommendations />
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
    setAnalytics,
    setRecommendations
};

export default connect(
    mapStateToProps,
    mapDispatchToProps,
)(Application);
