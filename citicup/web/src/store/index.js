import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    token: window.sessionStorage.getItem('token'),
    login:false,
    user:JSON.parse(window.sessionStorage.getItem('user'))
  },
  mutations: {
    LOGIN: (state, data) => {
      //更改token的值
      state.token = data;
      window.sessionStorage.setItem('token', data);
      state.login=true;
    },
    LOGOUT: (state) => {
      //登出的时候要清除token
      state.token = null;
      window.sessionStorage.removeItem('token');
      state.login=false;
      state.user={};
    },
    USER:(state,data)=>{
      state.user=data;
      window.sessionStorage.setItem('user',JSON.stringify(data));
    }
  },
  actions: {
  },
  modules: {
  }
})
