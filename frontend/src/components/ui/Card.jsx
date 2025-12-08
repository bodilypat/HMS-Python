//src/components/ui/Card.jsx 

import React from 'react';
import classNames from 'classnames';
import PropTypes from 'prop-types';
import './ui.css';

/* Card Component */
const Card = ({ 
    children,
    header,
    footer,
    className,
    shadow = true,
    border = true, 
    hoverabvle = false }) => {
    return (
        <div className={cardClass}>
            {header && <div className="card-header">{header}</div>}
            <div className="card-body">
                {children}
            </div>
            {footer && <div className="card-footer">{footer}</div>} 
        </div>
    );
};
Card.propTypes = {
    children: PropTypes.node.isRequired,
    header: PropTypes.node,
    footer: PropTypes.node,
    className: PropTypes.string,
    shadow: PropTypes.bool,
    border: PropTypes.bool,
    hoverable: PropTypes.bool,
};
export default Card;

