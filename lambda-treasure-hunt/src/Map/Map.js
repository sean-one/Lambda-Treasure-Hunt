import React, { Component } from 'react';
import Location from './Location'

import locations from '../python/locations.json'

const mapLocations = []
for (let i in locations) {
    mapLocations.push([i, locations[i]])
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
        <div>
            {this.state.mapLocations.map(location => {
                return (
                    <div key={location[0]}>
                        <Location location={location} />
                    </div>
                )
            })}
        </div>
        )
    }
}

export default Map;