import React from 'react';
import { connect } from 'react-redux'
import { createStructuredSelector } from 'reselect';
import { map } from 'lodash';
import {
    Link
} from "react-router-dom";

import { Box, Typography } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';

import { NAVIGATION_SELECTIONS } from '../../constants/navigation';
import { updateCurrentPage } from '../../actions/rootAction';
import { getCurrentPage } from '../../selectors/rootSelectors';

const styles = makeStyles({
    hoverNavigation: {
        "&:hover": {
            borderBottom: '#FF7E6B solid 3px'
        }
    },
    selectedNavigation: {
        borderBottom: 'burlywood solid 3px'
    },
    typographyStyle: {
        flex: 1,
        'padding-left': '50px',
        color: '#FF7E6B'
    },
    noFontWeight: {
        fontWeight: 100
    }
});

const NavigationOptions = ({
    updateCurrentPage,
    currentPage
}) => {
    const classes = styles();

    const handleCurrentPage = (currentPage) => {
        updateCurrentPage(currentPage)
    }

    return map(NAVIGATION_SELECTIONS, (option) => {
        return (
            <li
                className={(currentPage === option) ? classes.selectedNavigation : classes.hoverNavigation}
                key={option}
                onClick={()=> {handleCurrentPage(option)}}
            >
                <Link
                    style={{'textDecoration': 'none'}}
                    to={'/'+option}
                >
                    <Box
                        component={Typography}
                        variant='h6'
                        color='primary'
                        className={`${classes.typographyStyle} ${classes.noFontWeight}`}
                        alignSelf='center'
                        pt={2}
                    >
                        {option}
                    </Box>
                </Link>
            </li>
        );
    })
}

const mapStateToProps = createStructuredSelector({
    currentPage: getCurrentPage
});

const mapDispatchToProps = {
    updateCurrentPage
};

export default connect(
    mapStateToProps,
    mapDispatchToProps,
)(NavigationOptions);
