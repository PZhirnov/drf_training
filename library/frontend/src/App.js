import React from 'react';
import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Author';
import BookList from './components/Books';
import LoginForm from './components/Auth';
import Menu from './components/Menu';
import Footer from './components/Footer';
import BookForm from './components/BookForm';

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

    set_token (token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, () => this.load_data())  
    }

    is_authenticated() {
        //console.log(this.state.token)
        return this.state.token != ''
    }

    logout() {
        this.set_token('')
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, () => this.load_data())
    }

    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
        .then(response => {
            this.set_token(response.data['token'])
        }).catch(error => alert('Неверный логин или пароль'))
    }

    get_headers() {
        console.log('сработал')
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.is_authenticated())
        {
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }

    
    get_token(username, password) {
    axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username,
    password: password})
    .then(response => {
    this.set_token(response.data['token'])
    }).catch(error => alert('Неверный логин или пароль'))
    }
    get_headers() {
    let headers = {
    'Content-Type': 'application/json'
    }
    if (this.is_authenticated())
    {
    headers['Authorization'] = 'Token ' + this.state.token
    }
    return headers
    }
    load_data() {
        const headers = this.get_headers()
        axios.get('http://127.0.0.1:8000/api/authors/', {headers})
        .then(response => {
        this.setState({authors: response.data})
        }).catch(error => {
            console.log(error)
            this.setState({authors: []})
        })
        
        axios.get('http://127.0.0.1:8000/api/books/', {headers})
        .then(response => {
            console.log(response.data)
        this.setState({books: response.data})
        }).catch(error => {
        console.log(error)
        this.setState({books: []})
        })
    }

    deleteBook(id) {
        const headers=this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/books/${id}/`, {headers, headers})
        .then(response => {
            this.setState({books: this.state.books.filter((book) => book.id !== id)})
        }).catch(error => {console.log(error)})
    }

    createBook(name, author) {
        console.log('сработал')
        const headers=this.get_headers()
        console.log(headers)
        const data = {name: name, authors: [author]}
        axios.post(`http://127.0.0.1:8000/api/books/`, data, {headers, headers})
        .then(response => {
            let new_book = response.data
            const author = this.state.authors.filter((item) => item.id === new_book.author)[0]
            new_book.author = author
            this.setState({books: [...this.state.books, new_book]})
        }).catch(error => console.log(error))
    }
    


    componentDidMount() {
        this.get_token_from_storage();
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
                                {this.is_authenticated() ? <button onClick={()=>this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
                            </li>
                        </ul>
                    <Switch>
                        <Route exact path='/authors/' component={() => <AuthorList authors={this.state.authors} />}></Route>
                        <Route exact path='/books/' component={() => <BookList books={this.state.books} deleteBook={(id) => this.deleteBook(id)} />}></Route>
                        <Route exact path='/books/create' component={() => <BookForm authors={this.state.authors} createBook={(name, author) => this.createBook(name, author)} />} /> 
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
