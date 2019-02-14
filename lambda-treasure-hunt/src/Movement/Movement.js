import React from 'react';

import './Movement.css';

const Movement = (props) => {
    return (
        <div>
            <button id='n' onClick={props.mover}>North</button>
            <button id='w' onClick={props.mover}>West</button>
            <button id='e' onClick={props.mover}>East</button>
            <button id='s' onClick={props.mover}>South</button>
        </div>
    )
}

export default Movement;