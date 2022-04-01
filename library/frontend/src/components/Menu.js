import React from "react";
import {HashRouter, Route, Link, BrowserRouter} from "react-router-dom";

const Menu = () => {
    return (
        <nav class="navbar navbar-expand navbar-dark bg-dark" aria-label="Second navbar example">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">Library</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarsExample02" aria-controls="navbarsExample02" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <BrowserRouter>
                    <div class="collapse navbar-collapse" id="navbarsExample02">
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
                        </ul>
                        <form>
                            <input class="form-control" type="text" placeholder="Search" aria-label="Search"></input>
                        </form>
                    </div>
                </BrowserRouter>
            </div>
        </nav>
    )
}

export default Menu
