import React, { Component } from 'react';
import Location from './Location'
import './Map.css'

import locations from '../python/locations.json'

const mapLocations = []
for (let i in locations) {
    mapLocations.push(locations[i])
}
class Map extends Component{
    constructor() {
        super();
        this.state = {
            mapLocations: mapLocations,
        }
    }

    getRoom = (event) => {
        console.log(event.currentTarget.id)
    }

    render() {
        return (
        <div className='map'>
            {this.state.mapLocations.map(location => {
                return (
                    <div id={location.room_id} onClick={this.getRoom} key={location.room_id}>
                        <Location room={this.props.room} location={location} />
                    </div>
                )
            })}
        </div>
        )
    }
}

export default Map;