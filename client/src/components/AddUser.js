import React from "react";
import { connect } from "react-redux";
import { addUser } from "../redux/actions/addUser";

class AddUser extends React.Component {
  constructor(props) {
    super(props);
    this.state = { username: "", email: "", password: "" };
    this.updateInput = this.updateInput.bind(this);
  }

  updateInput = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  handleAddUser = () => {
    // e.preventDefault();
    this.props.addUser(this.state);
    this.setState({ username: "", email: "", password: "" });
  };

  render() {
    return (
      <div>
        <label>Username: </label>
        <input
          onChange={e => this.updateInput(e)}
          value={this.state.username}
          name="username"
        />
        <label>email: </label>
        <input
          onChange={e => this.updateInput(e)}
          value={this.state.email}
          name="email"
          type="email"
        />
        <label>password: </label>
        <input
          onChange={e => this.updateInput(e)}
          value={this.state.password}
          name="password"
        />
        <button className="add-user" onClick={this.handleAddUser}>
          Create User
        </button>
      </div>
    );
  }
}

export default connect(
  null,
  { addUser }
)(AddUser);
