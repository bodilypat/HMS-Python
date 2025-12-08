//src/components/ui/Avatar.jsx

import React from 'react';
import PropTypes from 'prop-types';
import classNames from 'classnames';

/* Avatar Components */
const Avatar = ({ src, alt, size, className, status }) => {
    const sizeClasses = {
        small: 'w-8 h-8',
        medium: 'w-12 h-12',
        large: 'w-16 h-16',
    };

    const statusColors = {
        online: 'bg-green-500',
        offline: 'bg-gray-400',
        busy: 'bg-red-500',
        away: 'bg-yellow-500',
    };

    return (
        <div className={classNames('relative inline-block', className)}>
            {src ? (
                <img 
                        src={src} 
                        alt={alt} 
                        className={classNames('rounded-full object-cover', 
                        sizeClasses[size]
                    )}
                />
                ) : (
                    <div className={classNames(
                        'rounded-full bg-gray-300 flex items-center justify-center', 
                        sizeClasses[size]
                    )}
                    >
                    {initials || '?'}
                    </div> 
                )}
                {status && (
                <span 
                    className={classNames(
                        'absolute bottom-0 right-0 block w-4 h-4 rounded-full border-2 border-white',
                        statusColors[status]
                    )}
                />
            )}
        </div>
    );
};

Avatar.propTypes = {
    src: PropTypes.string,
    alt: PropTypes.string.isRequired,
    size: PropTypes.oneOf(['small', 'medium', 'large']),
    className: PropTypes.string,
    initials: PropTypes.string,
    status: PropTypes.oneOf(['online', 'offline', 'busy', 'away']),
};

export default Avatar;