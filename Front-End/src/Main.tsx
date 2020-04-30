import React, {
  FunctionComponent,
  useState,
  useEffect,
  Component,
} from "react";
import Fullpage from "./FullPage";

import Service from "./components/Pages/01Service";
import Greeting from "./components/Pages/00Greeting";
// import SignUp from "./components/Accounts/04SignUp";
// import Login from "./components/Accounts/03Login";
import MonthlyInput from "./components/Pages/05MonthlyInput";
import DailyInput from "./components/Pages/06DailyInput";
import Information from "./components/UserPage/01Information";
import PriceResult from "./components/UserPage/02PriceResult";
import SelectStore from "./components/UserPage/02PriceResult";
import Recommand from "./components/Store/02Recommand";

import History from "./components/UserPage/03History";
import UserRank from "./components/Pages/Rank/11UserRank";
import KaKaoSignUp from "./components/Accounts/KaKaoSignUp";
import { makeStyles, Container} from '@material-ui/core';
// import ReactDOM from 'react-dom';

// 그리드
import Grid from "@material-ui/core/Grid";
import Box from "@material-ui/core/Box";

import Profile from "./components/UserPage/00ProfileMenu";

const useStlyes = makeStyles(theme => ({

  content:{
    alignItems:''
  },

  hambuger: {
    position:'relative',
    // right : '20px',
    // top : '20px',
    // zIndex:-1,
  },
}))

const Main: FunctionComponent<any> = ({}) => {
  const [checkResult, setCheckResult] = useState(true as boolean);
  const classes = useStlyes();
  // useEffect(() => setCheckResult(props_data), )

  return (
    <>

      <Box display="flex" justifyContent="flex-end" m={1} p={1}>

        <Fullpage />

      </Box>
    </>

  //  <Container >
  //     {/* <Grid>  */}
  //     {/* // display="flex" justifyContent="flex-end" m={1} p={1}> */}
  //     <Grid className={classes.hambuger} >
  //       <Profile   />
  //     </Grid>
  //     {/* </Box> */}
 
  //     <Grid> 
  //     {/* // display="flex" justifyContent="center" alignItems="center"> */}
  //       <Fullpage/>
  //     </Grid>

  //   </Container>
  //   </>
  );
};

export default Main;
