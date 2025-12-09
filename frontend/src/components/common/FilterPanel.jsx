//src/components/common/FilterPanel.jsx 

import React from 'react';
import PropTypes from 'prop-types';
import './common.css';

/* FilterPanel component */
const FilterPanel = ({ 
    filters, 
    onFilterChange 
}) => {
    return (
        <div className="filter-panel">
            {filters.map((filter) => (
                <div key={filter.id} className="filter-item">
                    <label htmlFor={filter.id}>{filter.label}</label>
                    <input
                        type="text"
                        id={filter.id}
                        value={filter.value}
                        onChange={(e) => onFilterChange(filter.id, e.target.value)}
                    />
                </div>
            ))}
        </div>
    );
}
FilterPanel.propTypes = {
    filters: PropTypes.arrayOf(
        PropTypes.shape({
            id: PropTypes.string.isRequired,
            label: PropTypes.string.isRequired,
            value: PropTypes.string.isRequired,
        })
    ).isRequired,
    onFilterChange: PropTypes.func.isRequired,
};

export default FilterPanel;
