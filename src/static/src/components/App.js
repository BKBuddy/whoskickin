import React, { Component } from 'react';
import _ from 'lodash';
import 'jquery';
import 'popper.js'
import 'bootstrap';
import axios from 'axios';
import GameList from './gameList.js';
import '../stylesheets/app.css'

class App extends Component {

  constructor(props) {
    super(props);
    this.state = {};
  }

  async componentDidMount(){
    const response = await this.getGameData()
    return this.setState(response.data);
  }

  render() {
    return (
      <div className="container">
        <div className='row justify-content-center'>
          <GameList gameData={this.state} ></GameList>
        </div>
      </div>
    );
  }

  async getGameData(){
    return await axios.get('http://localhost:5000/all_kicks');
  }
}

export default App;
