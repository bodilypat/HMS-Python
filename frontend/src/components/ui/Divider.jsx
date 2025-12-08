//src/components/ui/Divider.jsx 

import React from 'react';
import classNames from 'classnames';
import PropTypes from 'prop-types';
import './ui.css';

/* Divider Component */
const Divider = ({ 
    orientation = 'horizontal',
    color = '#e5e7eb',
    thickness ='1px',
    margin = '0.5rem 0',
    className
 }) => {
    const dividerClass = classNames(
        'divider',
        `divider-${orientation}`,
        className
    );

    const style = {
        backgroundColor: color,
        ...(orientation === 'horizontal'
            ? { height: thickness, width: '100%', margin }
            : { width: thickness, height: '100%', margin }
        )        
    };
    return <div className={dividerClass} style={style} />;
};
Divider.propTypes = {
    orientation: PropTypes.oneOf(['horizontal', 'vertical']),
    color: PropTypes.string,
    thickness: PropTypes.string,
    margin: PropTypes.string,
    className: PropTypes.string
};
