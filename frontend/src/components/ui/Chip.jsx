//src/components/Chip.jsx 

import React from 'react';
import classNames from 'classnames';
import PropTypes from 'prop-types';
import './ui.css';

/* Chip component */
const Chip = ({ 
    label,
    variant = 'primary',
    size = 'md',
    icon,
    onRemove, 
    className }) => {
    const chipClass = classNames(
        'chip',
        `chip-${variant}`,
        `chip-${size}`,
        className
    );

    return (
        <div className={chipClass}>
            {icon && <span className="chip-icon">{icon}</span>}
            <span className="chip-label">{label}</span>
            {onRemove && (
                <button
                    className="chip-remove"
                    onClick={onRemove}
                    aria-label="Remove chip"
                >
                    &times;
                </button>
            )}
        </div>
    );
};
Chip.propTypes = {
    label: PropTypes.string.isRequired,
    variant: PropTypes.oneOf(['primary', 'secondary', 'success', 'danger', 'warning']),
    size: PropTypes.oneOf(['sm', 'md', 'lg']),
    icon: PropTypes.node,
    onRemove: PropTypes.func,
    className: PropTypes.string
};

export default Chip;
