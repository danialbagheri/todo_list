import { ADD_USER_SUCCESS, ADD_USER_STARTED } from "../actionTypes";

const initialState = {
  loading: false,
  user: [],
  error: null
};

export default (state = initialState, action) => {
  switch (action.type) {
    case ADD_USER_STARTED:
      console.log("user-started");
      return {
        ...state,
        loading: true
      };
    case ADD_USER_SUCCESS:
      console.log("user-added");
      return {
        ...state,
        loading: false,
        error: null,
        user: [...state.user, action.payload]
      };
    default:
      return state;
  }
};
