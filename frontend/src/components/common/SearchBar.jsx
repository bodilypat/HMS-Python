//src/components/common/SearchBar.jsx

import React from 'react';
import PropTypes from 'prop-types';
import './common.css';

/* SearchBar Component */
const SearchBar = ({ 
    value,
    onChange,
    onClear,
    placeholder = 'Search',
    autoFocus = false,
    className,
    inputClass,
    showClear = true,
 }) => {
    return (
        <div className={`search-bar ${className || ''}`}>
            {/* Search Icon */}
            <span className="search-icon" role="img" aria-label="search">🔍</span>
            {/* Search Input */}
            <input
                type="text"
                value={value}
                onChange={(e) => onChange(e.target.value)}
                placeholder={placeholder}
                autoFocus={autoFocus}
                className={`search-input ${inputClass || ''}`}
            />
            {/* Clear Button */}
            {showClear && value && (
                <button 
                    className="clear-button"
                    onClick={onClear}
                    aria-label="clear search"
                >
                    ✖
                </button>
            )}
        </div>
    );
};

SearchBar.propTypes = {
    value: PropTypes.string.isRequired,
    onChange: PropTypes.func.isRequired,
    onClear: PropTypes.func,
    placeholder: PropTypes.string,
    autoFocus: PropTypes.bool,
    className: PropTypes.string,
    inputClass: PropTypes.string,
    showClear: PropTypes.bool,
};

export default SearchBar;

