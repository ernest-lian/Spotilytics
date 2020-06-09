import React from 'react';
import { connect } from 'react-redux'
import { createStructuredSelector } from 'reselect';
import { map } from 'lodash';

import { Box, Typography, Fade } from '@material-ui/core';
import { getTopSongs } from '../../selectors/rootSelectors';

const MostPlayed = ({
    topSong
}) => {
    const title = topSong['title']
    const artist = topSong['artist']
    const cover = topSong['cover']
    return (
        <Box
            display='flex'
            flexDirection='row'
            alignItems='center'
            justifyContent='center'
            pt={8}
            pb={8}
        >
            <Box
                pr={8}
                textAlign='center'
            >
                <Box
                    component={Typography}
                    variant='h3'
                    color='white'
                    style={{fontWeight: '800'}}
                >
                    You love {<span style={{'color': 'black'}}>{title}</span>}
                </Box>
                <Box
                    component={Typography}
                    variant='h6'
                    color='white'
                >
                    This song by {<span style={{'color': 'black'}}>{artist}</span>} is your most played song
                </Box>
            </Box>
            <Box
                component='img'
                borderRadius='10%'
                src={cover}
                width='300px'
                height='300px'
            />
        </Box>
    )
}

const TrackOptions = ({
    topSongs
}) => {

    return map(topSongs , (songDetails, index) => {
        const title = songDetails['title']
        const artist = songDetails['artist']
        const cover = songDetails['cover']

        return(
            <Box
                key={index}
                display='flex'
                flexDirection='row'
                width='450px'
                p={4}
            >
                <Box
                    component='img'
                    borderRadius='10%'
                    src={cover}
                    width='100px'
                    height='100px'
                    mr={2}
                />
                <Box
                    component={Typography}
                    display='flex'
                    alignItems='center'
                    variant='h1'
                >
                    {index+2}
                </Box>
                <Box
                    display='flex'
                    flexDirection='column'
                    justifyContent='center'
                    ml={2}
                >
                    <Box
                        component={Typography}
                        variant='h5'
                        color='white'
                    >
                        {title.length >=15 ? title.slice(0,12) + '...' : title}
                    </Box>
                    <Box
                        component={Typography}
                        variant='h6'
                    >
                        {artist}
                    </Box>
                </Box>
            </Box>
        );
    })
};


const Track = ({
    topSongs
}) => {
    return (
        <Box display='flex' flexDirection='column' pt={2} bgcolor='bisque'>
            <MostPlayed topSong={topSongs[0]}/>
            <Box display='flex' justifyContent='center' flexWrap='wrap'>
                <TrackOptions topSongs={topSongs.slice(1,6)}/>
            </Box>
        </Box>
    );
}

const mapStateToProps = createStructuredSelector({
    topSongs: getTopSongs
});

const mapDispatchToProps = {
};

export default connect(
    mapStateToProps,
    mapDispatchToProps,
)(Track);
