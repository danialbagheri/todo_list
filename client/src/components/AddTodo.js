import React from "react";
import { connect } from "react-redux";
import { addTodo } from "../redux/actions/addTodo";

class AddTodo extends React.Component {
  constructor(props) {
    super(props);
    this.state = { project_number: "" };
    this.updateInput = this.updateInput.bind(this);
  }

  updateInput = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  handleAddTodo = () => {
    this.props.addTodo(this.state);
    this.setState({ project_number: "" });
  };

  render() {
    return (
      <div>
        <div>Requested by:</div>
        <label>Project Number: </label>
        <input
          onChange={e => this.updateInput(e)}
          value={this.state.project_number}
          name="project_number"
        />
        <label>Required Date: </label>
        <input
          onChange={e => this.updateInput(e)}
          value={this.state.project_number}
          name="project_number"
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
