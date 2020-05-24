// import React, {Component, useState} from 'react';
// import { connect } from 'react-redux'
// import { createStructuredSelector } from 'reselect';

// import { Box, Typography, Button } from '@material-ui/core';

// import { getName, getDisplayPicture } from '../selectors/rootSelectors';

// const Profile = ({
//     name,
//     displayPicture
// }) => {
//     return (
//         <Box id='box-4' display='flex' alignItems='center' justifyContent='center'>
//             <Box component='img' src={displayPicture} width='100px' height='100px' borderRadius='50%'>

//             </Box>
//             <Typography component="div">
//                 <Box fontWeight="fontWeightLight" ml={2}>
//                     User
//                 </Box>
//                 <Box fontWeight="fontWeightBold" fontSize={40} ml={2}>
//                     {name}
//                 </Box>
//             </Typography>
//         </Box>
//     );
// }

// const mapStateToProps = createStructuredSelector({
//     name: getName,
//     displayPicture: getDisplayPicture
// });

// const mapDispatchToProps = {
// };

// export default connect(
//     mapStateToProps,
//     mapDispatchToProps,
// )(Profile)