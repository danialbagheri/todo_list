import { ADD_TODO, FETCH_TODOS } from "../actionTypes";

const todoState = {
  allIds: [],
  byIds: {},
  todo: [],
  error: null
};

export default (state = todoState, action) => {
  switch (action.type) {
    case FETCH_TODOS:
      return {
        ...state,
        todo: [...state.todo, action.payload]
      };
    case ADD_TODO:
      console.log("todo-added");
      return {
        ...state,
        loading: false,
        error: null,
        todo: [...state.todo, action.payload]
      };
    default:
      return state;
  }
};
console.log(todoState);
