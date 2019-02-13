import React, { Component } from 'react';
import Location from './Location'

import locations from '../python/locations.json'

class Map extends Component{
    constructor() {
        super();
        this.state = {
            mapLocations : locations
        }
    }
    render() {
        return (
        <div>
            {this.state.mapLocations.map((location) => (
                <Location location={location}/>
            ))}
        </div>
        )
    }
}

export default Map;