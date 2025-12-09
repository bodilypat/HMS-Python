//src/components/common/EmptyState.jsx 

import React from 'react';
import PropTypes from 'prop-types';
import './common.css';

const EmptyState = ({ message }) => {
    return (
        <div className="empty-state">
            <p>{message}</p>
        </div>
    );
};
EmptyState.propTypes = {
    message: PropTypes.string.isRequired,
};
export default EmptyState;
