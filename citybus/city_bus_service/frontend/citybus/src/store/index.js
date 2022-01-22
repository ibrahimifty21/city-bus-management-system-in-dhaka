import { createStore } from 'vuex'

export default createStore({
  state: {
    user:null,
    
  },
  
  actions: {
    user(context,user){
      context.commit('user',user)
    },
    error(context,value){
      context.commit('error',value)
    }

  },

  mutations: {
    user(state,user){
      state.user = user
    },
    error(state,value){
      state.error = value
    }
  },
  
})
