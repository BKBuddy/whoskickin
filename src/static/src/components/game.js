import React, { Component } from 'react';
import '../stylesheets/game.css';
import 'bootstrap';

export default class Game extends Component {
    render(){
        return (
            <div className='border gameContainer'>
                <div className='team'>
                    @{this.props.home_team}
                </div>
                <div></div>
                <div className='team'>
                    {this.props.away_team}
                </div>
            </div>
        )
    }
}