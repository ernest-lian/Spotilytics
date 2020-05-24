// import React, {Component} from 'react';
// import { connect } from 'react-redux'
// import { createStructuredSelector } from 'reselect';

// import { AppBar, Toolbar, Typography, IconButton, Box } from '@material-ui/core';
// import { makeStyles } from '@material-ui/core/styles';

// import AccountCircle from '@material-ui/icons/AccountCircle';
// import MenuIcon from '@material-ui/icons/Menu';

// import blue from '@material-ui/core/colors/blue';

// import { updateCurrentPage } from './actions/rootAction';


// const styles = makeStyles({
//     appBarStyle: {
//         backgroundColor: 'white'
//     },
//     profileButtonStyle: {
//         'padding-right': '50px'
//     },
//     toolBarStyle: {
//         display: 'flex',
//         'justify-content': 'space-between',
//         'flex-wrap': 'wrap'
//     },
//     typographyStyle: {
//         flex: 1,
//         'padding-left': '50px',
//         color: '#FF7E6B'
//     }
// });

// const TopNavigationBar = ({
//     updateCurrentPage
// }) => {
//     const classes = styles();

//     const openUserProfile = () => {
//         console.log('opening the user profile');
//         updateCurrentPage('Profile');
//     }

//     return (
//     <AppBar position='fixed' className={classes.appBarStyle}>
//         <Box display='flex' justifyContent='space-between'>
//             <Box display='flex'>
//                 {/* <Box 
//                     width={56}
//                     color='common.white'
//                     style={{borderRadius: '0%', backgroundColor: '#22031F'}}
//                     display='flex'
//                     justifyContent='center'
//                     alignItems='center' >
//                     <MenuIcon />
//                 </Box> */}
//                 <Box component={Typography} variant="h6" color='primary' className={classes.typographyStyle} alignSelf='center'>
//                     Spotilytics
//                 </Box>
//         </Box>
//         <Toolbar className={classes.toolBarStyle}>
//             {/* <Box className={classes.profileButtonStyle}>
//                 <IconButton color='primary'
//                             onClick={openUserProfile}>
//                     <AccountCircle />
//                 </IconButton>
//             </Box> */}
//         </Toolbar>
//         </Box>
//     </AppBar>);
// }

// const mapStateToProps = createStructuredSelector({

// });

// const mapDispatchToProps = {
//     updateCurrentPage
// };

// export default connect(
//     mapStateToProps,
//     mapDispatchToProps,
// )(TopNavigationBar);
