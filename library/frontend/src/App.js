import React from 'react';
import logo from './logo.svg';
import './App.css';
import AuthorLIst from './components/Author';
import Menu from './components/Menu';
import Footer from './components/Footer';
import axios from 'axios';

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'authors': []
        };
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/authors')
            .then(Response => {
                const authors = Response.data
                    this.setState(
                        {
                            'authors': authors
                        }
                    )
            }).catch(error => console.log(error));
    }

    /*componentDidMount() {
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
    }*/

    render() {
        return (
            <div>
                <Menu />
                <AuthorLIst authors={this.state.authors} />
                <Footer />
            </div>
        )
    }
}

export default App;
