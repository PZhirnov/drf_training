import React from "react";

class BookForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {name: '', author: props.authors[0]?.id}
    }
    
    handleChange(event){
        this.setState({
            [event.target.name]: event.target.value
        })
    }

    handleSubmit(event){
        console.log(this.state.name)
        console.log(this.state.author)
        console.log(this.props)
        this.props.createBook(this.state.name, this.state.author)
        event.preventDefault()

    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <div className="form-group">
                    <label for="name">Наименование книги</label>
                    <input type="text" className="form-control" name="name" value={this.state.name}
                    onChange={(event)=>this.handleChange(event)} />
                </div>
                <div className="form-group">
                    <label for="author">Наименование книги</label>

                    {/* <input type="number" className="form-control" name="author" value={this.state.author}
                    onChange={(event)=>this.handleChange(event)} /> */}

                    <select name="author" className="form-control" onChange={(event) => this.handleChange(event)} defaultValue='--'>
                        {this.props.authors.map((author) => <option value={author.id}>{`${author.first_name} ${author.last_name}`}</option>)}
                    </select>
                </div>
                <input type="submit" className="btn btn-primary" value="Save" />
            </form>
        )

    }
}

export default BookForm