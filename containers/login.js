import React, {Component} from 'react';


import { Box, Typography } from '@material-ui/core';

import { makeStyles } from '@material-ui/core/styles';


const styles = makeStyles({
    loginBoxStyle: {
        background: 'linear-gradient(45deg, #0d47a1 10%, #64b5f6 90%)',
        display: 'flex',
        justifyContent: 'center',
        borderColor: 'text.primary',
        m: 1,
        border: 1,
        style: { width: '5rem', height: '5rem' }
    }
});

function RenderLogin(){
    const classes = styles();
    return (
        <Box className={classes.loginBoxStyle}>
            <Typography variant="h6" color="inherit" className={classes.typographyStyle}>
              Spotilytics
            </Typography>
        </Box>
    );
}

export class Login extends Component {
    render () {
        return <RenderLogin />
    }
}