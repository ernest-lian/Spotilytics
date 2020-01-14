import React, {Component} from 'react';

import { AppBar, Toolbar, Typography, IconButton, Box, Drawer } from '@material-ui/core';
import AccountCircle from '@material-ui/icons/AccountCircle';
import { makeStyles } from '@material-ui/core/styles';

/* Side Navigation Bar */
import MenuIcon from '@material-ui/icons/Menu';
import DashboardIcon from '@material-ui/icons/Dashboard';
import ShowChartIcon from '@material-ui/icons/ShowChart';
import SearchIcon from '@material-ui/icons/Search';

const styles = {
    appBarStyle: {
        background : '#2E3B55'
    },
    profileButtonStyle: {
        align: 'center'
    },
    drawerStyle: {
        background: "blue"
    }
};

const element = (
    <div>
    <AppBar position='static' style={styles['appBarStyle']}>
        <Toolbar>
            <Typography variant="h6" color="inherit">
              Spotilytics
            </Typography>
            <Box>
                <IconButton color='inherit' style={styles['profileButtonStyle']}>
                    <AccountCircle />
                </IconButton>
            </Box>
        </Toolbar>
    </AppBar>
        <Drawer variant="persistent"
            anchor="left"
            open={open}
        >
            <IconButton>
                <MenuIcon />
            </IconButton>
            <IconButton>
                <DashboardIcon />
            </IconButton>
            <IconButton>
                <ShowChartIcon />
            </IconButton>
            <IconButton>
                <SearchIcon />
            </IconButton>
        </Drawer>
    </div>
)

export class TopNavigationBar extends Component{
    render () {
        return element
    }
}
