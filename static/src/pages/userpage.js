var React = require('react');
var api = require('../api.js');

class User extends React.Component {

	constructor() {
		super();
		this.state = {data: null};
	}

	componentDidMount() {
		api.getUser(this.props.params.userId, (err, data) => {
			if (err) console.err("[UserPage:componentDidMount] There's been an error retrieving data!");
			else {
				this.setState({data: data.user});
			}
		});
	}

	render() {
		var data = this.state.data;
		console.log(data);
		if (data) {
			return (
				<div className="user-page">
					<div className="container-fluid">
						<h3>User</h3>
						<p>Name: {data.name}</p>
						<div>
							<h3>Borrowed Books</h3>
							{data.borrowed_books.map( book => {
								return (<p>{book.title}</p>)
							})}
						</div>
						<div>
							<h3>Reviews</h3>
							{data.reviews.map( review => {
								return (<p>{review.description}</p>)
							})}
						</div>
					</div>
				</div>
			)
		} else {
			return (<div></div>)
		}
	}
}


module.exports = User;
