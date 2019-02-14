import React from 'react';
import './Location.css';

const Location = (props) => {
    const plot = {
        bottom: (props.location.coordinates[1] - 46) * 68,
        right: (30 - (props.location.coordinates[0] - 45)) * 68
    };
    const edges = props.location.exits
    // n - border-top
    // s - border-bottom
    // e - border-left
    // w - border-right
    console.log(edges)
    return (
        <div className='room' style={plot}>
            <p>{props.location.room_id}</p>
        </div>
    )
}

export default Location;