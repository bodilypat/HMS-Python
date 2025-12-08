//components/ui/Badge.jsx 

import React from 'react';
import PropTypes from 'prop-types';
import classNames from 'classnames';
import './ui.css';

/* Badge Component */
const Badge = ({ children, variant = 'primary', size = 'md', dot = false, className = '' }) => {
    const baseClasses = 'inline-flex items-center font-medium rounded-full';

    const variantClasses = {
        primary: 'bg-blue-100 text-blue-800',
        secondary: 'bg-gray-100 text-gray-800',
        success: 'bg-green-100 text-green-800',
        danger: 'bg-red-100 text-red-800',
        warning: 'bg-yellow-100 text-yellow-800',
        info: 'bg-teal-100 text-teal-800',
        error: 'bg-red-100 text-red-800',
    };

    const sizeClasses = {
        sm: 'text-xs px-2 py-1',
        md: 'text-sm px-3 py-1.5',
        lg: 'text-base px-4 py-2',
    };

    return (
        <span 
            className={classNames(
                baseClasses, 
                variantClasses[variant], 
                sizeClasses[size],
                dot && 'rounded-full',
                className
            )}
        >
            {dot && children}
        </span>
        );
    };
    
    Badge.prototype = {
    children: PropTypes.node.isRequired,
    variant: PropTypes.oneOf(['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'error']),
    size: PropTypes.oneOf(['sm', 'md', 'lg']),
    dot: PropTypes.bool,
    className: PropTypes.string,    
};
export default Badge;
