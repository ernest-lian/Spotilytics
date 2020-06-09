import React, { useState } from 'react';
import { connect } from 'react-redux';
import { createStructuredSelector } from 'reselect';
import { map } from 'lodash';
import Modal from 'react-bootstrap/Modal'

import { Box, Typography, TextField, Button } from '@material-ui/core';
import PublishIcon from '@material-ui/icons/Publish';

import { setPlaylistAcknowledge } from '../../actions/rootAction';
import { getRecommendations, getPlaylistAcknowledge } from '../../selectors/rootSelectors';
import TrackDetails from '../tracks/track-details';
import { PALE_PURPLE } from '../../constants/colors'
import { PLAYLIST_MODAL_TITLE, PLAYLIST_MODAL_CLOSE, PLAYLIST_NAME, CREATE } from '../../constants/recommendations'


const TrackRecommendations = ({
    recommendations
}) => {
    return map(recommendations , (trackDetails, index) => {
        const title = trackDetails['title']
        const artist = trackDetails['artist']
        const cover = trackDetails['cover']
        return (
            <Box
                p={2}
                key={index}
            >
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

    return JSON.parse(xhr.response)
}

const Recommendations = ({
    setPlaylistAcknowledge,
    recommendations,
    playlistAcknowledge
}) => {
    const [playlistName, setPlaylistName] = useState('');
    const [show, setShow] = useState(false);
    
    const handlePlaylistName = (currentPlaylistName) => {
        setPlaylistName(currentPlaylistName)
    }

    const submitPlaylistName = () => {
        const response = createPlaylist(playlistName)
        setPlaylistAcknowledge(response['message'])
        setShow(true)
    }

    const handleClose = () => setShow(false);

    return(
        <React.Fragment>
            <Modal
                show={show}
                onHide={handleClose}
                centered
            >
                <Modal.Header closeButton>
                <Modal.Title>
                    {PLAYLIST_MODAL_TITLE}
                </Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    {playlistAcknowledge}
                </Modal.Body>
                <Modal.Footer>
                <Button
                    variant="secondary"
                    onClick={handleClose}
                >
                    {PLAYLIST_MODAL_CLOSE}
                </Button>
                </Modal.Footer>
            </Modal>

            <Box pt={2}>
                <Box
                    component={Typography}
                    variant='h1'
                    textAlign='center'
                    style={{fontWeight: '800'}}
                >
                    Recom{<span style={{'color': 'white'}}>me</span>}ndations
                </Box>
                <Box
                    component={Typography}
                    variant='h6'
                    textAlign='center'
                    pb={5}
                >
                    Here are some songs {<span style={{'color': 'white'}}> you </span>} might vibe with
                </Box>
                <Box
                    display='flex'
                    justifyContent='space-around'
                    bgcolor={PALE_PURPLE}
                >
                    <Box
                        display='flex' 
                        alignSelf='center'
                        flexDirection='column'
                    >
                        <Box
                            component={Typography}
                            variant='h4'
                            textAlign='center'
                            pb={2}
                        >
                            Create {<span style={{'color': 'white'}}> your </span>} own playlist
                        </Box>
                        <TextField 
                            value={playlistName}
                            label={PLAYLIST_NAME}
                            onChange={(e) => handlePlaylistName(e.target.value)}
                            pb={2}
                        />
                        
                        <Button
                            startIcon={<PublishIcon/>}
                            onClick={() => {submitPlaylistName()}}
                        >
                            {CREATE} 
                        </Button>
                    </Box>
                    <Box
                        display='flex'
                        flexDirection='column'
                        height='300px'
                        overflow='scroll'
                        alignItems='flex-end'
                        pt={4}
                    >
                        <TrackRecommendations recommendations={recommendations}/>
                    </Box>
                </Box>
            </Box>
        </React.Fragment>
    );
}

const mapStateToProps = createStructuredSelector({
    recommendations: getRecommendations,
    playlistAcknowledge: getPlaylistAcknowledge
});

const mapDispatchToProps = {
    setPlaylistAcknowledge
};

export default connect(
    mapStateToProps,
    mapDispatchToProps,
)(Recommendations);
