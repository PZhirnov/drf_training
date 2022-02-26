import React from 'react';
import logo from './logo.svg';
import './App.css';
import AuthorLIst from './components/Author';

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'authors': []
        };
    }

    componentDidMount() {
        const authors = [
            {
                'first_name': 'Федор',
                'last_name': 'Достоевский',
                'birthday_year': 1821
            },
            {
                'first_name': 'Александр',
                'last_name': 'Грин',
                'birthday_year': 1880
            },
        ]
        this.setState(
            {
                'authors': authors
            }
        )
    }

    render () {
        return (
            <div>
                <AuthorLIst authors={this.state.authors}/>
            </div>
        )
    }
}

export default App;
