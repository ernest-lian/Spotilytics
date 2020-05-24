// import React, { Component, useState } from 'react'
// import axios from 'axios'

// import { makeStyles } from '@material-ui/core/styles';
// import Card from '@material-ui/core/Card';
// import CardActions from '@material-ui/core/CardActions';
// import CardContent from '@material-ui/core/CardContent';
// import Button from '@material-ui/core/Button';
// import Typography from '@material-ui/core/Typography';
// import { TextField, Box } from '@material-ui/core'
// import PersonIcon from '@material-ui/icons/Person';
// import InputAdornment from '@material-ui/core/InputAdornment';
// import AccountCircle from '@material-ui/icons/AccountCircle';
// import blue from '@material-ui/core/colors/blue';

// import Dashboard from '../dashboard'


// const useStyles = makeStyles({
//   card: {
//     minWidth: 400,
//   },
//   pos: {
//     marginBottom: 12,
//   },
//   columnFlexDirection: {
//     display: 'flex',
//     'flex-direction': 'column'
//   },
//   darkBlueBackground: {
//     // background: 'linear-gradient(45deg, #0d47a1 10%, #64b5f6 90%)',
//     minWidth: 170
//   },
//   whiteFontColor: {
//     color: 'white'
//   },
//   lightBlueBackground: {
//     backgroundColor: blue[600]
//   },
//   justifyContentCentre: {
//     'justify-content': 'center'
//   },
//   robotoLight: {
//     'font-family': 'Roboto-Light'
//   },
//   smallFontSize: {
//     'font-size': '10px'
//   },
//   largeFontSize: {
//     'font-size': '30px'
//   },
//   bold: {
//     'font-weight': 'bold'
//   },
//   maxWidth: {
//     width: '90%'
//   },
//   smallWidth: {
//     width: '40%'
//   },
//   borderRadius: {
//     'border-radius': '10px'
//   }
// });


// const RenderRegister = ({


// }) => {
//     const classes = useStyles();
//     const [firstName, setFirstName] = useState("");
//     const [lastName, setLastName] = useState("");
//     const [userName, setUserName] = useState("");
//     const [userPassword, setUserPassword] = useState("");
//     const [register, setRegister] = useState(true);

//     const setRegisterValue = value => {
//       console.log("Setting register value: ", value);
//       setRegister(value);
//     }

//     const submitRegistration = () => {
//       console.log("Submitting registration");
//       console.log(`the firstName is: ${firstName}`);
//       console.log(`the lastName is: ${lastName}`);
//       console.log(`the userName is: ${userName}`);
//       console.log(`the userPassword is: ${userPassword}`);

//       axios({
//         method: 'post',
//         url: 'http://localhost:5000/register',
//         data: {
//           firstName, lastName, userName, userPassword
//         },
//         headers: {
//           'Access-Control-Allow-Origin': '*'
//         }
//       }).then((response) => {
//         if (response['status'] === 200){
//           setRegister(false);
//           console.log('the response is 200');
//           // Render the dashboard
//         }
//       });
//     }

//     const submitLogin = () => {
//       console.log('submitLogin: ');
//       return <Dashboard />
//     };

//     return (
//         <Box id='cardbox' height='75%' display='flex' justifyContent='center'>
//           <Card className={classes.card} >
//             <CardContent>
//               <Box
//                 pt={2}
//                 display='flex'
//                 justifyContent='center'
//               >
//                 <Typography variant='h5' className={classes.bold}> {register? 'Sign Up' : 'Sign In'} </Typography>
//               </Box>
//               <form className={classes.columnFlexDirection} noValidate autoComplete="off">
//                 {register ? <Box p={2} id='thebox' display='flex' justifyContent='center'>
//                   <TextField className={classes.maxWidth} onChange={(event) => setFirstName(event.target.value)} id="standard-basic" label="First Name" />
//                 </Box>
//                 : null}

//                 {register ? <Box p={2} display='flex' justifyContent='center'>
//                   <TextField className={classes.maxWidth} onChange={(event) => setLastName(event.target.value)} id="standard-basic" label="Last Name" />
//                 </Box>
//                 : null}

//                 <Box p={2} display='flex' justifyContent='center'>
//                   <TextField className={classes.maxWidth} onChange={(event) => setUserName(event.target.value)} id="standard-basic" label="Username"/>
//                 </Box>

//                 <Box p={2} display='flex' justifyContent='center'>
//                   <TextField className={classes.maxWidth} onChange={(event) => setUserPassword(event.target.value)} id="standard-basic" type='password' label="Password" />
//                 </Box>
//               </form>
//             </CardContent>
            
//             <CardActions className={classes.justifyContentCentre}>
//               <Box display='flex' flexDirection='column'>
//                 <Box display='flex' justifyContent='center'>
//                   <Button className={`${classes.borderRadius} ${classes.darkBlueBackground} ${classes.smallWidth} ${classes.whiteFontColor} ${classes.smallFontSize}`} onClick={register? submitRegistration : submitLogin} >{register ? 'Create Account' : 'Log In'}</Button>
//                 </Box>
//                 <Box pt={2}display='flex' justifyContent='center'>
//                   <Box pt={0.5}>
//                     <Typography className={classes.smallFontSize}>Already have an account?</Typography>
//                   </Box>
//                   <Button id='signinbutton' size='small' className={classes.smallFontSize} onClick={() => {setRegisterValue(!register)}}>{register ? 'Sign In' : 'Sign Up'}</Button>
//                 </Box>
//               </Box>
//             </CardActions>
//         </Card>
//         </Box>
//     );
// }

// export default RenderRegister;
