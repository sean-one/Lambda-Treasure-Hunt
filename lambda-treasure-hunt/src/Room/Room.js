import React from 'react';

const Room = (props) => {
    return (
        <div className='room'>
            <p className='roomId'>0</p>
            <p className='roomTitle'>A brightly lit room</p>
            <p className='description'>You are standing in the center of a brightly lit room. You notice a shop to the west and exits to the north, south and east.</p>
            <p className='elevation'>0</p>
            <p className='terrain'>NORMAL</p>
            <p className='items'>[]</p>
            <p className='exits'>[]</p>
            <p className='messages'>You have walked west.</p>
            <p className='error'></p>
        </div>
    )
}

export default Room;