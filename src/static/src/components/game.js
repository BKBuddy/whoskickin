import React, { Component } from 'react';
import '../stylesheets/game.css';
import 'bootstrap';

const LOGO_PATH = '../../public/logos';

export default class Game extends Component {
    render(){
        return (
            <div className='gameContainer'>
                <div className='border team'>
                    <img src={`${LOGO_PATH}/${this.props.home_team}.png`} alt=''></img>
                    @{this.props.home_team}
                </div>
                <div></div>
                <div className='border team'>
                    <img src={`${LOGO_PATH}/${this.props.away_team}.png`} alt=''></img>
                    {this.props.away_team}
                </div>
            </div>
        )
    }
}