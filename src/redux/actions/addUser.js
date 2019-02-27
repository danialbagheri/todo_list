import { ADD_USER_STARTED, ADD_USER_SUCCESS } from "../actionTypes";

const url = "http://127.0.0.1:8082/add-user";
export const addUser = data => dispatch => {
  console.log("adding user...");
  dispatch(addUserStarted());
  // Default options are marked with *
  fetch(url, {
    method: "POST", // *GET, POST, PUT, DELETE, etc.
    mode: "cors", // no-cors, cors, *same-origin
    // cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
    // credentials: "same-origin", // include, *same-origin, omit
    // headers: {
    //   "Content-Type": "application/json"
    //   // "Content-Type": "application/x-www-form-urlencoded",
    // },
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
