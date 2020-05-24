import React from 'react';
import { Box, Typography } from '@material-ui/core';

const TrackDetails = ({
    title,
    artist,
    metricValue,
    metric,
    cover
}) => {
    return(
        <Box display='flex' flexDirection='row' p={2} width='300px' borderRadius='10%' bgcolor='white'>
            <Box component='img' borderRadius='10%' src={cover} width='100px' height='100px' mr={2}/>
            <Box display='flex' flexDirection='column' justifyContent='center'>
                <Box component={Typography} variant='h5'>
                    {title.length >=15 ? title.slice(0,12) + '...' : title}
                </Box>
                <Box component={Typography} variant='h6'>
                    {artist}
                </Box>
                <Box component={Typography} variant='h6'>
                    {(metricValue && metric) ? metricValue + metric : undefined}
                </Box>
            </Box>
        </Box>
    )
}

export default TrackDetails;