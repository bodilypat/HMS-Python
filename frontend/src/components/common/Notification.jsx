//src/components/common/Notification.jsx

import React from 'react';
import PropTypes from 'prop-types';
import { Box, Typography } from '@mui/material';

const EmptyState = ({ message }) => {
    return (
        <Box
            display="flex"
            flexDirection="column"
            alignItems="center"
            justifyContent="center"
            height="100%"
            textAlign="center"
            padding={4}
        >
            <Typography variant="h6" color="textSecondary">
                {message}
            </Typography>
        </Box>
    );
}

EmptyState.propTypes = {
    message: PropTypes.string.isRequired,
};

export default EmptyState;

