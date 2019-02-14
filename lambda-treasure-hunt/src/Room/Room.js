import React from 'react';

import './Room.css';

const Room = (props) => {
    return (
        <div className='information'>
            <p className='roomId'><strong>Current Room:</strong> {props.room.room_id}</p>
            <p className='roomTitle'><strong>Room Title:</strong> {props.room.title}</p>
            <p className='cooldown'><strong>Cooldown:</strong> {props.room.cooldown}</p>
            <p className='description'><strong>Room Description:</strong> {props.room.description}</p>
            <p className='elevation'><strong>Elevation:</strong> {props.room.elevation}</p>
            <p className='terrain'><strong>Terrain:</strong> {props.room.terrain}</p>
            <p className='items'><strong>Available Items:</strong> {props.room.items}</p>
            <p className='exits'><strong>Exits:</strong> {props.room.exits}</p>
            <p className='messages'><strong>Message:</strong> {props.room.messages}</p>
            <p className='error'><strong>Error Message:</strong> {props.room.error}</p>
        </div>
    )
}

export default Room;