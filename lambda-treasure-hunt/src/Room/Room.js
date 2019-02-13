import React from 'react';

const Room = (props) => {
    return (
        <div className='room'>
            <p className='roomId'>{props.room.room_id}</p>
            <p className='roomTitle'>{props.room.title}</p>
            <p className='cooldown'>wait: {props.room.cooldown}</p>
            <p className='description'>{props.room.description}</p>
            <p className='elevation'>{props.room.elevation}</p>
            <p className='terrain'>{props.room.terrain}</p>
            <p className='items'>{props.room.items}</p>
            <p className='exits'>{props.room.exits}</p>
            <p className='messages'>{props.room.messages}</p>
            <p className='error'>{props.room.error}</p>
        </div>
    )
}

export default Room;