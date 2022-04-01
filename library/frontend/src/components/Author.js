import React from "react";
import { Link } from "react-router-dom";

const AuthorItem = ({ author }) => {
    return (
        <tr>
            <td>
                {author.first_name}
            </td>
            <td>
                {author.last_name}
            </td>
            <td>
                {author.birthday_year}
            </td>
            <td>
                <Link to={`${author.id}`}>Открыть</Link>
            </td>
        </tr>
    )
}

const AuthorList = ({ authors }) => {
    return (
        <table class="table">
            <th>
                First name
            </th>
            <th>
                Last name
            </th>
            <th>
                Birthday year
            </th>
            <th>
                Info
            </th>

            {authors.map((author) => <AuthorItem author={author} />)}
        </table>
    )
}

export default AuthorList
