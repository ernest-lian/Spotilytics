import React from 'react';
import { connect } from 'react-redux'
import { createStructuredSelector } from 'reselect';
import Typist from 'react-typist';
import { map } from 'lodash';

import { Box, Typography } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';

import { getAnalytics } from './selectors/rootSelectors';
import TrackDetails from './trackDetails.js';

const styles = makeStyles({
    '@keyframes slide': {
        from: {backgroundPosition: '0 0'},
        to: {backgroundPosition: '-50000px 0'}
    },
    '@keyframes slidel': {
        from: {backgroundPosition: '0 0'},
        to: {backgroundPosition: '50000px 0'}
    },
    slideRight: {
        animationName: '$slide',
        animationDuration: '1000s',
        animationTimingFunction: 'linear',
        animationIterationCount: 'infinite'
    },
    slideLeft: {
        animationName: '$slidel',
        animationDuration: '1000s',
        animationTimingFunction: 'linear',
        animationIterationCount: 'infinite'
    },
    hoverAnalytic: {
        "&:hover": {
            animationName: '$slidel',
            animationDuration: '1000s',
            animationTimingFunction: 'linear',
            animationIterationCount: 'infinite'
        }
    }
});

const AnalyticsText = ({
    average,
    metric
}) => {
    return(
        <Box alignSelf='center'>
            <Box component={Typography} variant='h3' width='300px' alignSelf='center' style={{fontWeight: '800'}} color='black'>
                {average + metric}
            </Box>
            <Box component={Typography} variant='h6' width='300px' alignSelf='center' color='black'>
                The perceptual measure of intensity and activity
            </Box>
        </Box>
    );
}

const AnalyticsOption = ({
    analytics
}) => {
    const classes = styles();

    // const color = {'energetic_track': '#DCEDC1', 'fastest_track': '#FFD3B6', 'longest_track': '#FFAAA5'}
    const metric = {'energetic_track': ' % Energy', 'fastest_track': ' bpm', 'longest_track': ' ms', 'popular_track': '% Popularity'}
    const value = {'energetic_track': 'energy', 'fastest_track': 'speed', 'longest_track': 'duration', 'popular_track': 'popular'}
    // const title = {'energetic_track': 'Your Energetic Track', 'fastest_track': 'Your Fastest Track', 'longest_track': 'Your Longest Track'}
    return map(analytics, (analyticDetails, index) => {
        console.log('analyticDetails: ', analyticDetails);
        const title = analyticDetails['title']
        const artist = analyticDetails['artist']
        const average = analyticDetails['average']
        const cover = analyticDetails['cover']
        const metricValue = analyticDetails[value[index]]
        
        console.log('color[index]: ', metric)
        console.log('index: ', index)
        return(
            <Box bgcolor='#A8E6CF' pt={2}>
                <Box pl={4} pt={4} pb={4} display='flex' justifyContent='center' style={{background: `linear-gradient(rgba(255,255,255,.8), rgba(255,255,255,.8)), url(${cover})`, backgroundSize: 'contain'}}>
                    {index === ('fastest_track' || 'popular_track') ? <AnalyticsText average={average} metric={metric[index]}/>: null }
                    <Box>
                        <Box component={Typography} variant='h5' textAlign='center'>
                            {title[index]}
                        </Box>
                        {/* <Box display='flex' flexDirection='row' p={2} width='300px' borderRadius='10%' bgcolor='white'> */}
                        <TrackDetails title={title} artist={artist} metricValue={metricValue} metric={metric[index]} cover={cover}/>
                        {/* </Box> */}
                    </Box>
                    {index !== ('fastest_track' || 'popular_track') ? 
                            <AnalyticsText average={average} metric={metric[index]}/>
                        : null }
                </Box>
        </Box>);
    })
}


const Analytics = ({
    analytics
}) => {
    const classes = styles();

    console.log('Inside analytics');
    console.log(analytics);
    return (
        <Box>
            <Box bgcolor='#A8E6CF' pt={12} pb={4} textAlign='center'>
                <Typist cursor={{show: false}}>
                    <Box component={Typography} variant='h3' color='black' style={{fontWeight: '800'}}>
                        Lets {<span style={{'color': 'white'}}>analyze</span>} deeper
                    </Box>
                </Typist>
                <Typist cursor={{show: false}}>
                    <Box component={Typography} variant='h6' color='black'>
                        Here are some analytics on songs you recently listened to
                    </Box>
                </Typist>
            </Box>
            <AnalyticsOption analytics={analytics}/>
        </Box>
    );
}

const mapStateToProps = createStructuredSelector({
    analytics: getAnalytics
});

const mapDispatchToProps = {
};

export default connect(
    mapStateToProps,
    mapDispatchToProps,
)(Analytics);
