import React from 'react';
import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Author';
import BookList from './components/Books';
import LoginForm from './components/Auth';
import Menu from './components/Menu';
import Footer from './components/Footer';

import axios from 'axios';
import {HashRouter, Route, Link, BrowserRouter, Switch} from 'react-router-dom';
import Cookies from 'universal-cookie';


const main_page = ({location}) => {
    return (
        <div>
            <h1>Главная страница '{location.pathname}'</h1>
            <h2>Выберите интересующий вас раздел</h2>
            <Link to='/authors/'>Авторы</Link>
        </div>
    )


};

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'authors': [],
            'books': [],
            'token': '',
        };
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/authors/')
            .then(Response => {
                const authors = Response.data
                console.log(authors);
                    this.setState(
                        {
                            'authors': authors
                        }
                    )
            }).catch(error => console.log(error));
        axios.get('http://127.0.0.1:8000/api/books/')
            .then(Response => {
                const books = Response.data
                console.log(books)
                    this.setState(
                        {
                            'books': books
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
    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
        .then(response => {
        console.log(response.data)
        }).catch(error => alert('Неверный логин или пароль'))
        }

    render() {
        return (
            <div className ='App'> 
                
                <BrowserRouter>
                        <ul class="navbar-nav me-auto">
                            <li class="nav-item">
                                <Link to='/'>Главная</Link>  
                            </li>
                            <li class="nav-item">
                                <Link to='/authors/'>Авторы</Link>
                            </li>
                            <li class="nav-item">
                                <Link to='/books/'>Книги</Link>
                            </li>
                            <li class="nav-item">
                                <Link to='/login'>Login</Link>
                            </li>
                        </ul>
                    <Switch>
                        <Route exact path='/authors/' component={() => <AuthorList authors={this.state.authors} />}></Route>
                        <Route exact path='/books/' component={() => <BookList books={this.state.books} />}></Route>
                        <Route exact path='/' component={main_page}></Route>
                        <Route exact path='/login' component={() => <LoginForm get_token={(username, password) => this.get_token(username, password)} />} />

                    </Switch>
                    
                </BrowserRouter>
               

                <Footer />
            </div>
        )
    }
}

export default App;
