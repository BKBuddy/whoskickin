import React, { Component } from 'react';
import _ from 'lodash';
import Game from './game.js';

export default class GameList extends Component {
    constructor(props){
        super(props);
        this.state = null;
    }

    componentDidUpdate(prevProps){
        if(prevProps.gameData !==  this.props.gameData){
            return this.setState({gameData: this.props.gameData})
        }
    }

    render(){
        return (
            <div>
                <div className='searchBox'>
                    <input 
                        type='text'
                        placeholder='search teams...'
                        onChange={e => this.handleChange(e)}>
                    </input>
                    {this.state && _.values(this.state.gameData).map((game, i) => {
                        return (<Game key={i}
                                    home_team={game.home_team_abbr}
                                    away_team={game.away_team_abbr}
                                    kicking_team={game.kicking_team}>
                                </Game>);
                    })}
                </div>
            </div>
        )
    }

    handleChange(e){
        if(e.target.value === "") {
             return this.setState({gameData: this.props.gameData})
        }
        let filteredGames = _.pickBy(this.props.gameData, game => {
           const userInput = e.target.value.toLowerCase();
           const home_team_searchable_name = game.home_team_searchable_name.toLowerCase();
           const away_team_searchable_name = game.away_team_searchable_name.toLowerCase();
           if(home_team_searchable_name.includes(userInput) || away_team_searchable_name.includes(userInput)) {
               return game;
           }
        });
        this.setState({gameData: filteredGames});
    }

    
}