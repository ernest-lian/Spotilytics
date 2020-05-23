import React, {Component, useState} from 'react';
import { connect } from 'react-redux'
import { createStructuredSelector } from 'reselect';
import { map } from 'lodash';

/* Material-UI Components */
import { Drawer, IconButton, ListItem, Divider, Box, Typography, Icon} from '@material-ui/core';

/* Material-UI Icons */
import ArrowDropUpIcon from '@material-ui/icons/ArrowDropUp';
import ArrowDropDownIcon from '@material-ui/icons/ArrowDropDown';

import blue from '@material-ui/core/colors/blue';

/* Side Navigation Bar */
import MenuIcon from '@material-ui/icons/Menu';
import DashboardIcon from '@material-ui/icons/Dashboard';
import ShowChartIcon from '@material-ui/icons/ShowChart';
import SearchIcon from '@material-ui/icons/Search';
import { makeStyles } from '@material-ui/core/styles';

/* */
import { updateCurrentPage } from './actions/rootAction';
import { DASHBOARD, ANALYTICS, PREDICTIONS, NAVIGATION_SELECTIONS } from './constants/sideNavigationConstants';

const styles = makeStyles(theme => ({
    listItemStyle: {
        "&:hover": {
            backgroundColor: "blue"
        }
    },
    closedSideNav: {
        transition: theme.transitions.create('width', {
			easing: theme.transitions.easing.sharp,
			duration: theme.transitions.duration.leavingScreen
		}),
		[theme.breakpoints.up('sm')]: {
			width: theme.spacing(7)
		}
    },
    openedSideNav: {
        transition: theme.transitions.create('width', {
			easing: theme.transitions.easing.sharp,
			duration: theme.transitions.duration.enteringScreen
		})
    }
}));

const SIDE_NAV_WIDTH = 230;

const SIDE_NAV_ICONS = {
    [DASHBOARD]: <DashboardIcon/>,
    [ANALYTICS]: <ShowChartIcon/>,
    [PREDICTIONS]: <SearchIcon/>
}

const SideNavigationOptions = ({
    updateCurrentPage
}) => {

    const selectPage = (option) => {
        updateCurrentPage(option);
    }


    return map(NAVIGATION_SELECTIONS, (option) => {
        return (
            <Box key={option}>
                <Divider />
                <ListItem button>
                        <Box display='flex' justifyContent='flex-start' color='common.white'>
                            {SIDE_NAV_ICONS[option]}
                            {console.log('THE OPTION IS: ', option)}
                            <Box component={Typography} pl={2} onClick={() => {selectPage(option)}}>{option}</Box>
                        </Box>
                </ListItem>
                </Box>
        );
    })
};

const SideNavigationBar = ({
    updateCurrentPage
}) => {
    const classes = styles();

    const openSideNav = () => {
        console.log('opening the side nav');
        setIsMenuOpened(true);
    }

    const closeSideNav = () => {
        console.log('closing the side nav');
        setIsMenuOpened(false);
    }

    const [isMenuOpened, setIsMenuOpened] = useState(false);

    return (
        <Drawer
            id='this is the drawer'
            variant='permanent'
            onMouseEnter={openSideNav}
            onMouseLeave={closeSideNav}
        >
            <Box height='100%' bgcolor={'#22031F'}>
                <Box id='drawer2' width={SIDE_NAV_WIDTH} className={isMenuOpened? classes.openedSideNav: classes.closedSideNav}>
                    <Divider />
                    <Box mt={8}>
                        <SideNavigationOptions updateCurrentPage={updateCurrentPage}/>
                    </Box>
                    <Divider />
                </Box>
            </Box>
        </Drawer>
    );
}

const mapStateToProps = createStructuredSelector({

});

const mapDispatchToProps = {
    updateCurrentPage
};

export default connect(
    mapStateToProps,
    mapDispatchToProps,
)(SideNavigationBar);
