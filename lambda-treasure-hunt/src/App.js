import React, { Component } from 'react';
import './App.css';
import locations from '../src/python/locations.json'

class App extends Component {
  constructor() {
    super();
    this.state = {
      mapGraph: locations,
    }
  }
  render() {
    console.log(locations)
    return (
      <div className="App">
        {this.state.locations.map(roomID => <div>{roomID}</div>)}
      </div>
    );
  }
}

export default App;
