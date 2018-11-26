import React, { Component } from 'react';
import '../stylesheets/game.css';
import 'bootstrap';

const LOGO_PATH = '../../public/logos';

export default class Game extends Component {
    render(){
        const { home_team, away_team, kicking_team } = this.props
        const receiving_team = kicking_team === away_team ? home_team : away_team
        return (
            <div className='gameContainer'>
                <div className='border team'>
                    <img src={`${LOGO_PATH}/${kicking_team}.png`} alt=''></img>
                    {kicking_team === away_team ? `@ ${kicking_team}` : kicking_team}
                </div>
                <div></div>
                <div className='border team'>
                    <img src={`${LOGO_PATH}/${this.props.receivingTeam}.png`} alt=''></img>
                    {receiving_team === away_team ? `@ ${receiving_team}` : receiving_team}
                </div>
            </div>
        )
    }
}