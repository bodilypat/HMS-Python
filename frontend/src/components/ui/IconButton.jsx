//src/components/ui/IconButton.jsx 

import React from 'react';
import PropTypes from 'prop-types';
import classNames from 'classnames';
import './ui.css';

/* IconButton Component */
const IconButton = ({ 
    icon,
    variant = 'primary',
    size = 'md',
    disabled = false,
    onClick,
    className,
    disabled 
}) => {
    const btnClass = classNames(
        'icon-button',
        `icon-button--${variant}`,
        `icon-button--${size}`,
        { 'icon-button--disabled': disabled },
        className
    );
    return (
        <button className={btnClass} onClick={onClick} disabled={disabled}>
            <span className="icon-button__icon">
                {icon}
            </span>
        </button>
    );
};
IconButton.propTypes = {
    icon: PropTypes.node.isRequired,
    variant: PropTypes.oneOf(['primary', 'secondary', 'tertiary']),
    size: PropTypes.oneOf(['sm', 'md', 'lg']),
    disabled: PropTypes.bool,
    onClick: PropTypes.func,
    className: PropTypes.string,
};


