import React, {useEffect, useState} from 'react';
import { connect } from 'react-redux'
import { createStructuredSelector } from 'reselect';
import {
    BrowserRouter as Router,
    Switch,
    Route
  } from "react-router-dom";
import Spinner from 'react-bootstrap/Spinner'

import { Box, Typography, AppBar } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';

import Dashboard from './dashboard/dashboard.js';
import Analytics from './analytics/analytics.js';
import Recommendations from './recommendations/recommendations.js';
import NavigationOptions from './navigation/navigation-options.js';

import { setName, setDisplayPicture, setTopSongs, setTopArtists, setAnalytics, setRecommendations, updateCurrentPage, setErrorMessage } from '../actions/rootAction';
import { getDisplayPicture, getCurrentPage, getErrorMessage } from '../selectors/rootSelectors';
import { SPOTILYTICS } from '../constants/navigation'


const styles = makeStyles({
    appBarStyle: {
        backgroundColor: 'white',
        paddingBottom: '20px'
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

const Application = ({
    setName,
    setDisplayPicture,
    setTopSongs,
    setAnalytics,
    setTopArtists,
    setRecommendations,
    setErrorMessage,
    displayPicture,
    errorMessage
}) => {
    const classes = styles();

    const [loading, setLoading] = useState(true);

    const loginUser = (setName, setDisplayPicture, setTopSongs, setTopArtists, setAnalytics, setRecommendations, setErrorMessage) => {
        var xhr = new XMLHttpRequest()
    
        xhr.addEventListener('load', () => {
        })
    
        xhr.open('POST', 'http://localhost:5000/login', false)
        xhr.send()
        
        const responseBody = JSON.parse(xhr.response)

        if (responseBody['response'] === 200){
            const name = responseBody['body']['name']
            const displayPicture = responseBody['body']['display_picture']
            const topSongs = responseBody['body']['top_tracks'].splice(0,5)
            const topArtists = responseBody['body']['top_artists']
            const analytics = responseBody['body']['analytics']
            const recommendations = responseBody['body']['recommendations']
        
            setDisplayPicture(displayPicture)
            setName(name)
            setTopSongs(topSongs)
            setTopArtists(topArtists)
            setAnalytics(analytics)
            setRecommendations(recommendations)
            setLoading(false)
        } else {
            const errorMessage = responseBody['error']
            setErrorMessage(errorMessage)
        }
    }

    useEffect(() => {
        loginUser(setName, setDisplayPicture, setTopSongs, setTopArtists, setAnalytics, setRecommendations, setErrorMessage);
    }, []);

    return(
    <Box
        display='flex'
        flexDirection='column'
        height='100%'
        width='100%'
    >
        <Router>
            <Box
                pb={10}
            >
                <AppBar
                    position='fixed'
                    className={classes.appBarStyle}
                >
                    <Box
                        display='flex'
                        justifyContent='space-around'
                        alignItems='center'
                    >
                        <Box
                            alignSelf='center'
                        >
                            <Box
                                component={Typography}
                                variant="h5"
                                color='primary'
                                className={classes.typographyStyle}
                                alignSelf='center'
                            >
                                {SPOTILYTICS}
                            </Box>
                        </Box>
                        <Box
                            display='flex'
                            alignItems='center'
                        >
                            <ul
                                style={{'display':'flex', 'listStyleType': 'none', 'alignItems': 'center'}}
                            >
                                <NavigationOptions/>
                            </ul>
                        </Box>
                        <Box
                            component='img'
                            width='40px'
                            height='40px'
                            borderRadius='50%'
                            src={displayPicture}
                            style={{objectFit: 'cover'}}/>
                    </Box>
                </AppBar>
            </Box>

            <Box>
                <Switch>
                    <Route path="/dashboard">
                        <Dashboard />
                    </Route>
                    <Route path="/analytics">
                        <Analytics />
                    </Route>
                    <Route path="/recommendations">
                        <Recommendations />
                    </Route>
                    <Route path="/">
                        {loading ? 
                        <Box
                            textAlign='center'
                            paddingTop='20%'
                        >
                            <Spinner animation="border" variant="dark"/>
                            <Box
                                component={Typography}
                            >
                                {errorMessage}
                            </Box>
                        </Box>
                        : null}
                    </Route>
                </Switch>
            </Box>
        </Router>
    </Box>);
}

const mapStateToProps = createStructuredSelector({
    displayPicture: getDisplayPicture,
    currentPage: getCurrentPage,
    errorMessage: getErrorMessage
});

const mapDispatchToProps = {
    setName,
    setDisplayPicture,
    setTopSongs,
    setTopArtists,
    setAnalytics,
    setRecommendations,
    setErrorMessage,
    updateCurrentPage
};

export default connect(
    mapStateToProps,
    mapDispatchToProps,
)(Application);
