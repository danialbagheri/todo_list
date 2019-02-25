import React from "react";
import { connect } from "react-redux";
import { addTodo } from "../redux/actions";

class AddTodo extends React.Component {
  constructor(props) {
    super(props);
    this.state = { requested_by: "", input: "" };
    this.updateInput = this.updateInput.bind(this);
  }

  updateInput = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  handleAddTodo = () => {
    this.props.addTodo(this.state);
    this.setState({ input: "", requested_by: "" });
  };

  render() {
    return (
      <div>
        <label>Requested by: </label>
        <input
          onChange={e => this.updateInput(e)}
          value={this.state.requested_by}
          name="requested_by"
        />
        <label>Job: </label>
        <input
          onChange={e => this.updateInput(e)}
          value={this.state.input}
          name="input"
        />
        <button className="add-todo" onClick={this.handleAddTodo}>
          Add Todo
        </button>
      </div>
    );
  }
}

export default connect(
  null,
  { addTodo }
)(AddTodo);
