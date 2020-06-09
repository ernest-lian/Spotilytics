import React from 'react';
import { connect } from 'react-redux';
import { createStructuredSelector } from 'reselect';

import { Box, Typography, Button } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import blue from '@material-ui/core/colors/blue';

import Track from '../tracks/track'
import Artists from '../artists/artists'

import { getName, getDisplayPicture } from '../../selectors/rootSelectors';


const Dashboard = ({
    name,
    displayPicture
}) => {
    return (
        <Box>
            <Box
                display='flex'
                alignItems='center'
                justifyContent='center'
                pt={12}
                pb={12}
            >
                <Box
                    component='img'
                    style={{'objectFit': 'cover'}}
                    src={displayPicture}
                    width='200px'
                    height='200px'
                    border='3px solid white'
                    borderRadius='50%'
                />
                <Typography
                    component='div'
                    color={blue[900]}
                >
                    <Box
                        fontWeight='fontWeightLight'
                        ml={2}
                    >
                        User
                    </Box>
                    <Box
                        fontWeight="fontWeightBold"
                        fontSize={40}
                        ml={2}
                    >
                        {name}
                    </Box>
                </Typography>
            </Box>
            <Track />
            <Artists />
        </Box>
    );
}

const mapStateToProps = createStructuredSelector({
    name: getName,
    displayPicture: getDisplayPicture
});

const mapDispatchToProps = {
};

export default connect(
    mapStateToProps,
    mapDispatchToProps,
)(Dashboard);
