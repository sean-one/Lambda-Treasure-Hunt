// import dotenv from 'dotenv';
import React, { Component } from 'react';
import axios from 'axios';
import './App.css';

// Components
import Header from './Header/Header';
import Movement from './Movement/Movement';
import Map from './Map/Map';
import Room from './Room/Room';

require("dotenv").config();

class App extends Component {
  constructor() {
    super();
    this.state = {
      'currentRoom' : {}
    }

  }
  // componentDidMount() {
  //   const authKey = `Token ${process.env.REACT_APP_TOKEN_KEY}`
  //   axios.get(`${process.env.REACT_APP_BASE_URL}init/`, { headers: { 'Authorization': authKey } })
  //     .then(res => {
  //       this.setState({
  //         'currentRoom': res.data
  //       })
  //     })
  // }
  mover = (event) => {
    console.log(event.currentTarget.id)
  }
  render() {
    return (
      <div className="App">
        <Header />
        <div className="main">
          <Map />
          <div className='controls'>
            <Room room={this.state.currentRoom}/>
            <Movement mover={this.mover}/>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
