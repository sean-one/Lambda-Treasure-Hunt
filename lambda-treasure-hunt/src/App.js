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
        <h1>THIS IS THE HEADER</h1>
      </div>
    );
  }
}

export default App;
