// components/ui/Alert.jsx 
import React from 'react';
import PropTypes from 'prop-types';
import classNames from 'classnames';
import './ui.css';

const Alert = ({ 
    vaariant = 'info',
    title,
    message,
    icon,
    closable = false,
    onClose,
    className
}) => {
    const alertClasses = classNames(
        'alert',
        `alert-${vaariant}`,
        className
    );

    return (
        <div className={alertClasses} role="alert">
            {icon && <span className="alert-icon">{icon}</span>}
            <div className="alert-content">
                {title && <h4 className="alert-title">{title}</h4>}
                {message && <p className="alert-message">{message}</p>}
            </div>
            {closable && (
                <button 
                    className="alert-close" onClick={onClose} aria-label="Close alert">×</button>
            )}
        </div>
    );
};
Alert.propTypes = {
    vaariant: PropTypes.oneOf(['info', 'success', 'warning', 'error']),
    title: PropTypes.string,
    message: PropTypes.string,
    icon: PropTypes.node,
    closable: PropTypes.bool,
    onClose: PropTypes.func,
    className: PropTypes.string
};
export default Alert;
