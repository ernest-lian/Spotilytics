import React, {Component} from 'react';

import { AppBar, Toolbar, Typography, IconButton, Box } from '@material-ui/core';
import AccountCircle from '@material-ui/icons/AccountCircle';
import { makeStyles } from '@material-ui/core/styles';

const styles = makeStyles({
    appBarStyle: {
        // background : '#2E3B55'
        background: 'linear-gradient(45deg, #0d47a1 10%, #64b5f6 90%)'
    },
    profileButtonStyle: {

    },
    toolBarStyle: {
        display: 'flex',
        'justify-content': 'center',
        'flex-wrap': 'wrap'
    },
    typographyStyle: {
        flex: 1
    }
});

function RenderTopNavigationBar(){
    const classes = styles();
    return (
    <AppBar position='fixed' className={classes.appBarStyle}>
        <Toolbar className={classes.toolBarStyle}>
            <Typography variant="h6" color="inherit" className={classes.typographyStyle}>
              Spotilytics
            </Typography>
            <Box>
                <IconButton color='inherit' className={classes.profileButtonStyle}
                            onClick={()=> {getData();}}>
                    <AccountCircle />
                </IconButton>
            </Box>
        </Toolbar>
    </AppBar>);
}

function getData() {
    // create a new XMLHttpRequest
    var xhr = new XMLHttpRequest()

    // get a callback when the server responds
    xhr.addEventListener('load', () => {
      // update the state of the component with the result here
      console.log(xhr.responseText)
    })
    // open the request with the verb and the url
    xhr.open('GET', 'localhost:5000/dashboard?user_name=testing')
    // send the request
    xhr.send()
}

export class TopNavigationBar extends Component{
    render () {
        return <RenderTopNavigationBar />
    }
}
