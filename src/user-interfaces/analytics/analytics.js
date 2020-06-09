import React from 'react';
import { connect } from 'react-redux'
import { createStructuredSelector } from 'reselect';
import Typist from 'react-typist';
import { map } from 'lodash';

import { Box, Typography } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';

import { getAnalytics } from '../../selectors/rootSelectors';
import TrackDetails from '../tracks/track-details.js';
import AnalyticsText from './analytics-text.js';

import { METRICS, TRACK_HEADER, SECTION_TITLE, METRIC_TYPE, METRIC_DESCRIPTION, ANALYTICS_DESCRIPTION } from '../../constants/analytics';
import { MAGIC_MINT, WILLOW_BROOK, PALE_ORANGE, SEA_MIST } from '../../constants/colors'

const styles = makeStyles({
    '@keyframes slide': {
        from: {backgroundPosition: '0 0'},
        to: {backgroundPosition: '-50000px 0'}
    },
    '@keyframes slidel': {
        from: {backgroundPosition: '0 0'},
        to: {backgroundPosition: '50000px 0'}
    },
    slideLeft: {
        animationName: '$slidel',
        animationDuration: '1000s',
        animationTimingFunction: 'linear',
        animationIterationCount: 'infinite'
    }
});

const AnalyticsOption = ({
    analytics
}) => {
    const classes = styles();
    const color = {'energetic_track': WILLOW_BROOK, 'fastest_track': PALE_ORANGE, 'longest_track': SEA_MIST}  

    return map(analytics, (analyticDetails, index) => {
        const title = analyticDetails['title']
        const artist = analyticDetails['artist']
        const average = analyticDetails['average']
        const cover = analyticDetails['cover']
        const metricValue = analyticDetails[METRIC_TYPE[index]]
        const analyticsText = <AnalyticsText average={average} metric={METRICS[index]} metricDescription={METRIC_DESCRIPTION[index]}/>
        
        return(
            <Box
                bgcolor={color[index]}
                pt={2}
                key={index}
            >
                <Box
                    component={Typography}
                    variant='h2'
                    textAlign='center'
                    style={{fontWeight: '800'}}
                    color='white'
                    pb={2}
                >
                    {SECTION_TITLE[index]}
                </Box>
                <Box 
                    display='flex'
                    justifyContent='space-around'
                    className={classes.slideLeft}
                    style={{background: `linear-gradient(rgba(255,255,255,.8), rgba(255,255,255,.8)), url(${cover})`}}
                    pl={4}
                    pt={4}
                    pb={4} 
                >
                    {['fastest_track', 'popular_track'].indexOf(index) >= 0 ? analyticsText : null }
                    <Box>
                        <Box
                            component={Typography}
                            variant='h5'
                            textAlign='center'
                            style={{fontWeight: '500'}}
                        >
                            {TRACK_HEADER[index]}
                        </Box>
                        <TrackDetails
                            title={title}
                            artist={artist}
                            metricValue={metricValue}
                            metric={METRICS[index]}
                            cover={cover}
                        />
                    </Box>
                    {['energetic_track', 'longest_track'].indexOf(index) >= 0 ? analyticsText : null }
                </Box>
        </Box>);
    })
}


const Analytics = ({
    analytics
}) => {
    const classes = styles();

    return (
        <Box>
            <Box bgcolor={MAGIC_MINT} pt={12} pb={4} textAlign='center'>
                <Typist cursor={{show: false}}>
                    <Box component={Typography} variant='h3' color='black' style={{fontWeight: '800'}}>
                        Lets {<span style={{'color': 'white'}}>analyze</span>} deeper
                    </Box>
                </Typist>
                <Typist cursor={{show: false}}>
                    <Box component={Typography} variant='h6' color='black'>
                        {ANALYTICS_DESCRIPTION}
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
