import { createStore, applyMiddleware } from "redux";
import rootReducer from "./reducers";
import thunk from "redux-thunk";

const initalState = {};

const store = createStore(rootReducer, initalState, applyMiddleware(thunk));
export default store;
