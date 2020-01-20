import React, {Component, useState} from 'react';

import { Drawer, IconButton, ListItem, Divider } from '@material-ui/core';
            
/* Side Navigation Bar */
import MenuIcon from '@material-ui/icons/Menu';
import DashboardIcon from '@material-ui/icons/Dashboard';
import ShowChartIcon from '@material-ui/icons/ShowChart';
import SearchIcon from '@material-ui/icons/Search';
import { makeStyles } from '@material-ui/core/styles';

const styles = makeStyles({
    listItemStyle: {
        "&:hover": {
            backgroundColor: "blue"
        }
    }
});


function RenderSideNavigationBar(){
    const classes = styles();

    const [selectedIndex, setSelectedIndex] = useState(0);
    return (
    <Drawer variant="persistent"
        anchor="left"
        open={open}
    >
        <Divider />
        <ListItem selected={selectedIndex===0} button onClick={() => {setSelectedIndex(0);}}>
            <DashboardIcon />
        </ListItem>
        <Divider />
        <ListItem button selected={selectedIndex===1} className={styles.listItemStyle} onClick={() => {setSelectedIndex(1);}}>
            <ShowChartIcon />
        </ListItem>
        <Divider />
        <ListItem button selected={selectedIndex===2} onClick={() => {setSelectedIndex(2);}}>
            <SearchIcon />
        </ListItem>
        <Divider />
    </Drawer>);
}

export class SideNavigationBar extends Component{
    render () {
        return <RenderSideNavigationBar />
    }
}