import React from "react";
import { Link } from "react-router-dom";

const BookItem = ({ book, deleteBook }) => {
    return (
        <tr>
            <td>
                {book.name}
            </td>
            <td>
                {book.authors}
            </td>
            <td>
                <button type='button' onClick={() => deleteBook(book.id)}>Delete {book.id}</button>
            </td>
        </tr>
    )
}

const BookList = ({ books, deleteBook }) => {
    return (
        <div>
            <table class="table">
                <th>
                    Title
                </th>
                <th>
                    Authors
                </th>
                <th>
                    Delete
                </th>
                {books.map((book) => <BookItem book={book} deleteBook={deleteBook} />)}
            </table>
            <Link to='/books/create'>Create</Link>
        </div>
        
    )
}

export default BookList
