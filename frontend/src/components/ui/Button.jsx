/* components/ui/Button.jsx */ 

import React from 'react';
import PropTypes from 'prop-types';
import classNames from 'classnames';
import './ui.css';

/* Button Component */
const Button = ({ 
    children, 
    variant = 'primary', 
    size = 'md',
    disabled = false,
    loading = false,
    onClick,
    className, 
    disabled
 }) => {
    const btbClasses = classNames(
        'btn',
        `btn-${variant}`,
        `btn-${size}`,
        { 'btn-disabled': disabled || loading },
        className
    );

    return (
        <button
            className={btnClasses}
            onClick={onClick}
            disabled={disabled || loading}
            {...rest}
        >
            {loading && <span className="btn-spinner" />}
            {icon && <span className="btn-icon">{icon}</span>
            {span className="btn-text">{children}</span>
        </button>
    );
};

Button.propTypes = {
    children: PropTypes.node.isRequired,
    variant: PropTypes.oneOf(['primary', 'secondary', 'danger', 'link']),
    size: PropTypes.oneOf(['sm', 'md', 'lg']),
    disabled: PropTypes.bool,
    loading: PropTypes.bool,
    onClick: PropTypes.func,
    className: PropTypes.string,
    icon: PropTypes.node,
};
export default Button;


