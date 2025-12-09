//src/components/common/ConfirmationDialog.jsx 

import React from 'react';
import PropTypes from 'prop-types';
import { Box, Typography } from '@mui/material';
import './common.css';

const EmptyState = ({ message }) => {
    return (
        <Box className="empty-state-container">
            <Typography variant="h6" className="empty-state-message">
                {message}
            </Typography>
        </Box>
    );
}

EmptyState.propTypes = {
    message: PropTypes.string.isRequired,
};

export default EmptyState;
