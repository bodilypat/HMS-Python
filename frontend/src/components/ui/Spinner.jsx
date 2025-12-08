//components/ui/Spinner.jsx

import React from 'react';
import PropTypes from 'prop-types';
import classNames from 'classnames';
import './ui.css';

/* Spinner Component */

const Spinner = ({ 
    size = 'md', 
    color = 'primary',
    className 
}) => {
    const spinnerClass = classNames(
        'spinner',
        `spinner-${size}`,
        `spinner-${color}`,
        className
    );

    return <div className={spinnerClass} role="status" aria-label="Loading"></div>;
};

Spinner.propTypes = {
    size: PropTypes.oneOf(['sm', 'md', 'lg']),
    color: PropTypes.oneOf(['primary', 'secondary', 'success','warning','danger', 'light','dark']),
    className: PropTypes.string,
};

export default Spinner;

