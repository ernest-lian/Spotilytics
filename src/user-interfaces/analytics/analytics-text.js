import React from 'react';

import { Box, Typography } from '@material-ui/core';

import { AVERAGE } from '../../constants/analytics'

const ANALYTICS_DIMENSION = '300px'

const AnalyticsText = ({
    average,
    metric,
    metricDescription
}) => {
    return(
        <Box alignSelf='center'>
            <Box
                component={Typography}
                alignSelf='center'
                variant='h1'
                width={ANALYTICS_DIMENSION}
                style={{fontWeight: '800'}}
                color='black'
            >
                {AVERAGE}
            </Box>
            <Box
                component={Typography}
                alignSelf='center'
                variant='h4'
                width={ANALYTICS_DIMENSION}
                style={{fontWeight: '800'}}
                color='black'
            >
                {average + metric}
            </Box>
            <Box
                component={Typography}
                alignSelf='center'
                variant='h6'
                width={ANALYTICS_DIMENSION}
                style={{fontWeight: '100'}}
                color='black'
            >
                {metricDescription}
            </Box>
        </Box>
    );
}

export default AnalyticsText;