import React from 'react';

const Location = (props) => {
    return (
        <p>{props.location[1].coordinates}</p>
    )
}

export default Location;