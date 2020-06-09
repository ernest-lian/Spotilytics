import React from 'react';
import { connect } from 'react-redux'
import { createStructuredSelector } from 'reselect';
import { map } from 'lodash';

import { Box, Typography } from '@material-ui/core';
import { getTopArtists } from '../../selectors/rootSelectors';
import { YELLOW } from '../../constants/colors'
import { ARTIST_DESCRIPTION } from '../../constants/dashboard';


const MostPlayed = ({
    topArtist
}) => {
    const profile = topArtist['profile']
    const name = topArtist['name']

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
                    You are {<span style={{'color': YELLOW}}>{name}</span>}'s #1 fan
                </Box>
                <Box
                    component={Typography}
                    variant='h6'
                    color='white'
                >
                    {ARTIST_DESCRIPTION}
                </Box>
            </Box>
            <Box
                component='img'
                borderRadius='10%'
                src={profile}
                width='400px'
                height='400px'
            />
        </Box>
    )
}

const ArtistsOptions = ({
    topArtists
}) => {
    return map(topArtists , (artistDetails, index) => {
        const profile = artistDetails['profile']
        const name = artistDetails['name']
        const dimension = (350 / (index+1))+'px'
        return(
            <Box
                key={index}
                display='flex'
            >
                <Box
                    component={Typography}
                    variant='h5'
                    color='white'
                    pr={2}
                >
                    {index+2}
                </Box>
                <Box>
                    <Box
                        component='img'
                        borderRadius='10%'
                        src={profile}
                        width={dimension}
                        height={dimension}
                        mr={2}
                    />
                    <Box
                        component={Typography}
                        variant='h5'
                        color='white'
                    >
                        {name}
                    </Box>
                </Box>
            </Box>
        )
    });
}


const Artists = ({
    topArtists  
}) => {
    return (
        <Box display='flex' flexDirection='column' pb={4} bgcolor='#5D250F'>

            <MostPlayed topArtist={topArtists[0]}/>
            <Box display='flex' justifyContent='center' flexWrap='wrap'>
                <ArtistsOptions topArtists={topArtists.slice(1,6)}/>
            </Box>
        </Box>
    );
}

const mapStateToProps = createStructuredSelector({
    topArtists: getTopArtists
});

const mapDispatchToProps = {
};

export default connect(
    mapStateToProps,
    mapDispatchToProps,
)(Artists);
