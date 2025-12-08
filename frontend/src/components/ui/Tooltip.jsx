//src/components/ui/Tooltip.jsx

import React from 'react';
import PropTypes from 'prop-types';
import classNames from 'classnames';
import './ui.css';

const Tooltip = ({ 
    text,
    position = 'top',
    children,
    controlled = false,
    open = false,
    className,
    tooltipClass
 }) => {
    const [visible, setVisible] = React.useState(false);

    const showTooltip = () => {
        if (!controlled) {
            setVisible(true);
        }
    };

    const hideTooltip = () => {
        if (!controlled) {
            setVisible(false);
        }
    };

    const isVisible = controlled ? open : visible;

    return (
        <div
            className={classNames('tooltip-container', className)}
            onMouseEnter={showTooltip}
            onMouseLeave={hideTooltip}
        >
            {children}
            {isVisible && (
                <div className={classNames('tooltip-box', `tooltip-${position}`, tooltipClass)}>
                    {text}
                </div>
            )}
        </div>
    );
};
Tooltip.propTypes = {
    text: PropTypes.string.isRequired,
    position: PropTypes.oneOf(['top', 'bottom', 'left', 'right']),
    children: PropTypes.node.isRequired,
    controlled: PropTypes.bool,
    open: PropTypes.bool,
    className: PropTypes.string,
    tooltipClass: PropTypes.string
};
