//src/components/common/Breadcrumb.jsx 

import React from 'react';
import { Link } from 'react-router-dom';
import PropTypes from 'prop-types';
import './common.css';

const Breadcrumb = ({ items }) => {
    return (
        <nav className="breadcrumb">
            {items.map((item, index) => (
                <span key={index} className="breadcrumb-item">
                    {item.url ? (
                        <Link to={item.url}>{item.label}</Link>
                    ) : (
                        <span>{item.label}</span>
                    )}
                    {index < items.length - 1 && <span className="breadcrumb-separator"> / </span>}
                </span>
            ))}
        </nav>
    );
};
Breadcrumb.propTypes = {
    items: PropTypes.arrayOf(
        PropTypes.shape({
            label: PropTypes.string.isRequired,
            url: PropTypes.string,
        })
    ).isRequired,
};
export default Breadcrumb;
