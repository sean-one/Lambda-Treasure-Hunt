import React from 'react';
import './Location.css';

const Location = (props) => {
    const plot = {
        bottom: (props.location.coordinates[1] - 46) * 70,
        right: (30 - (props.location.coordinates[0] - 50)) * 70
    };
    const exits = {
        height: '100%',
        width: '100%',
        borderTop: (props.location.exits.includes("n")) ? 'none' : '1px black solid',
        borderBottom: (props.location.exits.includes("s")) ? 'none' : '1px black solid',
        borderRight: (props.location.exits.includes("e")) ? 'none' : '1px black solid',
        borderLeft: (props.location.exits.includes("w")) ? 'none' : '1px black solid'
    }

    return (
        <div className='room' style={plot}>
            <p style={exits}>{props.location.room_id}</p>
        </div>
    )
}

export default Location;