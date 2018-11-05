import React, { Component } from 'react';
import '../stylesheets/game.css';

export default class Game extends Component {
    render(){
        return (
            <div className='gameContainer'>
                <div className={this.props.home_team}>
                    @{this.props.home_team}
                </div>
                <div className={this.props.away_team}>
                    {this.props.away_team}
                </div>
            </div>
        )
    }
}