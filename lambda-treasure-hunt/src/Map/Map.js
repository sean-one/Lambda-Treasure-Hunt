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

    render() {
        return (
        <div className='map'>
            {this.state.mapLocations.map(location => {
                return (
                    <div key={location.room_id}>
                        <Location location={location} />
                    </div>
                )
            })}
        </div>
        )
    }
}

export default Map;