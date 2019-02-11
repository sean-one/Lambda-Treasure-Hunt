import React, { Component } from 'react';
import './App.css';

// Components
import Movement from './Movement/Movement';
import Room from './Room/Room';

class App extends Component {
  constructor() {
    super();
  }
  componentDidMount() {
    
  }
  render() {
    return (
      <div className="App">
        <h1>Lambda Treasure Hunt</h1>
        <Room />
        <Movement />
      </div>
    );
  }
}

export default App;
