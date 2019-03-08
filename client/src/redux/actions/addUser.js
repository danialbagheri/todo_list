import { ADD_USER_STARTED, ADD_USER_SUCCESS } from "../actionTypes";

const url = "http://127.0.0.1:8000/addtodo";
export const addUser = data => dispatch => {
  console.log("adding user...");
  dispatch(addUserStarted());
  // Default options are marked with *
  fetch(url, {
    method: "POST", // *GET, POST, PUT, DELETE, etc.
    mode: "cors", // no-cors, cors, *same-origin
    body: JSON.stringify(data) // body data type must match "Content-Type" header
  })
    .then(res => res.json())
    .then(data => dispatch(addUserSuccess(data))); // parses response to JSON
};

const addUserStarted = () => ({
  type: ADD_USER_STARTED
});

const addUserSuccess = users => ({
  type: ADD_USER_SUCCESS,
  payload: {
    ...users
  }
});
