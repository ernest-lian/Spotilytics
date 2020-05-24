import React, { useState } from 'react';
import { connect } from 'react-redux';
import { createStructuredSelector } from 'reselect';
import { map } from 'lodash';

import { makeStyles } from '@material-ui/core/styles';
import { Box, Typography, TextField, Button } from '@material-ui/core';

import { getRecommendations } from './selectors/rootSelectors';
import TrackDetails from './trackDetails.js';


const styles = makeStyles({
});

const SongRecommendations = ({
    recommendations
}) => {
    // console.log('inside dashbaord');
    const classes = styles();
    return map(recommendations , (trackDetails) => {
        const title = trackDetails['title']
        const artist = trackDetails['artist']
        const cover = trackDetails['cover']
        return (
            <Box p={2}>
                <TrackDetails title={title} artist={artist} cover={cover}/>
            </Box>
        )
    });
}

function createPlaylist(playlistName) {
    var xhr = new XMLHttpRequest()

    xhr.addEventListener('load', () => {
    })

    xhr.open('POST', 'http://localhost:5000/playlist', false)
    xhr.setRequestHeader('Content-Type', 'application/json; charset=UTF-8')
    xhr.send(JSON.stringify({'playlist_name': playlistName}))

    console.log(JSON.parse(xhr.response))

}

const Recommendations = ({
    recommendations
}) => {
    // console.log('inside dashbaord');
    const [playlistName, setPlaylistName] = useState('');
    
    const handlePlaylistName = (currentPlaylistName) => {
        setPlaylistName(currentPlaylistName)
    }

    const submitPlaylistName = () => {
        createPlaylist(playlistName)
    }

    return(
        <Box pt={2} pr={5}>
            <Box component={Typography} variant='h1' textAlign='center' color='white' style={{fontWeight: '800'}}>
                Recommendations
            </Box>
            <Box component={Typography} variant='h6' textAlign='center' color='white' pb={5}>
                Here are some songs you might {<span style={{'color': '#DCEDC1'}}>vibe</span>} with
            </Box>
            <Box display='flex' justifyContent='space-around'>
                <Box alignSelf='center' display='flex' flexDirection='column'>
                    <TextField value={playlistName} label='Playlist Name' variant='outlined' onChange={(e) => handlePlaylistName(e.target.value)}/>
                    <Button variant="contained" color="primary" onClick={() => {submitPlaylistName()}}>
                        Create Playlist
                    </Button>
                </Box>
                <Box display='flex' flexDirection='column' height='400px' overflow='scroll' alignItems='flex-end' pt={4}>
                    <SongRecommendations recommendations={recommendations}/>
                </Box>
            </Box>
        </Box>
    );
}

const mapStateToProps = createStructuredSelector({
    recommendations: getRecommendations
});

const mapDispatchToProps = {
};

export default connect(
    mapStateToProps,
    mapDispatchToProps,
)(Recommendations);
